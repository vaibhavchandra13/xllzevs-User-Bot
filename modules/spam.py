import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

class Info:
    short_desc = "[Разное] Спам."
    desc = "Модуль для спама."
    version = 1.7
    author = "@xllzevs"
    commands = {
	    ".spam [количество сообщений] [text]": "Обычный спам сообщениями.",
	    ".statspam [количество сообщений] [text]": "Обчный спам сообщениями с последующим удалением.",
	    ".fastspam [количество сообщений] [text]": "Быстрый спам сообщениями.",
	    ".slowspam [количество сообщений] [text]": "Медленный спам сообщениями."
    }

@Client.on_message(filters.command("statspam", ".") & filters.me)
async def statspam(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)
    await message.delete()
    for _ in range(quantity):
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.1)
        await msg.delete()
        await asyncio.sleep(0.1)


@Client.on_message(filters.command("spam", ".") & filters.me)
async def spam(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)
    await message.delete()

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(
                message.chat.id, spam_text, reply_to_message_id=reply_to_id
            )
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


@Client.on_message(filters.command("fastspam", ".") & filters.me)
async def fastspam(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)
    await message.delete()

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(
                message.chat.id, spam_text, reply_to_message_id=reply_to_id
            )
            await asyncio.sleep(0.02)
        return

    for _ in range(quantity):
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.02)


@Client.on_message(filters.command("slowspam", ".") & filters.me)
async def slowspam(client: Client, message: Message):
    quantity = message.command[1]
    spam_text = " ".join(message.command[2:])
    quantity = int(quantity)
    await message.delete()

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(
                message.chat.id, spam_text, reply_to_message_id=reply_to_id
            )
            await asyncio.sleep(0.9)
        return

    for _ in range(quantity):
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.9)