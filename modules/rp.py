from pyrogram import Client, filters

class Info:
	short_desc = "[Развлекательный] РП команды."
	desc = "РП команды для взаимодействия с пользывателем."
	version = 1.7
	commands = {"пом"}
	author = "@xllzevs"

@Client.on_message(filters.me & filters.command("пом", prefix),group = 3)
def hel(app, msg):
	msg.edit("""
➡️нагнуть
➡️посадить
➡️обнять
➡️поцеловать
➡️доброе
➡️спокойной
➡️закопать
➡️привет
➡️пока
➡️ага
➡️злость
➡️обиделся
➡️пощада
➡️ахах
➡️своя  - в этой команде вы сами пишите свой текст""")

# нагнуть
@Client.on_message(filters.reply & filters.me & filters.command("нагнуть", prefix), group = 3)
def nag(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"😈[{app.get_me().first_name}](tg://user?id={app.get_me().id}) ** нагнул** [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id}) **{text}** 😈")

# посадить
@Client.on_message(filters.reply & filters.me & filters.command("посадить", prefix), group = 3)
def pos(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"🍾[{app.get_me().first_name}](tg://user?id={app.get_me().id}) ** посадил на бутылку** [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}** 🍾")

# обнять 	
@Client.on_message(filters.reply & filters.me & filters.command("обнять", prefix), group = 3)
def obn(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"🤗[{app.get_me().first_name}](tg://user?id={app.get_me().id})  сильно обнял [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}**🤗 ")

# поцеловать
@Client.on_message(filters.reply & filters.me & filters.command("поцеловать", prefix), group = 3)
def poc(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"😘[{app.get_me().first_name}](tg://user?id={app.get_me().id}) ** поцеловал** [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}**😘")

# доброе
@Client.on_message(filters.reply & filters.me & filters.command("доброе", prefix), group = 3)
def dobr(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"☀️[{app.get_me().first_name}](tg://user?id={app.get_me().id}) ** пожелал доброго утра** [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}**☀️")

# спокойной
@Client.on_message(filters.reply & filters.me & filters.command("спокойной", prefix), group = 3)
def spok(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"🌙[{app.get_me().first_name}](tg://user?id={app.get_me().id}) ** пожелал спокойной ночи** [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}**🌙")

# закопать
@Client.on_message(filters.reply & filters.me & filters.command("закопать", prefix), group = 3)
def zak(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"🤬[{app.get_me().first_name}](tg://user?id={app.get_me().id}) ** закопал** [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}**😡")

# привет
@Client.on_message(filters.reply & filters.me & filters.command("привет", prefix), group = 3)
def priv(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"👋[{app.get_me().first_name}](tg://user?id={app.get_me().id}) ** поздоровался с ** [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}**👋")

# пока
@Client.on_message(filters.reply & filters.me & filters.command("пока", prefix), group = 3)
def poka(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"**👋[{app.get_me().first_name}](tg://user?id={app.get_me().id})  поопрощался с  **[{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}**👋")

# ага
@Client.on_message(filters.reply & filters.me & filters.command("ага", prefix), group = 3)
def aga(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"**😊[{app.get_me().first_name}](tg://user?id={app.get_me().id})  согласился с ** [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}**😊")

# зол
@Client.on_message(filters.reply & filters.me & filters.command("злость", prefix), group = 3)
def zol(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"**😡[{app.get_me().first_name}](tg://user?id={app.get_me().id})  злится на ** [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}**😡")

# обиделся
@Client.on_message(filters.reply & filters.me & filters.command("обиделся", prefix), group = 3)
def obid(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"**😢[{app.get_me().first_name}](tg://user?id={app.get_me().id})  обиделся на** [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}**😭")

# пощ
@Client.on_message(filters.reply & filters.me & filters.command("пощада", prefix), group = 3)
def posh(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"** 😎[{app.get_me().first_name}](tg://user?id={app.get_me().id})  заставил просить о пощаде** [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}** 😎")

# ахах
@Client.on_message(filters.reply & filters.me & filters.command("ахах", prefix), group = 3)
def ahah(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"** 😂[{app.get_me().first_name}](tg://user?id={app.get_me().id})  посмеялся над** [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})**{text}** 😂")

# своя
@Client.on_message(filters.reply & filters.me & filters.command("своя", prefix), group = 3)
def svoya(app, msg):
	text = ""
	if len(msg.text.split(" ")) > 1:
		text = " ".join(msg.text.split(" ")[1:])
	msg.edit(f"**😏  [{app.get_me().first_name}](tg://user?id={app.get_me().id}) { text} [{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id})😏**")
