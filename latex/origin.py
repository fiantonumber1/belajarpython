import requests
import json
import os
import logging
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_latex_content_and_check_validity(url_tex: str, compiler: str = "lualatex"):
    """
    Mengecek apakah dokumen LaTeX dari URL dapat dikompilasi menjadi PDF dan mengembalikan isinya.

    Args:
        url_tex (str): URL ke file .tex yang akan dikompilasi.
        compiler (str): Compiler LaTeX yang digunakan (default: 'lualatex').

    Returns:
        Tuple[bool, str]: Tuple berisi True/False apakah valid dan isi file .tex sebagai string.
    """
    base_url = "https://texlive2020.latexonline.cc/compile"
    params = {
        "url": url_tex,
        "command": compiler
    }

    try:
        # Ambil isi file .tex
        tex_response = requests.get(url_tex, timeout=10)
        if tex_response.status_code != 200:
            return False, ""

        latex_content = tex_response.text

        # Cek validitas kompilasi
        compile_response = requests.get(base_url, params=params, timeout=30)
        if compile_response.status_code == 200 and compile_response.headers.get('Content-Type') == 'application/pdf':
            return True, latex_content
        else:
            return False, latex_content
    except requests.exceptions.RequestException:
        return False, ""


def call_reviewer(user_message):
    schema = {
        "type": "object",
        "properties": {
            "jobdesk_rate": {"type": "number"},
            "kronologis_rate": {"type": "number"},
            "language": {"type": "string", "enum": ["Indonesia", "Inggris"]}
        },
        "required": ["jobdesk_rate", "kronologis_rate", "language"],
        "propertyOrdering": ["jobdesk_rate", "kronologis_rate", "language"]
    }

    prompt = '''
Kamu adalah reviewer yang memberikan penilaian terhadap dua aspek dari sebuah pengalaman organisasi:
1. `jobdesk_rate`: Skor antara 0-1. Jika pengalaman organisasi memiliki minimal 3 jobdesk, berikan nilai 1. Jika tidak ada jobdesk, berikan 0. 
2. `kronologis_rate`: Skor antara 0-1. Jika urutan CV dimulai dari yang terbaru di atas dan makin lama di bawah, berikan nilai 1. Semakin tidak terurut kronologisnya, nilainya mendekati 0.
3. `language`: Deteksi apakah isi CV menggunakan Bahasa Indonesia atau Bahasa Inggris.

Format output JSON yang diinginkan seperti berikut:

{
  "jobdesk_rate": <nilai_float>,
  "kronologis_rate": <nilai_float>,
  "language": "Indonesia" atau "Inggris"
}

Silakan evaluasi berdasarkan deskripsi di atas:
'''

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logging.error("GEMINI_API_KEY tidak ditemukan di environment variable.")
        return {"error": "API key tidak ditemukan"}

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt + "\n" + user_message}
                ]
            }
        ],
        "generationConfig": {
            "response_mime_type": "application/json",
            "response_schema": schema
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            response_body = response.json()
            generated_text = response_body.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "{}")
            try:
                parsed_response = json.loads(generated_text)
            except json.JSONDecodeError:
                logging.error("Respons API tidak valid (bukan JSON)", {"response": generated_text})
                return {"error": "Respons API tidak valid (bukan JSON)"}

            if not parsed_response:
                logging.error("Respons API kosong atau tidak valid", {"response": generated_text})
                return {"error": "Respons API kosong atau tidak valid"}

            return parsed_response
        else:
            logging.error("Gagal memanggil Gemini API", {
                "status": response.status_code,
                "body": response.text
            })
            return {
                "error": "Gagal mendapatkan respons dari API",
                "status": response.status_code
            }
    except Exception as e:
        logging.error("Kesalahan saat memanggil Gemini API", {"error": str(e)})
        return {"error": "Kesalahan server saat memproses permintaan", "status": 500}



output_file = "dataset.jsonl"

for i in range(8100, 8171):
    url_tex = f"https://yuksyari.in/storage/documents/{i}.tex"
    check_valid, latex_content = get_latex_content_and_check_validity(url_tex)

    result = call_reviewer(latex_content)
    print("Hasil review:", result)

    is_valid = 1 if check_valid else 0
    prompt_text = f"Judul: {i} \nReward: {is_valid}"
    generated_latex = latex_content.strip()
    jobdesk=result['jobdesk_rate']
    kronologis =result['kronologis_rate']
    final_reward = is_valid * (0.15 * jobdesk + 0.15 * kronologis + 0.7)
    print(f"\n📝 Prompt: {prompt_text}")
    print(f"🔧 Output:\n{generated_latex}...")  
    print(f"🎯 Reward: {final_reward}")

    
    data = {
        "messages": [
            {"role": "user", "content": prompt_text}
        ],
        "output": generated_latex,
        "reward": final_reward
    }

    with open(output_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")
