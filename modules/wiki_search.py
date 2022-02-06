from pyrogram import Client, filters
from bs4 import BeautifulSoup
import requests
import asyncio
import re


class Info:
	short_desc = "[Поиск] Поиск в вики педии."
	desc = "Модуль для поиска в вики педии."
	commands = {"Вики [запрос]"}
	author = "@xllevs"


@Client.on_message(filters.me & filters.regex('^вики',re.I), group = 4)
async def check_internet(app, msg):
	try:
		text = msg.text.split(maxsplit = 1)[1].replace(' ', '%20')
	except IndexError:
		text = msg.reply_to_message.text.replace(' ', '%20')
	url = f"https://ru.m.wikipedia.org/wiki/{text}"
	headers = {
		'User_agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 YaBrowser/20.3.0.1223 Yowser/2.5 Safari/537.36'
	}
	response = requests.get(url, headers = headers)
	soup = BeautifulSoup(response.content, 'html.parser')
	items = soup.findAll('div', class_ = 'content')
	wiki_list = []
	for item in items:
		wiki_list.append({
			'title' : item.find('p')
		})
	wiki = wiki_list[0]
	send_text = wiki['title']
	
	await msg.edit(u'**Результат:**\n\n{0}'.format(send_text))