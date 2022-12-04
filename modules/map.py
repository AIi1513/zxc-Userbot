from pyrogram import *
from pyrogram.types import Message
from utils.misc import modules_help, prefix
import asyncio
import os
import requests
import json
import jmespath

@Client.on_message(filters.command('map', prefixes=prefix) & filters.me)
async def sample(client, message):
    url2 = "https://api.alerts.in.ua/v1/alerts/active.json"
    res = requests.get(url2)
    alerts = res.json()
    text  = ""
    for loc in alerts["alerts"]:
        text += "\n"
        text += "🔴: "+loc["location_title"]
    await message.edit_text(
f"""
**‼Повітряна тривога в таких місцях:**
**{text}**

""")

modules_help["map"] = {
    "map": "send an air alert map",
}
