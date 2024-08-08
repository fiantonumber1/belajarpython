import requests

# URL endpoint API
url = "https://yuksyari.in/api/wamessages"

# Mengirim permintaan GET ke API
response = requests.get(url)

# Memeriksa respons dari server
if response.status_code == 200:
    print("Data berhasil diambil:", response.json())
else:
    print("Gagal mengambil data:", response.status_code, response.text)
