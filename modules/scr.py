import asyncio

from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from utils.misc import modules_help, prefix


@Client.on_message(
    filters.command(["scr", "screenshot"], prefix) & filters.private & filters.me
)
async def screenshot(client: Client, message: Message):
    amount = int(message.command[1]) if len(message.command) > 1 else 1
    await message.delete()
    for _ in range(amount):
        await client.send(
            functions.messages.SendScreenshotNotification(
                peer=await client.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=client.rnd_id(),
            )
        )
        await asyncio.sleep(0.1)


modules_help["scr"] = {
    "scr [amount]": 'Send "You took a screenshot" message. Works only in PM'
}
