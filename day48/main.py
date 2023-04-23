from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:/Program Files/chrome driver/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.vitejs.dev")
# title = driver.find_element(By.ID, "productTitle")
# names = driver.find_element(By.NAME, "q")
# print(title.text)
# a = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
link = driver.find_element(
    By.XPATH, '//*[@id="VPContent"]/div/div[1]/div/div[1]/div/div[1]/a'
)
print(link.text)

driver.quit()
