import os
import sys
import subprocess
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix, requirements_list
from utils.scripts import format_exc



def restart(restart_type):
    text = "1" if restart_type == "update" else "2"
    os.execvp(
        sys.executable,
        [
            sys.executable,
            "/data/data/com.termux/files/home/ub/main.py",
        ],
    )


@Client.on_message(filters.command("restart", prefix) & filters.me)
async def restart_cmd(_, message: Message):
    await message.edit("<b>Restarting ...</b>")
    await asyncio.sleep(1)
    await message.edit("<b>Wait 15 second ...</b>")
    await asyncio.sleep(1)
    await message.delete()
    restart("restart")

@Client.on_message(filters.command("update", prefix) & filters.me)
async def update(_, message: Message):
    try:
        await message.edit("<b>Updating: 1/4 (updating pip)</b>")
        subprocess.run([sys.executable, "-m", "pip", "install", "-U", "pip"])
        await message.edit("<b>Updating: 2/4 (git pull)</b>")
        subprocess.run(["git", "pull"])
        await message.edit("<b>Updating: 3/4 (updating libs from requirements.txt)</b>")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-U", "-r", "requirements.txt"]
        )
        await message.edit(
            "<b>Updating: 4/4 (updating libs from requirements_list)</b>"
        )
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-U", *requirements_list]
        )
        await message.edit("<b>Updating: done! Restarting...</b>")
    except Exception as e:
        await message.edit(format_exc(e))
    else:
        restart("update")


modules_help["updater"] = {
    "update": "Update the userbot. If new core modules are avaliable, they will be installed",
    "restart": "Restart userbot",
}
