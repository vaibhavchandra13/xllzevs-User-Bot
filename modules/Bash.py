from pyrogram import Client, filters
import subprocess 

class Info:
	short_desc = "[Инструменты] Запуск bash."
	desc = "Выполнение bash кода с возвратом в телеграм."
	author = "Неизвестен(переделал: @youngtitanium)"
	version = "2.0"
	commands = {".bash [код]": "Выполнение кода."}

def bash(code: str):
	return subprocess.getoutput(code)

@Client.on_message(filters.me & filters.command("bash", "."))
async def bash_command(_, msg):
	reply = msg.reply_to_message
	
	if len(msg.text.split()) != 1:
		code = msg.text.split(maxsplit=1)[1]
	elif reply:
		code = str(msg.reply_to_message.text)
	else:
	    await msg.edit("Код отсутствует.")
	    return
	result = bash(code)
	if result == "":
		result = "None"
	await msg.edit(f"**Код:**\n\n```{code}```\n\n**Результат:**\n\n```{result}```")
