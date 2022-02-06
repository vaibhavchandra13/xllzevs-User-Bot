from uuid import uuid4
from importlib import import_module

import importlib
from pyrogram import Client, filters
import os
import subprocess
import asyncio

import re

class Info:
    short_desc = "[Инструменты] Менеджмент плагинов."
    desc = (
        "Этот плагин является основным. От него зависит:\n"
        "Установка/Удаление/Переименование/"
        "Восстановление/Отправка/"
        "Получение справки модулей"
        )
    version = 3.2
    author = "@youngtitanium(отредактировал @xllzevs)"
    commands = {
         "плагины": "Получить список плагинов с документацией.",
         "помощь [modulename]": "Получить справку о плагине или о боте.",
         "установить [custom_modulename]": "Установка плагина.",
         "удалить [modulename]": "Удаление плагины.",
         "удаленные": "Получить список удалённых плагинов.",
         "восстановить [modulename]": "Восстановить удалённый плагин.",
         "drop [modulename]": "Поделиться плагином.",
         "переименовать [modulename] [название которое хотите]": "Переименовывает плагин.",
         "логи": "Получить файл(errors.txt) с логами."
    }

def modules_list():
    return [
        name[:-3] for name in os.listdir("modules")
        if name.endswith(".py") and not name.startswith("_")
    ]

def persuade(number):
    variants = ("хандлер", "хандлера", "хандеров")
    if number%100//10 == 1:
        return variants[2]
    units = number%10
    if units == 0 or units > 4:
        return variants[2]
    elif units > 1:
        return variants[1]
    else:
        return variants[0]

def deleted_modules_list():
    return [
        name[:-3] for name in os.listdir("deleted")
        if name.endswith(".py")
    ]

def random_name():
    return "py"+str(uuid4()).replace("-", "_")+".py"

def get_modules_with_docs() -> dict:
    module_names = [
        name[:-3]
        for name in os.listdir("modules")
        if name.endswith(".py") and not name.startswith("_")
        ]
    modules = {
        name: {
            key: value
            for key, value in getattr(
                getattr(
                    import_module(
                        f"modules.{name}"
                        ),
                    "Info",
                    object
                ),
                "__dict__", {}
            ).items()
            if not key.startswith("_")
            }
        for name in sorted(module_names)
        }
    return modules

@Client.on_message(filters.me & filters.regex('^помощь',re.I))
async def get_help(_, message):
    if len(message.text.split()) < 2:
        await message.edit("Где имя модуля?")
        return
    module_name = message.text.split(maxsplit=1)[1].replace(" ", "_")
    module = get_modules_with_docs().get(module_name)
    if module:
        await message.edit(
           f"Имя: {module_name}\n"
           f"Автор: {module.get('author', 'Неизвестно')}\n"
           f"Версия: {module.get('version', '1.0')}\n"
           f"Описание:\n{module.get('desc', 'Отсутствует')}\n\n"
           "Команды:\n" + "\n\n".join(
               [
                  f" • <code>{command}</code> — {desc}"
                  for command, desc in module.get("commands", {}).items()
                  ]
               )
           )
    else:
        await message.edit(
           "2 варианта:\n1.У тебя нету такого модуля.\n2.У тебя есть такой модуль но у него нету документации."
           )


@Client.on_message(filters.me & filters.regex('^модули',re.I))
async def get_modules(_, msg):
    modules = get_modules_with_docs()
    text = "Рабочие модули:\n"
    count_of_modules = 0
    for name, module in modules.items():
        if len(module) < 1:
            continue
        short_description = module.get("short_desc", "")
        version = module.get("version", 1.0)
        commands = module.get("commands", {})
        if len(short_description) < 1:
            short_description = "|".join(commands.keys())
        text += f"<code>{name}</code>[{version}] — <i>{short_description}</i>\n"
        count_of_modules += 1
    text += f"Всего модулей с документацией: {count_of_modules}"
    await msg.edit(text)

