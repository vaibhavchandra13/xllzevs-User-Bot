from pyrogram import Client as app, filters

class Info:
	short_desc = "[Инструменты] Модуль для создания файла с расширением .py"
	desc = ("Модуль для создания файлов с расширением .py")
	version = "1.3"
	commands = {
		"add": "Название файла."
		}
	author = "Неизвестно."


@app.on_message(filters.me & filters.command("add", prefix))
def module_adder(app, msg):
	try:
		name = msg.text.split(" ", 1)[1]
		text = msg.reply_to_message.text
		f = open(f"modules/{name}.py","w+")
		f.write(text)
		app.restart(False)
		msg.edit("**Успешно**")
	except:
		pass
