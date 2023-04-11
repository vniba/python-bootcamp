from dotenv import load_dotenv
import os
import config as c
import requests as req
import datetime as d
from tel import send_msg_t
import asyncio


load_dotenv()
stock_params = {
    "function": "TIME_SERIES_WEEKLY",
    "symbol": c.STOCK,
    "sortBy": "popularity",
    "apikey": os.environ.get("alpha_api_key"),
}


async def stock():
    stock_res = req.get(url=c.STOCK_API_URL, params=stock_params)
    stock_res.raise_for_status()
    stock_data = stock_res.json()
    stock_weekly = stock_data["Weekly Time Series"]
    return list(stock_weekly.items())[:2]


stock_list = asyncio.run(stock())
closing_price_y = stock_list[0][1]["1. open"]
closing_price_d_y = stock_list[1][1]["4. close"]


stock_diff = round(
    abs(
        (float(closing_price_d_y) - float(closing_price_y))
        / float(closing_price_y)
        * 100
    )
)
send_news = False
if stock_diff > c.STOCK_DIFF:
    send_news = True
else:
    send_news = False


high_low = "🔻" if float(closing_price_y) < float(closing_price_d_y) else "🔺"

days_from = (d.datetime.today() - d.timedelta(days=2)).isoformat()

news_params = {
    "q": c.COMPANY_NAME,
    "sortBy": "popularity",
    "from": days_from,
    "apiKey": os.environ.get("news_api_key"),
}


async def news():
    news_res = req.get(url=c.NEWS_API_URL, params=news_params)
    news_res.raise_for_status()
    news_data = news_res.json()
    return news_data["articles"][:3]


news_articles = asyncio.run(news())

formatted_news_a = [
    f"TSLA: {high_low} {stock_diff}%\n\n📰 {article_data['title']}\n\n🗞 "
    f"{article_data['source']['name']}\n\n📅 "
    f"{article_data['publishedAt']}\n\n"
    f"{article_data['description']}\n\nRead more: "
    f"{article_data['url']}"
    for article_data in news_articles
]


replay = asyncio.run(send_msg_t(formatted_news_a))
