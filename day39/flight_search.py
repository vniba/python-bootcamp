import pandas as pd
import requests as req
from datetime import datetime as d
from dateutil.relativedelta import relativedelta
import config as c


class FlightSearch:
    def __init__(self, apikey):
        self.__header = {"accept": "application/json", "apiKey": apikey}
        self.__today = d.today().strftime("%d/%m/%Y")
        self.__to = (d.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")

    async def search(self, dic):
        body = {
            "fly_from": c.HOME,
            "fly_to": "",
            "dateFrom": self.__today,
            "dateTo": self.__to,
        }
        for item, val in dic.items():
            if item == "IATA Code":
                body["fly_to"] = val[0]
        res = req.get(c.K_URL, headers=self.__header, params=body)
        res.raise_for_status()
        return res.json()
