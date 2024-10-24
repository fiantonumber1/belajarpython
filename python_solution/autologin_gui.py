import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule
import threading
import requests

# Fungsi untuk memeriksa koneksi internet
def check_internet_connection(url="https://jsonplaceholder.typicode.com/posts"):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

# Fungsi untuk auto login ke internet
def auto_login_internet():
    chrome_executable_path = r'C:\Users\USER\AppData\Local\Google\Chrome\Application\chrome.exe'
    user_data = r'user-data-dir=C://Users//USER//AppData//Local//Google//Chrome//User Data'
    profile_directory = 'profile-directory=Profile 1'

    options = webdriver.ChromeOptions()
    options.binary_location = chrome_executable_path
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')
    options.add_argument(user_data)
    options.add_argument(profile_directory)
    options.add_argument('--test-type')
    options.add_experimental_option("excludeSwitches", ['enable-automation'])

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://internet.inka.co.id/login")
        time.sleep(3)
        username_input = driver.find_element(By.XPATH, '/html/body/div/div/div/form/div[1]/input')
        username_input.send_keys('rudy.indrawan')
        password_input = driver.find_element(By.XPATH, '/html/body/div/div/div/form/div[2]/input')
        password_input.send_keys('Rahasiaq24')
        submit_button = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
        submit_button.click()
        time.sleep(5)
    finally:
        driver.quit()

# Fungsi untuk melakukan login sesuai kondisi
def auto_login():
    if check_internet_connection():
        print("Internet is available. No need to login.")
    else:
        print("No internet connection. Proceeding with login.")
        auto_login_internet()

# Fungsi untuk menjalankan login di thread terpisah
def run_login():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Fungsi untuk memulai countdown
def start_countdown():
    countdown_time = 600  # 10 menit dalam detik
    while True:
        while countdown_time:
            mins, secs = divmod(countdown_time, 60)
            timer_label.config(text=f"{mins:02}:{secs:02}")
            time.sleep(1)
            countdown_time -= 1
        
        # Setelah countdown selesai, lakukan login
        auto_login()  # Panggil fungsi login saat timer selesai
        countdown_time = 600  # Reset countdown ke 10 menit

# Fungsi untuk memulai proses
def start_process():
    schedule.every(10).minutes.do(auto_login)  # Ubah interval ke 10 menit
    threading.Thread(target=start_countdown, daemon=True).start()  # Jalankan countdown di thread terpisah
    threading.Thread(target=run_login, daemon=True).start()  # Jalankan scheduler di thread terpisah

# Buat GUI
root = tk.Tk()
root.title("Auto Login Scheduler")

start_button = tk.Button(root, text="Run Now", command=auto_login)
start_button.pack(pady=10)

timer_label = tk.Label(root, text="10:00", font=("Helvetica", 48))
timer_label.pack(pady=10)

process_button = tk.Button(root, text="Start Process", command=start_process)
process_button.pack(pady=10)

root.mainloop()
