import asyncio
from telegram import *
from dotenv import load_dotenv
import os

load_dotenv()

app = Bot(token=os.environ.get("tel_bot_api_key"))
chat_id = os.environ.get("tel_chat_id")
thread_id = 9960


async def msg_t(msg: str):
    try:
        await app.send_message(chat_id=chat_id, text=msg, message_thread_id=thread_id)
    except:
        await app.send_message(
            chat_id=chat_id, text="no data found 🙀", message_thread_id=thread_id
        )


async def send_msg_t(msg: list):
    for i in range(len(msg)):
        await msg_t(msg[i])
        await asyncio.sleep(2)
