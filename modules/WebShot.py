from asyncio import sleep

from pyrogram import Client, filters, types
 
class Info:
    desc = "Скрин по ссылке" # auto generated line. Old line: des = 'Скрин по ссылке'
    short_desc = "[Инструменты] web" # auto generated line. Old line: in_help = 'web'
    commands = {
        ".web [link]": "<https://wttr.in/CITY?m?M?0?q?T&lang=ru> Делает скрин по ссылке"
    } # auto generated line. Old line: cmd_list = {'web': '<https://wttr.in/CITY?m?M?0?q?T&lang=ru> Делает скрин по ссылке'}
    author = "Придумал @xllzevs, а реализовал @youngtitanium"
  
 
@Client.on_message(filters.command('web', prefix) & filters.me) 
async def webshot(client, message: types.Message):
    if len(message.text.split()) > 1:
        resource = message.text.split(maxsplit=1)[1]
    elif message.reply_to_message:
        resource = message.reply_to_message.text
    else:
        await message.edit("Вы не указали ссылку.")
        return
        
    await message.edit("Делаю скрин...")
    await sleep(2)
    link = f'https://shot.screenshotapi.net/screenshot?token=0FX99SN-RBH4W01-NS6TX0D-QAJ9NMW&url={resource}&width=1024&height=720&output=image&file_type=png&wait_for_event=load'
    await message.reply_photo(link)
    await message.delete()
