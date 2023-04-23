import requests as req
from bs4 import BeautifulSoup
import asyncio
import lxml
from selenium import webdriver

low_price = 500.00

url = "https://www.amazon.com/SAMSUNG-Odyssey-Computer-FreeSync-LS28AG700NNXZA/dp/B096YPN52D/ref=sr_1_4?crid=259Q6UK9UMRQU&keywords=led%2Bmonitor&qid=1682227284&refinements=p_36%3A1253507011&rnid=386442011&s=electronics&sprefix=led%2Bm%2Caps%2C1930&sr=1-4&th=1"


async def amazon(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    }
    response = req.get(url=url, headers=header)
    response.raise_for_status()
    return response


res = asyncio.run(amazon(url))
# driver = webdriver.Chrome()
# driver.get(url)
# driver.quit()
soup = BeautifulSoup(res.text, "lxml")
title = soup.find(id="productTitle").text.strip()
priceA = soup.select(selector=".a-price .a-offscreen")[:1]
price = float(priceA[0].text[1:])
if price > low_price:
    print(f"yehh Price dropped for {title} by ${round(price - low_price)}")
