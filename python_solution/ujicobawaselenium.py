import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL endpoint API
url = "https://diyloveheart.in/api/wamessages/get/rahasia_4321"

# Mengirim permintaan GET ke API
response = requests.get(url)

# Memeriksa respons dari server
if response.status_code == 200:
    data_list = response.json()
    print("Data berhasil diambil:", data_list)
    
    # Flag untuk mengetahui apakah ada pesan yang belum dikirim
    found_undelivered = False

    for data in data_list:
        status = data.get('status')
        
        if status != 'delivered':
            nomor_telepon = data['phone_number']
            pesan = data['message']
            idno = data['id']
            
            # Path ke WebDriver dan executable Chrome
            driver_path = 'C://Users//fiansyah//Downloads//chrome07082024//chromedriver-win64//chromedriver.exe'
            chrome_executable_path = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe'
            user_data = 'user-data-dir=C://Users//fiansyah//AppData//Local//Google//Chrome//User Data'
            profile_directory = 'profile-directory=Profile 33'

            url = f'https://web.whatsapp.com/send/?phone={nomor_telepon}&text={pesan}&type=phone_number&app_absent=0'

            options = webdriver.ChromeOptions()
            options.binary_location = chrome_executable_path
            options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36')
            options.add_argument(user_data)
            options.add_argument(profile_directory)
            options.add_argument('--test-type')
            options.add_experimental_option("excludeSwitches", ['enable-automation'])

            driver = webdriver.Chrome(executable_path=driver_path, options=options)
            driver.get(url)
            time.sleep(10)

            try:
                send_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]/ancestor::button'))
                )
                send_button.click()
                print(f"Pesan ke {nomor_telepon} berhasil dikirim.")
                found_undelivered = True
            except Exception as e:
                print(f"Terjadi kesalahan saat mengirim pesan ke {nomor_telepon}: {e}")

            time.sleep(5)
            driver.quit()
            urlsukses = f"https://yuksyari.in/api/wamessages/post/{idno}"
            # Mengirim permintaan GET ke API
            response = requests.get(urlsukses)
    if not found_undelivered:
        print("Semua pesan telah dikirim sebelumnya. Tidak perlu mengirim ulang.")
else:
    print("Gagal mengambil data:", response.status_code, response.text)
