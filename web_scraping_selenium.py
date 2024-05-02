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
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(3)
my_element = driver.find_element(By.ID, "downloadButton")   # downloadButton najdu v html kodu na strankach jako id.
my_element.click()

progress_element = driver.find_element(By.CLASS_NAME, "progress-label")
print(f"{progress_element.text == 'Completed!'}")

WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "progress-label"), "Complete")
)




