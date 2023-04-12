import asyncio

import requests as req
from dotenv import load_dotenv
import os
from config import *
from datetime import datetime

load_dotenv(dotenv_path="../.env")

user_params = {
    "token": os.environ.get("PIXELA_TOKEN"),
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# pixela_res = req.post(url=PIXELA_URL, json=user_params)
# pixela_res.raise_for_status()
# print(pixela_res)

p_graph_config = {
    "id": "fastest",
    "name": "walking",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": os.environ.get("PIXELA_TOKEN"),
}
# p_graph_res = req.post(url=PIXELA_GRAPH_URL, json=p_graph_config, headers=headers)
# print(p_graph_res.url)
# # p_graph_res.raise_for_status()
# print(p_graph_res.text)
today = datetime.today().strftime("%Y%m%d")
p_pixel_config = {"date": today, "quantity": "100"}

# p_pixel_res = req.post(url=PIXELA_PIXEL_URL, json=p_pixel_config, headers=headers)
# print(p_pixel_res.text)


async def update_pixel(url, json, header):
    p_res = req.post(url=url, json=json, headers=header)
    return p_res


# print(asyncio.run(update_pixel(PIXELA_PIXEL_URL, json=p_pixel_config, header=headers)))
svg_config = {"mode": "short", "appearance": "dark"}

# graph_res = req.get(url=PIXELA_PIXEL_URL, params=svg_config)
# print(graph_res.url)
# data = graph_res.text
# with open("graph.svg", mode="w") as f:
#     f.write(data)


# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

pul_url = f"{PIXELA_PIXEL_URL}/{today}"


async def put_pix(url, header, json):
    res = req.put(url=url, headers=header, json=json)
    return res


# put_pixle = asyncio.run(put_pix(url=pul_url, header=headers, json={"quantity": "100"}))
# print(put_pixle.text)


async def delete_p(url):
    res = req.delete(url=url)
    return res
