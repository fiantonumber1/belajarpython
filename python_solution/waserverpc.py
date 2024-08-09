import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from urllib.parse import quote

# URL endpoint API
url = "https://diyloveheart.in/api/wamessages/get/rahasia_4321"

# Path to WebDriver and Chrome executable
driver_path = 'C://Users//USER//Downloads//chrome07082024//chromedriver-win64//chromedriver.exe'
chrome_executable_path = 'C://Users//USER//AppData//Local//Google//Chrome//Application//chrome.exe'
user_data = 'user-data-dir=C://Users//USER//AppData//Local//Google//Chrome//User Data//Default'
profile_directory = 'profile-directory=Default'

# Configure options for WebDriver
options = webdriver.ChromeOptions()
options.binary_location = chrome_executable_path
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')
options.add_argument(user_data)
options.add_argument(profile_directory)
options.add_argument('--test-type')
options.add_experimental_option("excludeSwitches", ['enable-automation'])

while True:
    # Send GET request to API
    response = requests.get(url)

    # Check server response
    if response.status_code == 200:
        data_list = response.json()
        print("Data retrieved successfully:", data_list)
        
        found_undelivered = False

        for data in data_list:
            status = data.get('status')
            
            if status != 'delivered':
                phone_number = data['phone_number']
                message = data['message']
                idno = data['id']
                
                # Encode message to handle special characters in URL
                message_encoded = quote(message)
                
                send_url = f'https://web.whatsapp.com/send/?phone={phone_number}&text={message_encoded}&type=phone_number&app_absent=0'

                driver = webdriver.Chrome(executable_path=driver_path, options=options)

                # Set window position and size
                driver.set_window_position(-10000, 0)  # Move window offscreen
                driver.set_window_size(800, 600)  # Set window size (optional)

                driver.get(send_url)
                time.sleep(10)

                try:
                    send_button = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]/ancestor::button'))
                    )
                    send_button.click()
                    print(f"Message to {phone_number} sent successfully.")
                    found_undelivered = True
                except Exception as e:
                    print(f"Error sending message to {phone_number}: {e}")

                time.sleep(5)
                driver.quit()

                # Send GET request to API to update delivery status
                update_url = f"https://yuksyari.in/api/wamessages/post/{idno}"
                response = requests.get(update_url)
                
        if not found_undelivered:
            print("All messages have been previously sent. No need to resend.")
    else:
        print("Failed to retrieve data:", response.status_code, response.text)
    
    # Wait 1 minute before the next check
    print("Waiting 1 minute for the next check...")
    time.sleep(60)
