import asyncio

from pyrogram import Client as app, filters
from youtube_search import YoutubeSearch


class Info:
	short_desc = "[Поиск] Поиск в Google."
	desc = "Модуль для поиска в Google."
	version = "1.7"
	commands = {".google|.гугл|.поиск [запрос]"}
	author = "@youngtitanium"

@app.on_message(filters.me & filters.command("поиск", "."), group=666)
@app.on_message(filters.me & filters.command("гугл", "."), group=667)
@app.on_message(filters.me & filters.command("google", "."), group=668)
async def search(_, message):
	text = message.text or message.caption
	if len(text.split()) < 2:
		await asyncio.sleep(0.3)
		await message.edit(text="google.com")
		return
	query = text.split(maxsplit=1)[1]
	if ":youtube:" in query:
		response = YoutubeSearch(query.replace(":youtube:", ""), max_results=3).to_dict()
		await message.edit(
			text="\n\n".join(
			[
				f"<a href=\"youtube.com/{video['url_suffix']}\">{video['title']}</a>"
				for video in response
				]
			),
			parse_mode="HTML"
		)
		return
	await asyncio.sleep(0.3)
	await message.edit(
		text=f"<a href=\"google.com/search?q={'+'.join(query.split())}\">{query.title()}</a>",
		parse_mode="HTML"
		)