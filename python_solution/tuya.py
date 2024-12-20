import requests
import time
import hashlib
import hmac
import uuid

# Konfigurasi Tuya
TUYA_CLIENT_ID = "ks5wexwahr5ptxj3uddt"
TUYA_SECRET = "2cc16e6ff204428aba4b5d19382337cf"
TUYA_API_ENDPOINT = "https://openapi.tuyaus.com"
DEVICE_ID = 'eb3eb431497845d47cfaxo'


def calc_sha256(content):
    """Menghitung SHA256 dari konten (body request)"""
    if not content:  # Jika body kosong
        return "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def calc_sign(client_id, secret, t, nonce, string_to_sign, access_token ):
    """Menghitung tanda tangan HMAC-SHA256"""
    str_to_sign = client_id + access_token + t + nonce + string_to_sign
    signature = hmac.new(secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256)
    return signature.hexdigest().upper()


def get_tuya_token():
    """Mendapatkan akses token Tuya."""
    t = str(int(time.time() * 1000))  # Timestamp dalam milidetik
    nonce = str(uuid.uuid4())  # UUID sebagai nonce
    method = "GET"
    body = ""
    content_sha256 = calc_sha256(body)
    
    url_path = "/v1.0/token?grant_type=1"
    string_to_sign = f"{method}\n{content_sha256}\n\n{url_path}"
    sign = calc_sign(TUYA_CLIENT_ID, TUYA_SECRET, t, nonce, string_to_sign,"")
    
    headers = {
        "client_id": TUYA_CLIENT_ID,
        "sign": sign,
        "t": t,
        "sign_method": "HMAC-SHA256",
        "nonce": nonce
    }
    
    response = requests.get(TUYA_API_ENDPOINT + url_path, headers=headers)
    response_data = response.json()
    if response_data.get("success"):
        return response_data["result"]["access_token"]
    else:
        raise Exception(f"Error mendapatkan token: {response_data.get('msg')}")


def get_device_status(access_token, device_id):
    """Fungsi untuk mendapatkan detail perangkat Tuya"""
    t = str(int(time.time() * 1000))  # Timestamp saat ini dalam milidetik
    nonce = str(uuid.uuid4())  # UUID sebagai nonce unik
    method = "GET"
    body = ""  # Body kosong untuk permintaan GET
    content_sha256 = calc_sha256(body)  # Kalkulasi SHA256 body request
    
    # Path URL yang benar (tanpa host)
    url_path = f"/v1.0/devices/{device_id}"
    string_to_sign = f"{method}\n{content_sha256}\n\n{url_path}"
    
    # Kalkulasi tanda tangan
    sign = calc_sign(TUYA_CLIENT_ID, TUYA_SECRET, t, nonce, string_to_sign, access_token )
    
    # Header request
    headers = {
        "client_id": TUYA_CLIENT_ID,
        "sign": sign,
        "t": t,
        "sign_method": "HMAC-SHA256",
        "nonce": nonce,
        "access_token": access_token
    }
    
    # Permintaan detail perangkat
    url = TUYA_API_ENDPOINT + url_path  # Endpoint lengkap
    response = requests.get(url, headers=headers)
    
    # Debug jika ada kesalahan
    if response.status_code != 200:
        print("Error:", response.text)
    return response.json()



# Eksekusi Skrip
try:
    # Ambil token hanya satu kali
    access_token = get_tuya_token()
    print("Access Token:", access_token)

    # Ambil detail perangkat
    device_details = get_device_status(access_token, DEVICE_ID)
    if device_details.get("success"):
        print("Device Details:")
        print(device_details["result"])
    else:
        print("Gagal mendapatkan detail perangkat:", device_details.get("msg"))
except Exception as e:
    print("Error:", str(e))
