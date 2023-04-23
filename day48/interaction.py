from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver_path = "C:/Program Files/chrome driver/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.wikipedia.org/")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()
# species = driver.find_element(By.LINK_TEXT, "Wikispecies")
# species.click()
search = driver.find_element(By.ID, "searchInput")
search.send_keys("blackhole")
search.send_keys(Keys.ENTER)
# search.submit()
