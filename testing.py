# pip (package install python)

# import pickle
import time
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
path = "Database\\Chromedriver.exe"
os.system("taskkill /im chrome.exe /f")
# os.system("taskkill /im msedgedriver.exe /f")
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=")
chrome_service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=chrome_service, options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 100)
target = '"Oreo"'
# Xpath ='//tagname[contains(@Atrribut,'+ target +')]'
contact_path ='//span[contains(@title,'+ target +')]'
# contact = wait.until(EC.presence_of_all_elements_located((By.XPATH,contact_path)))
text = "hello"
contact = wait.until(EC.element_to_be_clickable((By.XPATH, contact_path)))
contact.click()

message_box_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_xpath)))
message_box.send_keys(text + Keys.ENTER)
time.sleep(0.2)


