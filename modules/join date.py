import os
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message

class Info:
    short_desc = "[Инструменты] Список всех участников чата отсортированные по дате вступления" # он вроде не работает, если сможете починить его то если не сложно скиньть мне в тг
    desc = "Модуль для получиния списка всех участников чата отсортированных по дате вступления в группу."
    version = 1.0
    author = "@xllzevs"


@Client.on_message(filters.command("joindate" prefix) & filters.me)
def join_date(app, message: Message):
    members = []
    for m in app.iter_chat_members(message.chat.id):
        members.append(
            (
                m.user.first_name,
                m.joined_date or app.get_messages(message.chat.id, 1).date,
            )
        )

    members.sort(key=lambda member: member[1])

    with open("joined_date.txt", "w", encoding="utf8") as f:
        f.write("Дата Вступления      Имя\n")
        for member in members:
            f.write(
                str(datetime.fromtimestamp(member[1]).strftime("%y-%m-%d %H:%M"))
                + f" {member[0]}\n"
            )

    app.send_document(message.chat.id, "joined_date.txt")
    os.remove("joined_date.txt")
