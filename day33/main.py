import datetime

import requests as req

LAT = -82.862755
LNG = 135.000000
# res = req.get(url="http://api.open-notify.org/iss-now.json")
# res.raise_for_status()
# data = res.json()
# (latitude, longitude) = (
#     data["iss_position"]["latitude"],
#     data["iss_position"]["longitude"],
# )
# print(latitude, longitude)
# cords = tuple(data["iss_position"].values())
# print(cords)

"""  "results": {
    "sunrise": "5:56:56 AM",
    "sunset": "6:05:49 PM",
    "solar_noon": "12:01:22 PM",
    "day_length": "12:08:53",
    "civil_twilight_begin": "5:37:08 AM",
    "civil_twilight_end": "6:25:36 PM",
    "nautical_twilight_begin": "5:12:54 AM",
    "nautical_twilight_end": "6:49:51 PM",
    "astronomical_twilight_begin": "4:48:39 AM",
    "astronomical_twilight_end": "7:14:06 PM"
  },
  "status": "OK"
}"""


param = {"lat": LAT, "log": LNG, "formatted": 0}

res = req.get(url="https://api.sunrise-sunset.org/json", params=param)
res.raise_for_status()
data = res.json()
sunrise, sunset = data["results"]["sunrise"], data["results"]["sunset"]

sunrise_hour = datetime.datetime.fromisoformat(sunrise).strftime("%H")
sunset_hour = datetime.datetime.fromisoformat(sunset).strftime("%H")

print(sunrise_hour, sunset_hour)
