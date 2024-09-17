import requests
import json

# URL dari Google Apps Script Anda
script_url = "https://script.google.com/macros/s/AKfycbyhTYLOimwjPmEauKoFoUIEOE8px4-aB0DfD_-2dIn51jXkQwsirxoPsOOe7EA-gaNUMw/exec"

# Data yang ingin dikirim
data_to_send = [
    {"Sheet": "Teknologi Proses", "nodokumen": "31.2-R35014", "newStatus": "RELEASED", "row": 68, "colStatus": 8},
    # Tambahkan data lain sesuai kebutuhan...
]

# Membuat payload untuk dikirim
payload = {
    "updates": data_to_send
}

# Mengirim request POST
response = requests.post(script_url, json=payload)

# Menampilkan respons
try:
    response.raise_for_status()  # Menaikkan kesalahan jika status kode tidak 200
    print("Response:", response.json())
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # Menampilkan kesalahan HTTP
except json.JSONDecodeError:
    print("JSON decode error. Raw response:", response.text)  # Menampilkan respons mentah jika tidak bisa decode
except Exception as err:
    print(f"Other error occurred: {err}")  # Menampilkan kesalahan lain
