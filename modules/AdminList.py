import json
from html import escape as t
from time import perf_counter

from pyrogram import Client, filters
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.raw.functions.messages.get_all_chats import GetAllChats
from pyrogram.types import Message

class Info:
    short_desc = "[Инструменты] Получить список административных и собственных чатов."
    desc = "Модуль для вывода списка административных и собственных чатов."
    commands = {".admlist": "Выводит административные и собственные чаты."}
    author = "Неизвестно(переделал @xllzevs)"

@Client.on_message(filters.command("admlist", ".") & filters.me)
async def ownlist(client: Client, message: Message):
    tstart = perf_counter()
    await message.edit("<code>Извлечение информации... (это займет некоторое время)</code>")
    chatlist = []
    try:
        _ = await client.send(GetAllChats(except_ids=[]))
        chats = json.loads(str(_))
        for chat in chats["chats"]:
            if chat.get("migrated_to") is None and (
                chat.get("creator") is True
                or chat.get("admin_rights") is not None
            ):
                role = "creator" if chat.get("creator") is True else "administrator"
                chatlist.append(
                    {
                        "chat_name": str(chat["title"]),
                        "chat_id": chat["id"],
                        "role": role,
                        "username": chat.get("username"),
                        "link": "https://t.me/c/{}/1".format(chat["id"]),
                    }
                )

        adminned_chats = "<b>Администрируемые чаты:</b>\n"
        owned_chats = "<b>Принадлежащие чаты:</b>\n"
        owned_chats_with_username = "<b>Собственные чаты с именем пользователя:</b>\n"

        c_adminned_chats = 0
        c_owned_chats = 0
        c_owned_chats_with_username = 0

        for chat in chatlist:
            if chat["role"] == "creator" and chat["username"] is not None:
                c_owned_chats_with_username += 1
                owned_chats_with_username += f'{c_owned_chats_with_username}. <a href="{chat["link"]}">{t(chat["chat_name"])}</a> - @{chat["username"]}\n'
            elif chat["role"] == "creator":
                c_owned_chats += 1
                owned_chats += f'{c_owned_chats}. <a href="{chat["link"]}">{t(chat["chat_name"])}</a>\n'
            elif chat["role"] == "administrator":
                c_adminned_chats += 1
                adminned_chats += f'{c_adminned_chats}. <a href="{chat["link"]}">{t(chat["chat_name"])}</a>\n'
        stats = f"<b><u>Total:</u></b> {len(chatlist)}\n<b><u>Администрируемые чаты:</u></b> {c_adminned_chats}\n<b><u>Принадлежащие чаты:</u></b> {c_owned_chats}\n<b><u>Собственные чаты с именем пользователя:</u></b> {c_owned_chats_with_username}"
        tstop = perf_counter()
        await message.edit(
            adminned_chats
            + "\n"
            + owned_chats
            + "\n"
            + owned_chats_with_username
            + "\n"
            + stats
            + "\n\n"
            + f"Сделано в {int(tstop - tstart)} секунд.",
            disable_web_page_preview=True,
        )
    except FloodWait as e:
        await message.edit(
            "<b>Произошла ошибка.</b>\n<code>Ожидание наводнения. Попробуйте еще раз в {} секунд</code>".format(
                e.x
            )
        )