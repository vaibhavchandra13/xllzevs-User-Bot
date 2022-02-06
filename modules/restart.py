from pyrogram import Client, filters
import os

import re

class Info:
	short_desc= "[Инструменты] Перезагружает бота."
	desc = "Перезагружает бота."
	commands = {"рестарт": "Перезагрузить бота"}
	version = 1.0
	author = "@youngtitanium"

@Client.on_message(filters.me & filters.regex('^рестарт',re.I))
async def restart_bot(_, msg):
	await msg.edit("Перезагрузка...")
	await msg.edit("Перезагрузка прошла успешно!")	
	os.execvp("python3", ("python3", "main.py", ))