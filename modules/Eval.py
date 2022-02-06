import re
import traceback
from io import StringIO
from contextlib import redirect_stdout
from html import escape
import asyncio
import uuid

from meval import meval
from pyrogram import Client, filters, types
from pyrogram.handlers import MessageHandler


class Info:
    short_desc = desc = "[Инструменты] Выполнение Python кода."
    version = 4.4
    author = "Кобан + @youngtitanium"
    commands = {".e [code]": "Выполнение code."}

__storage__ = {
	"results": {}
	}

class CustomInput:
    def __init__(self, app, message):
        self.app = app
        self.message = message

    def __str__(self):
        return repr(input)
    
    def __repr__(self):
        return repr(input)

    def __int__(self):
        return -666
    
    async def __call__(self, text = "Жду сообщения...", everyone=False):
        return await wait_quote(self.app, self.message, text, everyone)
        
async def wait_quote(app, message, text="Жду сообщения...", everyone=False):
    await message.edit(
        text=text
        )
    last = await app.get_history(chat_id=message.chat.id, offset=0, limit=1)
    received = False
    counter = 0
    while 1:
        for msg in last:
            if (
                msg.reply_to_message and
                msg.reply_to_message.message_id == message.message_id
                ):
                if everyone:
                    received = msg
                    break
                elif not everyone and msg.from_user.id == message.from_user.id:
                	received = msg
                	break
               
        if received:
            break
        last = await app.get_history(chat_id=message.chat.id, offset=0, limit=5)
        if counter < 10:
            await asyncio.sleep(0.5)
        else:
            counter = 0
            await asyncio.sleep(1.4)
        counter += 1
    await message.edit(
        text="Обработка"
        )
    content = received.text
    if not everyone:
        await received.delete()
    else:
        try:
            await received.delete()
        except:
            pass
    return content

async def slicer(text, step):
    for i in range(0, len(text), step):
        yield text[i:i+step]

code_regex = re.compile(r"^код:\n([\w\W\n]+)", flags=re.I)
output_regex = re.compile(r"((возвращено|ошибка|вывод):[\w\W\n]*)", flags=re.I)
 
def get_code(string, msg=False):
    code = code_regex.findall(string)
    if len(code) > 0 and len(out := output_regex.findall(code[0])) > 0:
        code = code[0].replace(out[0][0],"")
    elif len(code) > 0:
        code = code[0]
    else:
        code = ""
    if code == "" and msg:
        return msg.reply_to_message.text
    return code


@Client.on_message(filters.regex(code_regex) & filters.me & filters.edited)
@Client.on_message(filters.command("e", ".") & filters.me)
async def evalcmd(app, msg):
    if msg.command:
        if len(msg.command) > 1:
            args = msg.text.split(maxsplit=1)
            if len(args) > 1:
            	args = args[1]
            else:
            	args = "None"
        else:
            args = get_code(msg.reply_to_message.text, msg)
    else:  # если редактирование
        args = get_code(msg.text, msg)
    result = StringIO()
    error = None
    output = None
    attrs = await getattrs(app, msg)
    attrs.update(globals())
    try:
        with redirect_stdout(result):
            output = await meval(args, globals(), **attrs)
    except:
        error = traceback.format_exc(limit=0)
    result = result.getvalue()
    if len(str(output)) < 3900:
        result_output = f"**Код:**\n```{escape(args)}```"
        result_output += "\n\n**Возвращено:**\n```{}```".format(escape(str(output)).rstrip('\n') ) if output is not None else ""
        result_output += "\n\n**Вывод:**\n```{}```".format(escape(result).rstrip('\n')) if result else ""
        result_output += "\n\n**Ошибка:**\n```{}```".format(escape(error).rstrip('\n')) if error else ""

        await msg.edit(result_output)

    elif 3900 < len(str(output)) < 40000:
        await msg.edit(f"**Код:**```\n{escape(args)}```\n\n"f"**Возвращено:**\n```{str(output)[:3900]}```")
        async for i in slicer(str(output)[3900:], 3900):
            await msg.reply(f"```{i}```")
    else:
        await msg.edit(f"**Код:**```\n{escape(args)}```\n\n"f"**Возвращено:**\n```MESSAGE_TOO_LONG```")


async def getattrs(app, msg):
    return {
            "reply": msg.reply_to_message,
            "msg": msg,
            "app": app,
            "chat": msg.chat,
            "message": msg,
            "client": app,
            "input": CustomInput(app, msg)
            }
