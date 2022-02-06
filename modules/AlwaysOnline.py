from pyrogram import Client, filters, ContinuePropagation
from pyrogram.raw.functions.account import UpdateStatus

class Info:
    short_desc = "[Разное] Держать в онлайне."
    desc = "Модуль который держит вас в онлайне."
    version = 2.0
    commands = {"online": "Включить модуль."}

on = True

@Client.on_message()
async def online(app, _):
    if on:
        await app.send(UpdateStatus(offline=False))
    raise ContinuePropagation

@Client.on_message(filters.me & filters.command("online", prefix))
async def switch(_, msg):
    global on
    if on:
        on = False
    else:
        on = True
    await msg.edit("Всегда онлайн: "+ str(on))
    
