from pyrogram import Client, filters
import os
os.popen("pip install gtts")
from gtts import gTTS 


class Info:
	short_desc = "[Развлекательный] Преобразовывает текст в голосовое сообщение."
	desc = "Модуль для преобразования текста в голосовое сообщение."
	commands = {".voice [text]"}
	author = "@xllzevs"

@Client.on_message(filters.me & filters.command('voice', '.'))
async def voice(app, msg):
	try:
		await msg.delete()
		text = msg.text.split(maxsplit=1)[1]
		language = 'ru'
		speech = gTTS(text = text, lang = language, slow = False)
		speech.save("downloads/module_voice.ogg")
		if msg.reply_to_message:
			await msg.reply_to_message.reply_voice("downloads/module_voice.ogg")
		else:
			await app.send_voice(msg.chat.id, "downloads/module_voice.ogg")
	except IndexError:
		await msg.edit("**ТЫ ПОХОДУ ТЕКСТ ЗАБЫЛ НАПИСАТЬ!)**")