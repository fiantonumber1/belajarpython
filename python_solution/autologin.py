from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path to Chrome executable
chrome_executable_path = r'C:\Users\USER\AppData\Local\Google\Chrome\Application\chrome.exe'
user_data = r'user-data-dir=C://Users//USER//AppData//Local//Google//Chrome//User Data'
profile_directory = 'profile-directory=Profile 1'

# Configure options for WebDriver
options = webdriver.ChromeOptions()
options.binary_location = chrome_executable_path
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')
options.add_argument(user_data)
options.add_argument(profile_directory)
options.add_argument('--test-type')
options.add_experimental_option("excludeSwitches", ['enable-automation'])

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Open the login page
    driver.get("https://internet.inka.co.id/login")

    # Wait for the page to load
    time.sleep(3)

    # Input username
    username_input = driver.find_element(By.XPATH, '/html/body/div/div/div/form/div[1]/input')
    username_input.send_keys('rudy.indrawan')

    # Input password
    password_input = driver.find_element(By.XPATH, '/html/body/div/div/div/form/div[2]/input')
    password_input.send_keys('Rahasiaq24')

    # Click the submit button
    submit_button = driver.find_element(By.XPATH, '/html/body/div/div/div/form/button')
    submit_button.click()

    # Optional: wait for a while to see the result
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
