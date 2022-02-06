from pyrogram import Client, filters

import re

class Info:
	short_desc = "[Инструменты] Узнать id чата."
	desc = "Модуль для вывода id чата."
	commands = {".id": "Отправляет id чата.",
				"id": "Отправляет id человека."}
	author = "@xllzevs"

@Client.on_message(filters.me & filters.command("id", "/", "."))
def chat_id(app, msg):
	msg.edit(msg.chat.id)

@Client.on_message(filters.me & filters.command("uid", "/", "."))
def user_id(app, msg):
	try:
		msg.edit(msg.reply_to_message.from_user.id)
	except AttributeError:
		msg.edit('No reply message.')
