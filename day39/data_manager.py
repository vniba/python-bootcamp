import pandas as pd


class DataManager:
    def user_data(self, path):
        data = pd.read_csv(path)
        list_d = data.to_dict(orient="list")
        return list_d

    def flight(self, data):
        objc = [item for item in data["data"][:1]]
        return objc

    def items(self, obj):
        routes = obj[0]["route"][0]
        return {
            "price": obj[0]["price"],
            "flyFrom": routes["flyFrom"],
            "flyTo": routes["flyTo"],
            "cityFrom": routes["cityFrom"],
            "cityTo": routes["cityTo"],
            "utc_departure": routes["utc_departure"],
        }
