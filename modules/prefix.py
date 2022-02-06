from pyrogram import Client, filters
from pyrogram.types import Message

class Info:
    short_desc = "[Инструменты] Установка префикса."
    desc = "Модуль для установки кастомного префикса."
    author = "Неизвестно(отредактировал @xllzevs)"
    commands = {"setprefix": "Устанавливает кастомный префикс."}

@Client.on_message(
    filters.command(["setprefix"], prefix) & filters.me
)
async def pref(client: Client, message: Message):
    if len(message.command) > 1:
        prefix = message.command[1]
        print(message.command)
        db.set("core.main", "prefix", prefix)
        await message.edit(f"<b>Префикс [ <code>{prefix}</code> ] установлен!</b>")
        await restart()
    else:
        await message.edit("<b>Префикс не должен быть пустым!</b>")
