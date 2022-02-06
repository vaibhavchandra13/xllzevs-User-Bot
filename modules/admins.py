from pyrogram import Client as app, filters
import pyrogram
from pyrogram.types import ChatPermissions
import time

class Info:
    short_desc = "[Инструменты] Облегчение модерации"
    desc = (
        "Модуль для облегчения модерации групп."
        )
    author = "@xllzevs"
    commands = {
        "promote": "Сделать участника группы админом",
        "demote": "Сделать админа группы обычным участником",
        "ban": "Забанить участника группы",
        "unban": "Разбанить участника группы",
        "mute": "Замутить участника группы",
        "unmute": "Размутить участника группы",
        "kick": "Кикнуть участника группы"
    }

@app.on_message(filters.me & filters.command("promote","."))
def promontion(app, msg):
    try:
        user_id = msg.reply_to_message.from_user.id
        try:
            pref = msg.text.split()[1]
        except:
            pref = "Админ"
        app.promote_chat_member(msg.chat.id, user_id)
        app.set_administrator_title(msg.chat.id, user_id, title = pref)
        msg.edit('**Повышен(а)**')
    except pyrogram.errors.exceptions.bad_request_400.ChannelInvalid:
        msg.edit('**Это не чат**')
    except AttributeError:
        msg.edit('**Кого повышаем?**')


@app.on_message(filters.me & filters.command("demote","."))
def demontion(app, msg):
  try:
    user_id = msg.reply_to_message.from_user.id
    app.promote_chat_member(msg.chat.id, user_id, False,False,False,False,False,False,False,False)
    msg.edit('**Понижен(а)**')
  except pyrogram.errors.exceptions.bad_request_400.ChannelInvalid:
    msg.edit('**Это не чат**')
  except AttributeError:
    msg.edit('**Кого понижаем?**')

@app.on_message(filters.me & filters.command("ban","."))
def baner(app, msg):
    try:
        user_id = msg.reply_to_message.from_user.id
        user_name = msg.reply_to_message.from_user.first_name
        try:
            timer = msg.text.split(" ",1)[1]
            app.kick_chat_member(msg.chat.id, user_id, int(time.time() + int(timer)))
            msg.edit(f"**{user_name} забанен на {timer} секунд**")
        except:
            app.kick_chat_member(msg.chat.id, user_id)
            msg.delete()
    except AttributeError:
        msg.edit("**Кого банить?**")
    except pyrogram.errors.exceptions.bad_request_400.ChatAdminRequired:
        msg.edit("**Я не одмен**")
    except pyrogram.errors.exceptions.bad_request_400.UserAdminInvalid:
        msg.edit("**Этот лох - Админ**")


@app.on_message(filters.me & filters.command("unban","."))
def unbaner(app, msg):
  try:
    user_id = msg.reply_to_message.from_user.id
    app.unban_chat_member(msg.chat.id, user_id)
  except AttributeError:
    msg.edit("**Кого разбанить?**")
  msg.delete()


@app.on_message(filters.me & filters.command("kick","."))
def kick(app, msg):
    try:
        user_id = msg.reply_to_message.from_user.id
        app.kick_chat_member(msg.chat.id, user_id)
        app.unban_chat_member(msg.chat.id, user_id)
        msg.delete()
    except AttributeError:
        msg.edit("**Кого кикать?**")


@app.on_message(filters.me & filters.command("mute","."))
def mute(app, msg):
    try:
        try:
            timer = int(msg.text.split()[1])
        except:
            timer = 0
        name = msg.reply_to_message.from_user.first_name
        user_id = msg.reply_to_message.from_user.id
        app.restrict_chat_member(msg.chat.id, user_id, ChatPermissions(can_send_messages = False), int(time.time() + timer))
        msg.edit(f"**Теперь {name} заглушен(а)**")
    except AttributeError:
        msg.edit("**Кого мутить?**")



@app.on_message(filters.me & filters.command("unmute","."))
def unmute(app, msg):
    try:
        user_id = msg.reply_to_message.from_user.id
        app.restrict_chat_member(msg.chat.id, user_id, ChatPermissions(can_send_messages = True, can_send_media_messages = True, can_send_stickers = True, can_send_animations = True, can_send_games = True, can_send_polls = True, can_use_inline_bots = True))
        msg.edit("**Ладно, он(а) вновь может говорить**")
    except AttributeError:
        msg.edit("**Кого размутить?**")