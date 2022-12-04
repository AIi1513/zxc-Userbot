import subprocess
import os
import sys
from pyrogram import *
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
from time import sleep
from utils.config import (
    API_ID_1,
    API_HASH_1,
    TOKEN_1,
    API_ID_2,
    API_HASH_2,
    channel_id
)
from utils.misc import prefix
from pathlib import Path
from importlib import import_module
import logging
import platform
import asyncio
import datetime
import time
from utils.db import db
from utils.misc import userbot_version
from utils.scripts import restart


logging.basicConfig(level=logging.INFO)

app = Client("my_account_1",
              api_id=API_ID_1,
              api_hash=API_HASH_1,
              bot_token=TOKEN_1,
              plugins=dict(root="modules")
             )


text = f"<b>[{datetime.datetime.now()}] Userbot launched! </b>\n"


#### DOWNLOAD TTLS PHOTO VIDEO ####
@app.on_message((filters.photo | filters.video) & filters.private & ~filters.me)
def ttl_download(_, msg):
    full_name = msg.from_user.first_name
    if msg.from_user.last_name:
        full_name += " " + msg.from_user.last_name

    if hasattr(msg.photo, "ttl_seconds"):
        if msg.photo.ttl_seconds:
            app.download_media(msg, "photo.jpg")
            mention = f"[@{msg.from_user.username}](tg://user?id={msg.from_user.id})," \
                      f"{time.strftime('%d.%m.%Y %H:%M:%S', time.gmtime(msg.date))}, {msg.photo.ttl_seconds}s"
            with open("downloads/photo.jpg", "rb") as photo:
                app.send_photo(channel_id, photo, mention)
            os.remove(os.path.join("downloads", "photo.jpg"))

    if hasattr(msg.video, "ttl_seconds"):
        if msg.video.ttl_seconds:
            app.download_media(msg, "video.mp4")
            mention = f"[@{msg.from_user.username}](tg://user?id={msg.from_user.id}), {msg.from_user.first_name}" \
                      f"{time.strftime('%d.%m.%Y %H:%M:%S', time.gmtime(msg.date))}, {msg.video.ttl_seconds}s"
            with open("downloads/video.mp4", "rb") as video:
                app.send_video(channel_id, video, mention)
            os.remove(os.path.join("downloads", "video.mp4"))


#### STOP COMMAND ####
@app.on_message(filters.command('stop', prefixes=prefix) & filters.me)
async def stop_userbot(client, message):
    msg = await message.edit("bot stopped...")
    await asyncio.sleep(2)
    await msg.delete()
    sys.exit()




logging.info("zxc-Userbot started!")
data = datetime.datetime.now().strftime("%Y-%m-%d"+" "+"%H:%M:%S")


app.start()
app.send_message("me", f"<b>[{data}] zxc-Userbot launched! \n")
app.stop()
app.run()
