from pyrogram import *
from pyrogram.types import Message
from utils.misc import modules_help, prefix
import asyncio
import qrcode
import time
import os



@Client.on_message(filters.command('qrgen', prefixes=prefix) & filters.me)
async def sample(client, message):
    await message.delete()
    data = message.text.split(maxsplit=1)[1]
    img = qrcode.make(data)
    img.save("qr.png")
    time.sleep(2)
    await client.send_photo(chat_id=message.chat.id, photo="qr.png")
    os.remove("qr.png")


modules_help["qr"] = {
    "qrgen": ".qrgen [text to qr-code] generate qr-code",
}
