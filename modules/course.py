import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from utils.scripts import format_exc, import_library
from utils.misc import modules_help, prefix

bs4 = import_library("bs4", "beautifulsoup4")
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}


@Client.on_message(filters.command("course", prefix) & filters.me)
async def convert(_, message: Message):
    if len(message.command) == 1:
        await message.edit("<b>Enter currency name</b>")
        return

    name = message.command[1]
    await message.edit("<b>Data retrieval...</b>")

    try:
        if name == "btc":
            name = "1₿"
            link = "https://ru.investing.com/crypto/bitcoin"
        else:
            link = f"https://ru.investing.com/currencies/{name}-rub"

        full_page = requests.get(link, headers=headers, timeout=3)
        soup = BeautifulSoup(full_page.content, "html.parser")
        rub = soup.find("span", class_="text-2xl")
        await message.edit(f"<b>{name} now is </b><code> {rub} </code><b> rub</b>")
    except Exception as e:
        await message.edit(format_exc(e))


modules_help["course"] = {
    "course [currency]*": "Transfer from any state currency to the ruble. Don't use more than 10 times per minute"
}
