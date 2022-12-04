import os
import asyncio
from asyncio import sleep
from pyrogram import *
from pyrogram.types import Message
from utils.misc import modules_help, prefix


#{message.reply_to_message.id}
#{message.reply_to_message.from_user.id}
#{reply_to_message_id=message.reply_to_message.id}



@Client.on_message(filters.command('l2t', prefixes=prefix) & filters.me)
async def link2text(client, message):
    data = " ".join(message.command[1:])
    chat = await client.get_chat(chat_id=message.chat.id)
#   data = message.text.split(maxsplit=1)[1]
#    if message.reply_to_message:
#        await message.edit_text(f"[{data}](tg://user?id={message.reply_to_message.from_user.id})")

#    elif message.reply_to_message.photo:
#        await message.edit_text(f"[{data}](tg://user?id={message.reply_to_message.from_user.id})")

#    elif message.reply_to_message.sticker:
#        await message.edit_text(f"[{data}](tg://user?id={message.reply_to_message.from_user.id})")

#    elif message.reply_to_message.audio:
#        await message.edit_text(f"[{data}](tg://user?id={message.reply_to_message.from_user.id})")

#   elif message.reply_to_message.video:
#        await message.edit_text(f"[{data}](tg://user?id={message.reply_to_message.from_user.id})")

#    else:
#        pass

    if message.reply_to_message:
        await message.delete()
        await client.send_message(chat_id=chat.id, text=f"[{data}](tg://user?id={message.reply_to_message.from_user.id})")

    elif message.reply_to_message.photo:
        await message.delete()
        await client.send_message(chat_id=chat.id, text=f"[{data}](tg://user?id={message.reply_to_message.from_user.id})")

    elif message.reply_to_message.sticker:
        await message.delete()
        await client.send_message(chat_id=chat.id, text=f"[{data}](tg://user?id={message.reply_to_message.from_user.id})")

    elif message.reply_to_message.audio:
        await message.delete()
        await client.send_message(chat_id=chat.id, text=f"[{data}](tg://user?id={message.reply_to_message.from_user.id})")

    elif message.reply_to_message.video:
        await message.delete()
        await client.send_message(chat_id=chat.id, text=f"[{data}](tg://user?id={message.reply_to_message.from_user.id})")

    else:
        pass





modules_help["mentio_mod"] = {
    "mnt": ".mnt [text]",
}
