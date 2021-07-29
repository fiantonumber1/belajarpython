from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "D:\chromedriver.exe"
driver = webdriver.Chrome(PATH)

website = driver.get("https://ilmucerdik.com/")

yangdicari= "pos terbaru"
link = driver.find_element_by_link_text(yangdicari.upper())
link.click()

driver.quit()