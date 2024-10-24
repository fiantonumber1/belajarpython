import requests
import json

# URL Google Apps Script yang baru
google_script_url = 'https://script.google.com/macros/s/AKfycbybSW9SzZLaLMqnhYw7qZjj23GRVaxWTWC5yw4328OVo07s7v_Rf_zVn55PScglOdaQ-g/exec'

# Nama-nama sheet yang ingin diambil datanya
sheet_names = ["Sistem Mekanik"]  # Gantilah dengan nama sheet yang sesuai

# Mengirim POST request
response = requests.post(google_script_url, data=json.dumps(sheet_names))

# Memeriksa status response
if response.status_code == 200:
    # Parsing response JSON
    data = response.json()
    print("Data retrieved successfully:")

    # Menggunakan for loop untuk menampilkan data
    for sheet_name, sheet_data in data.items():
        print(f"\nData from sheet: {sheet_name}")
        for row in sheet_data:
            print(row)

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print("Response:", response.text)
