from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = "C:/Program Files/chrome driver/chromedriver.exe"
url = "https://www.python.org/"
service = Service(driver_path)

driver = webdriver.Chrome(service=service)
driver.get(url=url)

event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu time")
event_text = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")
schedule = {}
for i in range(len(event_time)):
    schedule[i] = {"name": event_text[i].text, "time": event_time[i].text}
print(schedule)

driver.quit()
