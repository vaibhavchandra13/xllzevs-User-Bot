from pyrogram import Client as app, filters
import pyrogram

class Info:
	short_desc = "[Инструменты] Добавить челика в чат."
	desc = "Модуль для добавления человека в чат."
	commands = {"invite id|номер человека": "Добавляет человека в чат."}
	author = "@xllzevs"

@app.on_message(filters.me & filters.command("invite", prefix) & ~filters.private)
def invite_users(app, msg):
	chat_id = msg.chat.id
	reply = msg.reply_to_message
	if reply != None:
		ids = msg.reply_to_message.from_user.id
		try:
		    app.add_chat_members(chat_id, ids)
		except:
			msg.edit("**Этого челика нельзя добавить**")
	else:
		try: 
			user = msg.text.split(" ", 1)[1]
			try:
				app.add_chat_members(chat_id, user)
			except pyrogram.errors.exceptions.bad_request_400.UserNotMutualContact:
				msg.edit("**Этого пользователя нельзя добавить**")
			except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
				msg.edit("**Нет такого айди**")
			except:
				msg.edit('Не контакт')
		except:
			msg.edit("**Мало информации**")
