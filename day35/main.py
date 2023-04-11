import requests as req
import config as c
from dotenv import load_dotenv
import os

load_dotenv()

params = {
    "lat": c.LAT,
    "lon": c.LNG,
    "appid": os.environ.get("WHETHER_API_KEY"),
    "units": "metric",
}

# res = req.get(url=c.WHETHER_API_URL, params=params)
# res.raise_for_status()
# data = res.json()
# print(data)

f_params = {
    "lat": c.LAT,
    "lon": c.LNG,
    "appid": os.environ.get("WHETHER_API_KEY"),
}

forcast_res = req.get(url=c.FORECAST_API_URL, params=f_params)
forcast_res.raise_for_status()
forecast_data = forcast_res.json()
forecast_data_list = forecast_data["list"]
rain = any(data["weather"][0]["id"] <= 700 for data in forecast_data_list[:11])

if rain:
    print(
        "Looks like the rain is coming to town. Time to grab your umbrella and your rubber ducky and make a splash!"
    )
