import asyncio

import requests as req
import config as c
from dotenv import load_dotenv
import os
from day36.tel import send_msg_t

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
print(forcast_res.url)
forcast_res.raise_for_status()
forecast_data = forcast_res.json()
forecast_data_list = forecast_data["list"]
rain = any(data["weather"][0]["id"] <= 700 for data in forecast_data_list[:11])


# if rain:
#     print(
#         "Looks like the rain is coming to town. Time to grab your umbrella and your rubber ducky and make a splash!"
#     )
formatted_string = (
    f"🌡️ Temperature: {forecast_data_list[0]['main']['temp']}°K\n"
    f"☁️ Weather: {forecast_data_list[0]['weather'][0]['main']}\n"
    f"🔍 Description: {forecast_data_list[0]['weather'][0]['description']}\n"
    f"💨 Wind Speed: {forecast_data_list[0]['wind']['speed']} m/s"
    f"\n\nLife is like the weather, sometimes it's sunny and other times it pours. Don't "
    f"let "
    f"`the rain bring you down, use it as an opportunity to grow and nurture yourself. Remember that after the rain, comes the rainbow. Stay safe and enjoy the beauty of the storm. 🌧️🌈☔️`"
)

asyncio.run(send_msg_t([formatted_string]))
