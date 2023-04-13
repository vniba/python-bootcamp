import asyncio
import pandas as pd
from dotenv import load_dotenv
import os
import requests as req
from config import EXERCISE_URL
from datetime import datetime

load_dotenv()

domo = {
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30,
}


header = {
    "x-app-id": os.environ.get("NUT_APP_ID"),
    "x-app-key": os.environ.get("NUT_API_KEY"),
    "Content-Type": "application/json",
}


async def nut(query, head=header):
    body = {"query": query}
    res = req.post(url=EXERCISE_URL, headers=header, json=body)
    res.raise_for_status()
    return res.json()


q = input(
    "Please enter the type of exercise, duration, track your progress and achieve your "
    "fitness goals. \n"
)

data = ""
if len(q) < 4:
    exit()
else:
    data = asyncio.run(nut(q))

# print(data)
date = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%H:%M:%S")

exercise = data["exercises"]
user_data = []
for i in range(len(exercise)):
    user_data.append(
        {
            "Date": date,
            "Time": now,
            "Exercise": exercise[i]["user_input"],
            "duration": exercise[i]["duration_min"],
            "Calories": round(exercise[i]["nf_calories"]),
        }
    )

if len(user_data) == 0:
    exit()
else:
    out = pd.DataFrame(user_data)
    out.to_csv(path_or_buf="exercise.csv", index=False, header=False, mode="a")
