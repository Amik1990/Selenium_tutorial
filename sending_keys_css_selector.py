import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import array

os.environ["PATH"] += r"D:\python_projects\Selenium_tutorial"
driver = webdriver.Chrome()

driver.get("https://www.penize.cz/kalkulacky/vypocet-ciste-mzdy")
driver.implicitly_wait(5)

# try:
    #no_button = driver.find_element(By.ID, "")
   #no_button.click()
# except:
    #print("No element with this class name. Skipping")

hruba_mzda = driver.find_element(By.ID, "Mzda")
deti = driver.find_element(By.ID, "PocetDeti")

hruba_mzda.send_keys(4, 0, 0, 0, 0)
deti.send_keys(1)

btn = driver.find_element((By.ID, "btncalculate"))
btn.click()

# try:
    #no_button = driver.find_element(By.ID, "")
   #no_button.click()
# except:
    #print("No element with this class name. Skipping")


