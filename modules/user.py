import asyncio

from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

class Info:
	short_desc = "[Инструменты] Показывает информацию о человеке."
	desc = "Модуль для отображения онформации о человеке."
	version = 1.4
	author = "@xllzevs"
	commands = {".user|.perm": "показывает информацию о человеке."}

@Client.on_message(filters.command("user", ".") & filters.me)
async def get_user_info(client: Client, message: Message):
    if len(message.text.split()) >= 2:
        try:
            user = await client.get_users(message.text.split()[1])
            user = user.id
        except:
            try:
                user = message.reply_to_message.from_user.id
            except:
                user = message.from_user.id
    else:
        try:
            user = message.reply_to_message.from_user.id
        except:
            user = message.from_user.id
    user_info = (await client.get_users(user))
    if user_info.username is None:
        username = "None"
    else:
        username = f"@{user_info.username}"
    user_info = f"""|=<b>Username: {username}
Id: <code>{user_info.id}</code>
Бот: <code>{user_info.is_bot}</code>
Скам: <code>{user_info.is_scam}</code>
Имя: <code>{user_info.first_name}</code>
Удаленный аккаунт: <code>{user_info.is_deleted}</code>
</b>"""
    await message.edit(user_info)


@Client.on_message(filters.command("perm", ".") & filters.me)
async def get_full_user_info(client: Client, message: Message):
    await message.edit("<code>Получение информации...</code>")
    if len(message.text.split()) >= 2:
        try:
            user = await client.get_users(message.text.split()[1])
            user = user.id
        except:
            try:
                user = message.reply_to_message.from_user.id
            except:
                user = message.from_user.id
    else:
        try:
            user = message.reply_to_message.from_user.id
        except:
            user = message.from_user.id
    try:
        msg = await client.send_message("@creationdatebot", f"/id {user}")
        await asyncio.sleep(1)
        date_dict = await client.get_history("@creationdatebot")
        date_dict = date_dict[0].text
        await client.send(
            functions.messages.DeleteHistory(
                peer=await client.resolve_peer(747653812), max_id=msg.chat.id
            )
        )
        user_info = await client.send(
            functions.users.GetFullUser(id=await client.resolve_peer(user))
        )
        if user_info.users[0].username is None:
            username = "None"
        else:
            username = f"@{user_info.users[0].username}"
        about = "None" if user_info.full_user.about is None else user_info.full_user.about
        user_info = f"""|=<b>Username: {username}
Id: <code>{user_info.users[0].id}</code>
Дата создания аккаунта: <code>{date_dict}</code>
Бот: <code>{user_info.users[0].bot}</code>
Скам: <code>{user_info.users[0].scam}</code>
Имя: <code>{user_info.users[0].first_name}</code>
Удаленный аккаунт: <code>{user_info.users[0].deleted}</code>
BIO: <code>{about}</code>
В контактах: <code>{user_info.users[0].contact}</code>
Может закреплять сообщения: <code>{user_info.full_user.can_pin_message}</code>
Взаимный контакт: <code>{user_info.users[0].mutual_contact}</code>
Хеш доступа: <code>{user_info.users[0].access_hash}</code>
Ограниченый: <code>{user_info.users[0].restricted}</code>
Верифицированный: <code>{user_info.users[0].verified}</code>
Доступны ли телефонный звонки: <code>{user_info.full_user.phone_calls_available}</code>
Приватные телефонные звонки: <code>{user_info.full_user.phone_calls_private}</code>
Заблокирован: <code>{user_info.full_user.blocked}</code></b>"""
        await message.edit(user_info)
    except:
    	await message.edit("<code>user_info error<code>")