@Client.on_message(filters.reply & filters.me & filters.regex('^установить',re.I))
async def load(app, message):
    name = message.reply_to_message.document.file_name
    if len(message.command) > 1:
        name = "_".join(message.text.split(" ")[1:]) + ".py"
    doc = message.reply_to_message.document.file_id
    await message.edit("Проверка модуля на работоспособность...")
    await app.download_media(message=doc, file_name=f"modules/{name}")
    try:
        with open(f"modules/{name}", encoding="utf8") as f:
            code = f.read()
        exec(code)
    except Exception as e:
        await message.edit(f"{e}")
        os.remove(f"modules/{name}")
        return
    module = importlib.import_module(f"modules.{name[:-3]}")
    handlers = len(list(filter(lambda x: hasattr(x, "handlers"), vars(module).values())))
    await message.edit(
       "Модуль <code>{}</code> успешно успешно прошел проверку на работоспособность и им можно пользываться\n"
       "Добавлен{} {} {}".format(
          name,
          'о' if handlers != 1 else '',
          handlers,
          persuade(handlers)
          ),
        parse_mode="HTML"
        )
    await app.restart(False)


@Client.on_message(filters.me & filters.regex('^удалить',re.I))
async def delete_module(app, msg):
    if len(msg.text.split()) < 2:
        await msg.reply(
            "Где имя модуля?"
            )
        return
    name = msg.command[1].replace(" ", "_")
    if name in modules_list():
        subprocess.run(["mv",f'modules/{name}.py', 'deleted/'], check=True)
        await msg.edit("Вы выкинули модуль `{}` в мусорку!".format(name))
        await app.restart(False) 
    else:
        await msg.edit(f"Модуль `{name}` не найден!")
        await asyncio.sleep(5)
        await msg.delete()

@Client.on_message(filters.me & filters.regex('^drop',re.I))
async def send_main(app, message):
    if len(message.text.split()) < 2:
        await message.reply(
            "Где имя модуля?"
            )
    name = message.text.split(" ", 1)[1]
    if name.endswith(".py"):
        name = name[:-3]
    if not name+".py" in os.listdir("./modules"):
        await message.edit(
            f"Модуль <code>{name}</code> не найден!",
            parse_mode="HTML"
            )
        await asyncio.sleep(10)
        await message.delete()
        return
    text = f"Отправка модуля <code>{name}</code>\n"
    await message.edit(text, parse_mode="HTML")
    await app.send_document(message.chat.id, document = f"modules/{name}.py")
    text = f"Модуль <code>{name}</code> отправлен!"
    await message.edit(text, parse_mode="HTML")
    await asyncio.sleep(10)
    await message.delete()

@Client.on_message(filters.me & filters.regex('^переименовать',re.I))
async def module_renamer(app, message):
    _, stock, name = message.text.split(" ", 2)
    if stock in modules_list():
        os.rename(f"modules/{stock}.py", f"modules/{name}.py")
        await message.edit("Модуль переименован!" )
        await app.restart(False)
    else:
        await message.edit("Модуль не существует!")

@Client.on_message(filters.me & filters.regex('^восстановить',re.I))
async def recovery_modules(app,msg):
    try:
        name = msg.text.split(" ",1)[1].replace(" ","_")
        if name in deleted_modules_list():
            subprocess.run(['mv', f'deleted/{name}.py', 'modules/'], check=True)
            await msg.edit(f"Вы дастали модуль `{name}` с мусорки!")
            await app.restart(False)
        else:
            await msg.edit("Такого модуля нету в мусорке")
    except Exception as e:
        await msg.edit(f"__{e}__")

@Client.on_message(filters.me & filters.regex('^удаленные',re.I))
async def delete_list(_, msg):
    text = "**Мусорка:**\n"
    for name in deleted_modules_list():
        text += f'➜ `{name}`\n'
    await msg.edit(text)
    
@Client.on_message(filters.me & filters.regex('^логи',re.I))
async def send_logs(app, msg):
    try:
        await app.send_document(msg.chat.id, "errors.txt")
    except:
        await msg.edit("<b>Ошибок нет</b>")
    with open("errors.txt", "w+") as file:
        file.write("")
    await asyncio.sleep(3)
    await msg.delete()
