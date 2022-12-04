<p align="center">
        <img src="https://telegra.ph/file/bd45340691abc5b975704.jpg" width="500" alt="zxc-Userbot">
    </a>
    <br>
    <b>zxc-Userbot</b>
    <br>
    <b>Telegram userbot with the easiest installation</b>
    <br>
    <a href='https://github.com/deadboi-zxc/zxc-Userbot#installation'>
        Installation
    </a>
    •
    <a href="https://github.com/deadboi-zxc/zxc-Userbot/releases">
        Releases
    </a>
    •
    <a href="https://github.com/deadboi-zxc/zxc-Userbot#groups-and-support">
        Community
    </a>
    •
    <a href='https://github.com/deadboi-zxc/zxc-Userbot#custom-modules'>
        Custom modules
    </a>
</p>




<h1>About</h1>
<p>zxc-Userbot is a Telegram userbot (in case you didn't know, selfbot/userbot are used to automate user accounts).
So how does it work? It works in a very simple way, using the pyrogram library, a python script connects to your account (creating a new session) and catches your commands.

Using selfbot/userbot is against Telegram's Terms of Service, and you may get banned for using it if you're not careful.

The developers are not responsible for any consequences you may encounter when using zxc-Userbot. We are also not
responsible for any damage to chat rooms caused by using this userbot.</p>



<h1>Installation</h1>
<h2>Linux, Termux (use <a href='https://f-droid.org/en/packages/com.termux/'>f-droid</a> version) and Windows [only wsl]</h2>

<pre><code>apt-get upgrade -y && apt-get update && apt install git && git clone https://github.com/deadboi-zxc/zxc-Userbot.git && cd zxc-Userbot/ && bash install.sh
</code></pre>



Subsequent launch:

<pre><code>python3 main.py</code></pre>


<h1>Custom modules</h1>


<p>To add your module to the bot, create a pull request in the <a href='https://github.com/deadboi-zxc/custom_modules/'>custom_modules</a> repository</p>
<p>Either send the module and its hash to me (<a href='https://t.me/deadboizxc'>@deadboizxc</a>)

```python3
from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix


# if your module has packages from PyPi

# from utils.scripts import import_library
# example_1 = import_library("example_1")
# example_2 = import_library("example_2")

# import_library() will automatically install required library
# if it isn't installed


@Client.on_message(filters.command("example_edit", prefix) & filters.me)
async def example_edit(client: Client, message: Message):
    await message.edit("<code>This is an example module</code>")


@Client.on_message(filters.command("example_send", prefix) & filters.me)
async def example_send(client: Client, message: Message):
    await client.send_message(message.chat.id, "<b>This is an example module</b>")


# This adds instructions for your module
modules_help["example"] = {
    "example_send": "example send",
    "example_edit": "example edit",
}

# modules_help["example"] = { "example_send [text]": "example send" }
#                  |            |              |        |
#                  |            |              |        └─ command description
#           module_name         command_name   └─ optional command arguments
#        (only snake_case)   (only snake_case too)
```

<h2>Credits</h2>
<nav>
<li><a href='https://github.com/deadboi-zxc'>deadboi-zxc</a></li>
<li><a href='http://t.me/deadboizxc'>deadboizxc</a></li>
</nav>
<h4>Written on <a href='https://github.com/pyrogram/pyrogram'>Pyrogram❤️</a> and <a href='https://github.com/MarshalX/tgcalls/tree/main/pytgcalls'>pytgcalls❤️</a></h4>
