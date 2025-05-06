from flask import Flask, request, render_template, send_file, redirect, url_for
import os, time, json, shutil
import pyautogui
import base64
import requests
import subprocess
from zipfile import ZipFile
from dotenv import load_dotenv
from threading import Thread

# Load .env file
load_dotenv()

app = Flask(__name__)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

PROMPT_TEMPLATE = """
Kamu adalah asisten virtual (seperti Jarvis) yang menjalankan komputer saya.

Tugas utama: [TUJUAN_SAYA]

Jika sebuah aksi dapat dilakukan menggunakan CMD (Command Prompt), prioritaskan gunakan CMD terlebih dahulu.
Jika tidak bisa menggunakan CMD, baru gunakan klik, ketik, atau tekan tombol.

Saat saya kirim screenshot layar, balas hanya dalam salah satu format JSON berikut **dengan tepat**:
- {"action": "cmd", "command": "dir C:\\\\Users"}
- {"action": "click", "x": 123, "y": 456}
- {"action": "type", "text": "Halo dunia"}
- {"action": "press", "key": "enter"}
- {"status": "selesai"}

⚠️ Penting: **Selalu gunakan key 'action'. Jangan hilangkan key 'action'.** Jawaban harus JSON valid satu baris, tanpa tambahan apapun.
"""

running = False  # kontrol proses

def setup_folder():
    if os.path.exists("screenshots"):
        shutil.rmtree("screenshots")
    os.makedirs("screenshots")

def ambil_screenshot(nomor):
    screenshot = pyautogui.screenshot()
    path = f"screenshots/step_{nomor}.png"
    screenshot.save(path)
    with open("screenshots/latest.txt", "w") as f:
        f.write(path)
    return path

def encode_screenshot(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")

def kirim_ke_gemini(img_base64, tujuan, izinkan_cmd):
    action_cmd = '- {"action": "cmd", "command": "dir C:\\\\Users"}' if izinkan_cmd else ''
    prompt = PROMPT_TEMPLATE.replace("[TUJUAN_SAYA]", tujuan).replace("[ACTION_CMD]", action_cmd)

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt},
                    {
                        "inlineData": {
                            "mimeType": "image/png",
                            "data": img_base64
                        }
                    }
                ]
            }
        ]
    }

    response = requests.post(GEMINI_ENDPOINT, headers={"Content-Type": "application/json"}, json=data)
    try:
        text = response.json()['candidates'][0]['content']['parts'][0]['text']
        print("[RESPON GEMINI]:", text)   # Debug print
        return text
    except Exception as e:
        print("Error Gemini response:", e)
        return ""

def eksekusi_aksi(respon_text):
    try:
        data = json.loads(respon_text)
        with open("screenshots/log.txt", "a", encoding="utf-8") as f:
            f.write(respon_text + "\n")

        if data.get("status") == "selesai":
            return "selesai"

        action = data.get("action")
        if action == "click":
            pyautogui.click(data["x"], data["y"])
        elif action == "type":
            pyautogui.write(data["text"], interval=0.05)
        elif action == "press":
            pyautogui.press(data["key"])
        elif action == "cmd":
            cmd = data["command"]
            hasil = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            with open("screenshots/cmd_output.txt", "a", encoding="utf-8") as f:
                f.write(f"\n> {cmd}\n{hasil.stdout}\n")
        return "lanjut"
    except Exception as e:
        print("Error eksekusi:", e)
        return "gagal"

def buat_zip():
    with ZipFile("hasil.zip", "w") as zipf:
        for fname in os.listdir("screenshots"):
            zipf.write(os.path.join("screenshots", fname), arcname=fname)

def jalankan_jarvis(tujuan, izinkan_cmd):
    global running
    setup_folder()
    running = True
    i = 1
    while running:
        path = ambil_screenshot(i)
        img64 = encode_screenshot(path)
        respon = kirim_ke_gemini(img64, tujuan, izinkan_cmd)
        hasil = eksekusi_aksi(respon)
        if hasil == "selesai":
            break
        elif hasil == "gagal":
            break
        time.sleep(2)
        i += 1

    buat_zip()
    pyautogui.alert("Jarvis telah selesai menjalankan tugas.")
    running = False

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tujuan = request.form.get("tujuan")
        izinkan_cmd = True if request.form.get("cmd_allowed") == "on" else False
        Thread(target=jalankan_jarvis, args=(tujuan, izinkan_cmd)).start()
        return redirect(url_for("monitor"))
    return '''
        <form method="post">
            <h2>Masukkan Tujuan AI Jarvis</h2>
            <input name="tujuan" size="80" placeholder="Contoh: Buka Notepad dan ketik Halo Dunia"><br><br>
            <input type="checkbox" name="cmd_allowed"> Izinkan AI menjalankan Command Prompt (CMD)<br><br>
            <input type="submit" value="Mulai Jalankan">
        </form>
    '''

@app.route("/monitor")
def monitor():
    screenshot = "screenshots/step_1.png"
    if os.path.exists("screenshots/latest.txt"):
        with open("screenshots/latest.txt") as f:
            screenshot = f.read().strip()

    log = ""
    if os.path.exists("screenshots/log.txt"):
        with open("screenshots/log.txt", encoding="utf-8") as f:
            log = f.read()

    cmd_out = ""
    if os.path.exists("screenshots/cmd_output.txt"):
        with open("screenshots/cmd_output.txt", encoding="utf-8") as f:
            cmd_out = f.read()

    return f'''
        <h2>Monitor Jarvis</h2>
        <img src="/{screenshot}" width="600"><br><br>
        <a href="/stop">Stop Jarvis</a> | <a href="/download">Download Hasil (ZIP)</a><br><br>

        <h3>Log Aksi:</h3>
        <pre>{log}</pre>

        <h3>Output CMD:</h3>
        <pre>{cmd_out}</pre>
    '''

@app.route("/stop")
def stop():
    global running
    running = False
    return redirect(url_for("monitor"))

@app.route("/download")
def download():
    return send_file("hasil.zip", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
