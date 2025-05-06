from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path ke WebDriver dan executable Chrome
driver_path = "C:/Users/fiansyah/Downloads/win64/chrome-win64/chrome.exe"
chrome_executable_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"

# Konfigurasi Chrome Options
options = webdriver.ChromeOptions()
options.binary_location = chrome_executable_path
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36")
options.add_argument("--test-type")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Inisialisasi Service dan Driver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# URL situs lelang
url = "https://www.lelang.go.id"  # Ganti dengan URL yang sesuai

# Buka halaman lelang dengan handling error
try:
    driver.get(url)
    print("Berhasil membuka halaman:", url)
except Exception as e:
    print(f"Error membuka halaman: {e}")
    driver.quit()
    exit()

# Tunggu hingga elemen lot lelang tersedia
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='lot-lelang']"))
    )
except Exception as e:
    print("Gagal menemukan elemen lot lelang:", e)
    driver.quit()
    exit()

# Ambil data lelang
lelang_items = driver.find_elements(By.CSS_SELECTOR, "div[class*='lot-lelang']")  # Sesuaikan selector

# Simpan hasil scraping
results = []

for item in lelang_items:
    try:
        title = item.find_element(By.CSS_SELECTOR, "h3").text.strip()  # Judul lelang
        limit_value = item.find_element(By.CSS_SELECTOR, ".nilai-limit").text.strip()  # Nilai Limit
        deposit = item.find_element(By.CSS_SELECTOR, ".uang-jaminan").text.strip()  # Uang Jaminan
        location = item.find_element(By.CSS_SELECTOR, ".lokasi").text.strip()  # Lokasi
        
        results.append({
            "Judul": title,
            "Nilai Limit": limit_value,
            "Uang Jaminan": deposit,
            "Lokasi": location
        })
    except Exception as e:
        print(f"Error saat mengambil data: {e}")

# Tampilkan hasil scraping
if results:
    print("\n=== Hasil Scraping ===")
    for r in results:
        print(r)
else:
    print("Tidak ada data lelang yang ditemukan.")

# Tutup browser
driver.quit()
