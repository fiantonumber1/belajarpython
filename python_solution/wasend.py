from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import schedule

# Nomor telepon penerima dengan format internasional
nomor_telepon = "+6281515814752"

# Pesan yang akan dikirim
pesan = "Halo, ini adalah pesan otomatis yang dikirim menggunakan Selenium setiap 3 menit!"

# Path ke driver browser, sesuaikan dengan browser yang digunakan
driver_path = 'C:\\Users\\fiansyah\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe'

def kirim_pesan():
    try:
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
        driver.get(f"https://web.whatsapp.com/send?phone={nomor_telepon}&text={pesan}")
        time.sleep(15)  # Tunggu sampai QR code discan dan halaman terbuka

        # Klik tombol kirim
        send_button = driver.find_element(By.XPATH, "//span[@data-icon='send']")
        send_button.click()
        print(f"Pesan berhasil dikirim ke {nomor_telepon}")

        time.sleep(5)  # Tunggu beberapa saat sebelum menutup browser
        driver.quit()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Menjadwalkan pesan untuk dikirim setiap 1 menit
schedule.every(1).minutes.do(kirim_pesan)

# Menjalankan penjadwalan
while True:
    schedule.run_pending()
    time.sleep(1)
