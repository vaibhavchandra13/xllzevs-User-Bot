import asyncio
import datetime

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

class Info:
    short_desc = "[Разное] Держать в афк."
    desc = "Модуль который держит вас в афк."
    version = 1.4
    author = "Неизвестно(отредактировал @xllzevs)"

async def afk_handler(client, message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = end - start
        if message.from_user.is_bot is False:
            await message.reply_text(
                f"<b>Я афк {afk_time}</b>\n" f"<b>Причина:</b> <i>{reason}</i>"
            )
    except NameError:
        pass


@Client.on_message(filters.command("afk", prefix) & filters.me)
async def afk(client, message):
    global start, end, handler, reason
    start = datetime.datetime.now().replace(microsecond=0)
    handler = client.add_handler(
        MessageHandler(afk_handler, (filters.private & ~filters.me))
    )
    if len(message.text.split()) >= 2:
        reason = message.text.split(" ", maxsplit=1)[1]
    else:
        reason = "None"
    await message.edit("<b>Я собираюсь в афк</b>")


@Client.on_message(filters.command("unafk", prefix) & filters.me)
async def unafk(client, message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = end - start
        await message.edit(f"<b>Я больше не АФК.\nЯ был афк {afk_time}</b>")
        client.remove_handler(*handler)
    except NameError:
        await message.edit("<b>Ты не был афк</b>")
        await asyncio.sleep(3)
        await message.delete()
