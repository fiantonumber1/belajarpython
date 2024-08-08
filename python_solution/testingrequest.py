import requests

# URL endpoint API
url = "https://diyloveheart.in/api/wamessages/post"

# Data yang akan dikirim ke API
data = {
    "phone_numbers": ["6288228483739"],  # Array of phone numbers
    "message": "Reminder:Agenda rapat hari ini di Ruang 3.3 pada jam: 13.00",
    'idtoken': '2910219210291',
    'accesstoken': '37237232u32y',
}

# Mengirim permintaan POST ke API
response = requests.post(url, json=data)

# Memeriksa respons dari server
if response.status_code == 201:
    print("Data berhasil disimpan:", response.json())
else:
    print("Gagal menyimpan data:", response.status_code)
    print("Response Headers:", response.headers)
    print("Response Body:", response.text)
