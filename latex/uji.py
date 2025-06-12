import requests
import json
import os
import logging
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
            "jobdesk_rate": {
            "type": "number",
            "format": "float"
            },
            "kronologis_rate": {
            "type": "number",
            "format": "float"
            },
            "date_format_rate": {
            "type": "number",
            "format": "float"
            },
            "content": {
            "type": "string"
            },
            
            "language": {"type": "string", "enum": ["Indonesia", "Inggris"]}
        },
        "required": ["jobdesk_rate", "kronologis_rate",'date_format_rate','content', "language"],
    }

    prompt = '''
Kamu adalah reviewer yang memberikan penilaian terhadap dua aspek dari sebuah pengalaman organisasi:
1. `jobdesk_rate`: Skor 0 / 1. Jika pengalaman organisasi memiliki minimal 3 jobdesk, berikan nilai 1. Jika tidak ada jobdesk, berikan 0. 
2. `kronologis_rate`: Skor  0 / 1. Jika urutan CV dimulai dari yang terbaru di atas dan makin lama di bawah, berikan nilai 1. Jika tidak berikan 0. 
3. `date_format_rate`: Apakah format penulisan tanggal konsisten? nilai 1 jika ya, 0 jika tidak.
4. `language`: Deteksi apakah isi CV menggunakan Bahasa Indonesia atau Bahasa Inggris.
5. `content`: mengubah inputan latex menjadi format text yang dapat dibaca oleh manusia.

Format output JSON seperti ini:
{
  "jobdesk_rate": <nilai_float>,
  "kronologis_rate": <nilai_float>,
  "date_format_rate": <nilai_float>,
  "language": "Indonesia" atau "Inggris"
  "content" : "Mohammad Fadli Awaludin
Lulusan Teknik Pertambangan yang Termotivasi dan Berdedikasi
� +62 898-6247-072 � mohammadfadli245@gmail.com � Fadli Awaludin
� Jl. Syeh Quro Dusun Krajan IV Talagasari, Karawang, Jawa Barat 41381
Tentang Saya
Lulusan Teknik Pertambangan yang termotivasi dan berdedikasi dengan pengetahuan yang kuat tentang sistem produksi pertambangan,
analisis data, dan alat perangkat lunak pertambangan. Mahir dalam mengelola data produksi, pelaporan, dan analisis. Bersemangat
untuk berkontribusi pada lingkungan pertambangan yang dinamis. Pembelajar cepat, mudah beradaptasi, dan sangat bertanggung
jawab.
Pendidikan
Institut Teknologi Nasional Yogyakarta Yogyakarta
Sarjana Teknik Pertambangan 2019 – 2025
IPK: 3.16 / 4.00
• Berpartisipasi dalam seminar nasional, webinar, tes TOEFL, dan pelatihan teknik perangkat lunak.
SMK Negeri 1 Karawang Karawang
Teknik Komputer dan Jaringan 2016 – 2019
• Mempelajari sistem perangkat lunak dan perangkat keras.
• Menyelesaikan magang 3 bulan.
• Mempersembahkan hasil magang kepada instruktur kejuruan.
Pengalaman Kerja
PT Aneka Dharma Persada Karawang
Magang Desember 2023 – Februari 2024
• Menganalisis alur produksi dan sistem pengangkutan.
• Memantau dan mengoptimalkan produktivitas transportasi pertambangan.
• Memasukkan data penggunaan bahan bakar untuk Departemen Bahan Bakar.
• Mempersembahkan analisis penggunaan bahan bakar pada peralatan pengangkutan.
Pengalaman Organisasi
Himpunan Mahasiswa Teknik Pertambangan (HMTA) Institut Teknologi Nasional Yogyakarta
Anggota 2019 – 2025
• Berpartisipasi dalam acara tim dan rapat umum.
Himpunan Mahasiswa Teknik Pertambangan (HMTA) Institut Teknologi Nasional Yogyakarta
Komite – Mining Care, Ulang Tahun HMTA ke-18 2020 – 2021
• Merancang dan melaksanakan kegiatan penggalangan dana.
• Donasi dialokasikan untuk panti asuhan dan bantuan bencana.
Himpunan Mahasiswa Teknik Pertambangan (HMTA) Institut Teknologi Nasional Yogyakarta
Komite – Acara Pelantikan, Ulang Tahun HMTA ke-17 2019 – 2020
• Berkolaborasi dalam konsep acara dan logistik.
• Mengkoordinasikan kegiatan antar departemen untuk pelaksanaan yang lancar.
Keterampilan
Keterampilan Teknik: Microsoft Office: Word, Excel, PowerPoint
Perangkat Lunak Teknik: Google Earth, ArcMap, Global Mapper
Bahasa: Bahasa Indonesia (Lancar), Bahasa Inggris (Menengah)
Sertifikasi
Sertifikasi: Tes TOEFL – Program Bahasa Internasional (2024)
Sertifikasi: Seminar Nasional: Peran Kecerdasan Buatan dalam Mengembangkan Industri Pertambangan (2022)
Sertifikasi: Seminar Nasional: Industri Pertambangan Hilir Menurut UU No. 3 Tahun 2020 (2021)"
}

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
                parsed = json.loads(generated_text)
                return parsed
            except json.JSONDecodeError:
                logging.warning(f"Format respons tidak valid JSON: {generated_text}")
                return {"jobdesk_rate": 0.0, "kronologis_rate": 0.0, "language": "Indonesia"}
        else:
            logging.error(f"Error dari API: {response.status_code}, {response.text}")
            return {"jobdesk_rate": 0.0, "kronologis_rate": 0.0, "language": "Indonesia"}
    except Exception as e:
        logging.error(f"Exception saat API call: {str(e)}")
        return {"jobdesk_rate": 0.0, "kronologis_rate": 0.0, "language": "Indonesia"}


def calculate_reward(result: dict, is_valid: int) -> float:
    numeric_keys = [k for k in result.keys() if k.endswith("_rate")]
    total_score = sum(result[k] for k in numeric_keys)
    normalized_score = total_score / len(numeric_keys)
    return is_valid * normalized_score


# Main Execution Loop
output_file = "dataset.jsonl"

for i in range(8161, 8171):
    url_tex = f"https://yuksyari.in/storage/documents/{i}.tex"
    check_valid, latex_content = get_latex_content_and_check_validity(url_tex)

    if not latex_content:
        logging.warning(f"Tidak bisa mengakses konten dari {url_tex}")
        continue

    review = call_reviewer(latex_content)
    jobdesk = review.get("jobdesk_rate", 0.0)
    content = review.get("content", "")
    kronologis = review.get("kronologis_rate", 0.0)
    date_format_rate = review.get("date_format_rate", 0.0)
    language = review.get("language", "Indonesia")

    is_valid = 1 if check_valid else 0

    # Ubah bobot agar reward lebih bervariasi
    final_reward = calculate_reward(review, check_valid)

    print(f"\n📄 File: {i}.tex")
    print(f"✅ Valid PDF: {bool(is_valid)}")
    print(f"🔍 Review: jobdesk={jobdesk}, kronologis={kronologis}, date_format={date_format_rate}, language={language}")
    print(f"🎯 Reward: {final_reward}")

    prompt_text = content
    data = {
        "messages": [
            {"role": "user", "content": prompt_text}
        ],
        "output": latex_content.strip(),
        "reward": final_reward
    }

    with open(output_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")

#https://platform.openai.com/finetune/ftjob-ReEQGIZqfnwNUEghH1OU53D5?filter=all