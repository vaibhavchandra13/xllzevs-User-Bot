import time
from pyrogram import Client as app, filters

class Info:
	short_desc = "[Инструменты] Показывает безпрерывное время работы бота."
	desc = "Модуль для просмотра безпрерывной работы юзер бота."
	commands = {".uptime": "Показывает время безпрерывной работы бота."}
	author = "@xllzevs"

timer = time.time()

def uptime():
  now = time.time() - timer
  return int(now)

@app.on_message(filters.me & filters.command("uptime","."))
def uptimer(_, message):
  hours = int((uptime() - uptime() % 60) / 3600)
  minutes = uptime() - hours * 3600
  minutes = int((minutes - minutes % 60) / 60)
  seconds = int(uptime() % 60) 
  message.edit(f"ЮБ работает уже {hours} час(ов), {minutes} минут(ы) и {seconds} секунд(ы)") 