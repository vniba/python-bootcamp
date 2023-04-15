from selenium import webdriver
from bs4 import BeautifulSoup
import lxml

url = "https://www.empireonline.com/movies/features/best-movies-2/"
driver = webdriver.Chrome()
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, "lxml")
movies_div = soup.select(selector=".listicle-item h3")
h3 = []
for items in movies_div:
    h3.append(items.getText())

if len(h3) != 0:
    h3.reverse()
    with open("movies.txt", "w") as f:
        for item in h3:
            f.write("%s\n" % item)

driver.quit()
