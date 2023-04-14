import asyncio

import pandas as pd

# check csv data
# search for flight
# check for cheapest
# 6months

import requests as req
import config as c
from dotenv import load_dotenv
import os
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

load_dotenv()


flight = FlightSearch(
    apikey=os.environ.get("KIWI_API_KEY"),
)
data = DataManager()
user_data = data.user_data("./Copy of Flight Deals - prices.csv")

res = asyncio.run(flight.search(user_data))
res_obj = data.flight(res)
model_obj = data.items(res_obj)

notification = NotificationManager(model_obj)
result = asyncio.run(notification.send_notification(notification.string))
