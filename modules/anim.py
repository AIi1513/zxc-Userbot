from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import modules_help, prefix
import async_timeout
import asyncio
import time
import os


@Client.on_message(filters.command('love', prefixes=prefix) & filters.me)
async def hearth_anim(client, message):
    me = await client.get_me()
    ME_USERNAME = f'@{me.username}'

    await asyncio.sleep(1)
    await message.edit_text("🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.05)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)

    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)

    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️‍🩹❤️‍🩹🤍❤️‍🩹❤️‍🩹🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️‍🩹❤️‍🩹🤍❤️‍🩹❤️‍🩹🤍🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️‍🩹❤️‍🩹🤍❤️‍🩹❤️‍🩹🤍🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)

    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️‍🩹❤️‍🩹🤍❤️‍🩹❤️‍🩹🤍🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍🤍\n🤍🤍🤍❤️‍🩹❤️‍🩹❤️‍🩹🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️‍🩹❤️‍🩹🤍❤️‍🩹❤️‍🩹🤍🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍\n🤍🤍❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹🤍🤍\n🤍🤍🤍❤️‍🩹❤️‍🩹❤️‍🩹🤍🤍🤍\n🤍🤍🤍🤍❤️‍🩹🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)





    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🤍🤍💗💗🤍💗💗🤍🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.09)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🤍💗💗💗💗💗💗💗🤍\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🤍💗💗💗💗💗💗💗🤍\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🤍🤍💗💗💗💗💗🤍🤍\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🤍🤍🤍💗💗💗🤍🤍🤍\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🤍🤍🤍🤍💗🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
    await asyncio.sleep(0.1)
    await message.edit_text("🍀🍀🍀🍀🍀🍀🍀🍀🍀\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)

    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🍀🍀💖💖🍀💖💖🍀🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.09)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🍀💖💖💖💖💖💖💖🍀\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🍀💖💖💖💖💖💖💖🍀\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🍀🍀💖💖💖💖💖🍀🍀\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🐼🐼🐼🐼🐼🌴🌴\n🍀🍀🍀💖💖💖🍀🍀🍀\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🐼🐼🐼🐼🐼🌴🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🍀🍀🍀🍀💖🍀🍀🍀🍀\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🐼🐼🐼🐼🐼🌴🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    await asyncio.sleep(0.1)
    await message.edit_text("🌴🌴🌴🌴🌴🌴🌴🌴🌴\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🐼🐼🐼🐼🐼🌴🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)

    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n🌴🌴🐼🐼🌴🐼🐼🌴🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.09)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️💟💟💟💟💟💟💟☁️\n🌴🐼🐼🐼🐼🐼🐼🐼🌴\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️☁️💟💟💟💟💟☁️☁️\n🌴🌴🌴🐼🐼🐼🌴🌴🌴\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️☁️💟💟💟💟💟☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n🌴🌴🌴🌴🐼🌴🌴🌴🌴\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️☁️💟💟💟💟💟☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n🌴🌴🌴🌴🌴🌴🌴🌴🌴")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟☁️💟💟☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️☁️💟💟💟💟💟☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)


    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️☁️💟💟💟💟💟☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️💟💟💟💟💟💟💟☁️\n☁️☁️💟💟💟💟💟☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️💟💟💟💟💟☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️💟💟💟☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️💟☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)

    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️\n☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.1)
    await message.edit_text("☁️☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(1.5)
    await message.edit_text("❤️❤️i☁️☁️☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.3)
    await message.edit_text("❤️❤️i❤️❤️love☁️☁️☁️☁️☁️☁️")
    await asyncio.sleep(0.3)
    await message.edit_text("❤️❤️i❤️❤️love❤️❤️you☁️☁️☁️☁️")
    await asyncio.sleep(0.3)
    await message.edit_text("❤️❤️i❤️❤️love❤️❤️you❤️❤️forever☁️☁️")
    await asyncio.sleep(0.3)
    await message.edit_text("❤️❤️i❤️❤️love❤️❤️you❤️❤️forever❤️❤️")
    await message.reply_text(f"from {ME_USERNAME} ❤️🤭")


modules_help["love"] = {
    "love": "love animation",
}
