import asyncio
import time

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

class Info:
    short_desc = "[Развлекательный] Постепенный ввод сообщения с typing эффектом."
    desc = "Постепенно вводит сообщения."
    author = "@xllzevs"
    commands = {"type [text]"}

@Client.on_message(filters.command("type", prefix) & filters.me)
async def type(client: Client, message: Message):
    orig_text = " ".join(message.command[1:])
    text = orig_text
    tbp = ""
    typing_symbol = "▒"

    while tbp != text:
        try:
            await message.edit(tbp + typing_symbol)
            await asyncio.sleep(0.1)

            tbp += text[0]
            text = text[1:]

            await message.edit(tbp)
            await asyncio.sleep(0.1)

        except FloodWait as e:
            time.sleep(e.x)
