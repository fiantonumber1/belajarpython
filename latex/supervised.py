import requests
import json
import os
import logging
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
logging.basicConfig(level=logging.INFO)

def get_latex_content_and_check_validity(url_tex: str, compiler: str = "lualatex"):
    base_url = "https://texlive2020.latexonline.cc/compile"
    params = {
        "url": url_tex,
        "command": compiler
    }

    try:
        tex_response = requests.get(url_tex, timeout=10)
        if tex_response.status_code != 200:
            return False, ""

        latex_content = tex_response.text

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
            "jobdesk_rate": {"type": "number", "format": "float"},
            "kronologis_rate": {"type": "number", "format": "float"},
            "date_format_rate": {"type": "number", "format": "float"},
            "content": {"type": "string"},
            "language": {"type": "string", "enum": ["id", "en"]}
        },
        "required": ["jobdesk_rate", "kronologis_rate", "date_format_rate", "content", "language"],
    }

    prompt = '''
Kamu adalah reviewer yang memberikan penilaian terhadap dua aspek dari sebuah pengalaman organisasi:
1. `jobdesk_rate`: Skor 0 / 1. Jika pengalaman organisasi memiliki minimal 3 jobdesk, berikan nilai 1. Jika tidak ada jobdesk, berikan 0. 
2. `kronologis_rate`: Skor 0 / 1. Jika urutan CV dimulai dari yang terbaru di atas dan makin lama di bawah, berikan nilai 1. Jika tidak berikan 0. 
3. `date_format_rate`: Apakah format penulisan tanggal konsisten? nilai 1 jika ya, 0 jika tidak.
4. `language`: Deteksi apakah isi CV menggunakan Bahasa Indonesia atau Bahasa Inggris.
5. `content`: mengubah inputan latex menjadi format text yang dapat dibaca oleh manusia.

Silakan evaluasi:
'''

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logging.error("API key tidak ditemukan.")
        return {"error": "API key tidak ditemukan"}

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

    data = {
        "contents": [{"parts": [{"text": prompt + "\n" + user_message}]}],
        "generationConfig": {
            "response_mime_type": "application/json",
            "response_schema": schema
        }
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            response_body = response.json()
            generated_text = response_body.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "{}")
            try:
                return json.loads(generated_text)
            except json.JSONDecodeError:
                logging.warning(f"Format respons tidak valid JSON: {generated_text}")
                return {}
        else:
            logging.error(f"Error dari API: {response.status_code}, {response.text}")
            return {}
    except Exception as e:
        logging.error(f"Exception saat API call: {str(e)}")
        return {}




# ---- Ambil dan proses semua data dulu ke dalam memory
all_data = []
for i in range(8161, 8171):
    url_tex = f"https://yuksyari.in/storage/documents/{i}.tex"
    check_valid, latex_content = get_latex_content_and_check_validity(url_tex)

    if not latex_content:
        logging.warning(f"Tidak bisa mengakses konten dari {url_tex}")
        continue

    review = call_reviewer(latex_content)
    if "content" not in review:
        continue

    is_valid = 1 if check_valid else 0

    item ={
        "messages": [
            {"role": "user", "content": review.get("content", "")},
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "id": "call_id",
                        "type": "function",
                        "function": {
                            "name": "get_latex_content",
                            "arguments": json.dumps({
                                "latex": latex_content.strip(),
                                "valid": 1 if is_valid else 0,
                                "language": review.get("language", "id")
                            })
                        }
                    }
                ]
            }
        ],
        "parallel_tool_calls": False,
        "tools": [
            {
                "type": "function",
                "function": {
                    "name": "get_latex_content",
                    "description": "Get the LaTeX content and check its validity",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "latex": {"type": "string", "description": "The LaTeX content to be checked"},
                            "valid": {"type": "integer", "enum": [0, 1], "description": "Indicates if the LaTeX content is valid (1) or not (0)"},
                            "language": {
                                "type": "string",
                                "enum": ["id", "en"],
                                "description": "The language of the LaTeX content, either 'id' for Indonesian or 'en' for English"
                            }
                        },
                        "required": ["latex", "valid", "language"]
                    }
                }
            }
        ]
    }



    all_data.append(item)

# ---- Shuffle and split (70% training, 30% validation)
random.shuffle(all_data)
split_index = int(0.7 * len(all_data))
train_data = all_data[:split_index]
valid_data = all_data[split_index:]

# ---- Simpan ke file .jsonl
def save_jsonl(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

save_jsonl(train_data, "train.jsonl")
save_jsonl(valid_data, "valid.jsonl")

print(f"✅ Total data: {len(all_data)} | Train: {len(train_data)} | Valid: {len(valid_data)}")
