import requests as req

import config as c

params = {
    "amount": 40,
    "type": "boolean",
}

res = req.get(url=c.API_URL, params=params)
res.raise_for_status()
results = res.json()

question_data = results["results"]
