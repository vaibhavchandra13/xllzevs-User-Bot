from pyrogram import Client, filters

from datetime import datetime

import re

class Info:
	short_desc = "[Инструменты] Показывает пинг."
	desc = "Модуль для отображения пинга."
	commands = {"пинг"}
	author = "@xllzevs"

@Client.on_message(filters.me & filters.regex('^пинг',re.I))
async def ping(app, msg):
    start = datetime.now()
    await msg.edit('`Понг!`')
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await msg.edit(f"**Понг!**\n`{m_s} ms`")