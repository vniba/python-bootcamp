import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("C:/Program Files/chrome driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker")
cookie = ""
time.sleep(10)
try:
    cookie = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )
except Exception as e:
    print("error", e)


while cookie:
    cookie.click()

# driver.quit()
