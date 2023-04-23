import requests as req
from bs4 import BeautifulSoup as bs
import lxml

URL = "https://www.billboard.com/charts/hot-100/"

user_choice = input(
    f"What is your favorite type of music to listen to on custom date " f"yy-mo-dd?"
)
updated_url = f"{URL}/{user_choice}/"
res = req.get(url=updated_url)
res.raise_for_status()
html = res.text

soup = bs(html, "lxml")
lists = soup.select(selector=".o-chart-results-list__item h3")
titles = [item.text.strip() for item in lists]

songs = {"title": titles, "date": user_choice}
