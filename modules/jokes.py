from pyrogram import Client, filters
import requests
from bs4 import BeautifulSoup

import re

class Info:
    desc = "Поиск анекдотов в интернете."
    short_desc = "[Развлекательный] Парсит анекдоты: .joke"
    author = "@AIDS_company (переделал: @youngtitanium)"
    commands = {".joke": "Парсит анекдоты."}
    version = 2.0
    
class storage:
    jokes = []
 
storage = storage()
def parse():
    # Сайт с анекдотами
    url = "https://nekdo.ru/random/"
    # Кастомные хедеры, для того чтобы
    # сайт думал что мы заходим через браузер
    headers = {
        'User_agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 YaBrowser/20.3.0.1223 Yowser/2.5 Safari/537.36'
    }
    # Делаем запрос
    response = requests.get(url, headers = headers)
    # Поиск анекдотов в результате запроса
    soup = BeautifulSoup(response.content, 'html.parser').find('body', class_='main').find('div',class_='content').findAll('div',class_='text')
    for i in soup: 
        # Записываем все анекдоты
        storage.jokes.append(i.text)

@Client.on_message(filters.me & filters.regex('^анекдот',re.I))
async def get_joke(_, msg): 
    if len(storage.jokes) < 1:
        await msg.edit("Парсим анекдоты...")
        parse()
    await msg.edit(storage.jokes[0])
    storage.jokes.pop(0)