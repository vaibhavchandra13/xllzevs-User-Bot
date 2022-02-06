from pyrogram import Client, filters
from pyrogram.errors import FloodWait

 
import time
from time import sleep
import random


import re


class Info:
    short_desc = "[Развлекательный] Взлом аккаунта."
    desc = "Взлом аккаунта."
    author = "@xllzevs"
    commands = {"взломать"}


@Client.on_message(filters.regex('^взломать',re.I) & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "📟 Взлом вашего аккаунта в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Аккаунт успешно взломан!")
    sleep(3)
 
    msg.edit("📂Поиск данных пользователя ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "📂Поиск данных пользователя ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("📂Аккаунт взломан, все необходимые данные получены!")