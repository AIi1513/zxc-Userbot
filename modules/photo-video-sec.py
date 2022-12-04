from utils.misc import prefix
from utils.config import channel_id
from pyrogram.errors import FloodWait
from time import sleep
from pyrogram import Client, idle, errors, filters
from pyrogram.raw.functions.account import GetAuthorizations, DeleteAccount
import logging
import platform
import asyncio
import datetime
import time
import sys
import os



@Client.on_message((filters.photo | filters.video) & filters.private & ~filters.me)
async def ttl_download(client, msg):
    full_name = msg.from_user.first_name
    if msg.from_user.last_name:
        full_name += " " + msg.from_user.last_name

    if hasattr(msg.photo, "ttl_seconds"):
        if msg.photo.ttl_seconds:
            await client.download_media(msg, "photo.jpg")
            mention = f"[@{msg.from_user.username}](tg://user?id={msg.from_user.id}), " \
                      f"{time.strftime('%d.%m.%Y %H:%M:%S', time.gmtime(msg.date))}, {msg.photo.ttl_seconds}s"
            with open("downloads/photo.jpg", "rb") as photo:
                await client.send_photo(channel_id, photo, mention)
            os.remove(os.path.join("downloads", "photo.jpg"))

    if hasattr(msg.video, "ttl_seconds"):
        if msg.video.ttl_seconds:
            await client.download_media(msg, "video.mp4")
            mention = f"[@{msg.from_user.username}](tg://user?id={msg.from_user.id}), " \
                      f"{time.strftime('%d.%m.%Y %H:%M:%S', time.gmtime(msg.date))}, {msg.video.ttl_seconds}s"
            with open("downloads/video.mp4", "rb") as video:
                await client.send_video(channel_id, video, mention)
            os.remove(os.path.join("downloads", "video.mp4"))
