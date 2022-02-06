from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep

import random


class Info:
    short_desc = "[Развлекательный] Щелчок Таноса."
    desc = "Щелчок Таноса."
    version = 0.9
    author = "@xllzevs"
    commands = {"щелчок": "Щелчок Таноса."}

@Client.on_message(filters.command('щелчок', prefix) & filters.me)
def thanos(_, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]
 
    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]
 
    random.shuffle(members)
 
    app.send_message(chat, "Щелчок Таноса ... *щёлк*")
 
    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> ожидание", e.x, "секунд.")
            time.sleep(e.x)
 
    app.send_message(chat, "Но какой ценой?")
