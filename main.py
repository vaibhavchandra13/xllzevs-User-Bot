from pyrogram import Client, idle

app = Client("session_name") # для подключения доп.сессий нужно добавить:
# app = Client2("session_name2")

app.start()
# app.start2()
idle()
