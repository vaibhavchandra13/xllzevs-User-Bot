from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from asyncio import sleep

slot = ["True"]

class Info:
	desc = "Постоянная отправка сообщений в указанном кол-ве."
	short_desc = "[Разное] Постоянная отправка сообщений."
	cmd_list = {
		".автореп [интервал] [кол-во] [текст]" : "спам сбщ реплаем(удаляются).",
		".авто [интервал] [кол-во] [текст]" : "спам обычными сбщ(удаляются).",
	}
	ver = 2.1

@Client.on_message(filters.me & filters.command("автореп", "."))
async def _(app, message):
	try:
		timer = message.text.split(" ", 3)[1]
		kolvo = message.text.split(" ", 3)[2]
		auto_send = message.text.split(" ", 3)[3]
		re_ids = message.reply_to_message.from_user.id
		repl = message.reply_to_message
		stime = float(timer)
		kol = int(kolvo)
		perc = 0
		message.delete()
		if repl == None:
			if kolvo == "0":
				while True:
					if slot[0] == "True":
						try:
							auto = await app.send_message(message.chat.id, auto_send, reply_to_message_id = re_ids)
							await sleep(stime)
							await app.delete_messages(
							    chat_id=message.chat.id,
							    message_ids=auto.message_id)
						except:
							await message.edit_text("Шо-то не то")
					else:
						break
			elif kol != 0:
				while perc < kol:
					if slot[0] == "True":
						try:
							auto = await app.send_message(message.chat.id, auto_send)
							await sleep(stime)
							await app.delete_messages(
							    chat_id=message.chat.id,
							    message_ids=auto.message_id)
							perc += 1
						except FloodWait as e:
							await sleep(e.x)
					else:
						break
		else:
			if kolvo == "0":
				while True:
					try:
						if slot[0] == "True":
							try:
								auto = await app.send_message(message.chat.id, auto_send, reply_to_message_id=repl.message_id)
								await sleep(stime)
								await app.delete_messages(
								    chat_id=message.chat.id,
								    message_ids=auto.message_id)
							except:
								await message.edit_text("Шо-то не то")
						else:
							break
					except:
						await app.send_message(message.chat.id, "сообщение пропало")
						break
			elif kol != 0:
				while perc < kol:
					try:
						if slot[0] == "True":
							try:
								auto = await app.send_message(message.chat.id, auto_send, reply_to_message_id=repl.message_id)
								await sleep(stime)
								await app.delete_messages(
								    chat_id=message.chat.id,
								    message_ids=auto.message_id)
								perc += 1
							except FloodWait as e:
								await sleep(e.x)
						else:
							break
					except:
						await app.send_message(message.chat.id, "сообщение пропало")
						break
	except:
		await message.edit_text(f"```{message.text}```\nНеверный формат") 



@Client.on_message(filters.me & filters.command("авто", "."))
async def hacker(app, message):
	try:
		interval, count, message_text = message.text.split(" ", 3)[1:]
		interval = float(interval)
		if count.isdigit():
			count = int(count)
		else:
			await message.edit_text(
				"Количество должно быть числом"
				)
			return
		perc = 0
		await message.delete()
		for _ in range(interval):
			try:
				msg = await app.send_message(message.chat.id, message_text)
				await sleep(1)
				await msg.delete()
				await sleep(interval)
			except FloodWait as e:
				await sleep(e.x)
	except Exception as e:
		await message.edit_text(f"```{message.text}```\nНеверный формат\n\n"+str(e))

