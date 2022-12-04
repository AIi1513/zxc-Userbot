from pyrogram import Client, filters
from pyrogram.types import Message
import random
import datetime

from utils.misc import modules_help, prefix, userbot_version, python_version


@Client.on_message(filters.command(["support", "repo"], prefix) & filters.me)
async def support(_, message: Message):
    devs = ["@deadboizxc"]
    random.shuffle(devs)

    commands_count = 0.0
    for module in modules_help:
        for cmd in module:
            commands_count += 1

    await message.edit(
        f"<b>zxc-Userbot\n\n"
        "GitHub: <a href=https://github.com/deadboi-zxc/zxc-Userbot>deadboizxc/zxc-Userbot</a>\n"
        "Custom modules repository: <a href=https://github.com/deadboi-zxc/custom_modules>"
        f"Main developers: {', '.join(devs)}\n\n"
        f"Python version: {python_version}\n"
        f"Modules count: {len(modules_help) / 1}\n"
        f"Commands count: {commands_count}</b>",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command(["version", "ver"], prefix) & filters.me)
async def version(client: Client, message: Message):
    await message.edit(f"{userbot_version}")

modules_help["support"] = {
    "support": "Information about userbot",
    "version": "Check userbot version",
}
