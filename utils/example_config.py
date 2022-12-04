import os
import sys


TOKEN_NUM = '' #токен вашого бота
API_HASH_NUM = '' # api hash від вашого аккаунта
API_ID_NUM = # api id від вашого аккаунта
ADMIN_CHATID_NUM = "" # id  чату
ADMIN_USERNAME_NUM = "" # ваш юзернейм


channel_id = # айді каналу за допомогою bot api
db_name = "db.sqlite3" # це назва БД



#1
  """
; Це приклад файлу конфігурації"""

#2
  """
; Перейменуйте або зробіть копію цього файла,
  та вставте свої данні аккаунту telegram."""

#3
  """
; Щоб підключити 2 або більше акаунтів потрібно відредагувати 2 файли:"""

      # Ці данні потрібно дописати до файлу '''config.py''',
      # або до цього якщо ви просто перейменували цей файл:


        """
        TOKEN_2 = '' #токен вашого бота
        API_HASH_2 = '' # api hash від вашого аккаунта
        API_ID_2 = # api id від вашого аккаунта
        ADMIN_CHATID_2 = "" # id  чату
        ADMIN_USERNAME_2 = "" # ваш юзернейм

        channel_id = # айді каналу за допомогою bot api
        db_name = "db.sqlite3" # це ти БД"""


        ## ЗАМІСТЬ ЦИФРИ 'NUM' НАПИШІТЬ ІНШЕ ЧІСЛО
           " ps. число не має значення, воно просто для нумераціі"

#4
  """
; Зробіть копію файлу 'example_client.py'
  з додаванням чісла як в файлі конфігурації >> 'client2.py'"""

  """
; Відредагуйте файл 'client2.py' таким чином:"""


import subprocess
import os
import sys
from pyrogram import *
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
from time import sleep
from utils.config import (
        'змініть нумерацію для цих змінних'
    API_ID_NUM,
    API_HASH_NUM,
    TOKEN_NUM,
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

        'замість NUM чісло яке ви вказали'

app = Client("my_account_NUM",
              api_id=API_ID_NUM,
              api_hash=API_HASH_NUM,
              bot_token=TOKEN_NUM,
              plugins=dict(root="modules")
             )

