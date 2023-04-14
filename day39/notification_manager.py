import asyncio

from day36.tel import send_msg_t


class NotificationManager:
    def __init__(self, data: dict):
        self.dic = data
        self.string = self.format_not(self.dic)

    def format_not(self, flight_info):
        notf = (
            f"Flight from {flight_info['cityFrom']} 🛫 to {flight_info['cityTo']} 🛬 "
            f"on {flight_info['utc_departure'].replace('T','')[:10]} ⌚ costs"
            f" {flight_info['price']} 💰"
        )
        return notf

    async def send_notification(self, notfication):
        await send_msg_t([notfication])
