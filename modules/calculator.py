from pyrogram import filters, Client as app

class Info:
  short_desc = "[Инструменты] Калькулятор."
  desc = "Обчный колькулятор для решение примеров на умножение|деление|плюс|минус."
  commands = {".calc [пример]"}
  author = "@xllzevs"
  
@app.on_message(filters.me & filters.command("calc", "."))
def calculator(_, message):
  reply = message.reply_to_message
  if reply is None:
    try:
      example = message.text.split(" ",1)[1]
      message.edit(f"**{eval(example)}**")
    except:
      pass
  else:
    example = message.reply_to_message.text
    message.edit(f"**{eval(example)}**")