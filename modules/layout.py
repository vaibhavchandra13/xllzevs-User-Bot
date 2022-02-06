from pyrogram import Client as app, filters


class Info:
    desc = "Изменение раскладки с en в rus и наоборот."
    short_desc = "[Разное] Изменение раскладки."
    author = "@AIDS_company(Переделал: @youngtitanium)"
    version = "2.0.3"
    commands = {
		".trl/.аой (в ответ)" : "Переводит текст."
	}

MK = {"!": "!","@": '"',"#": "№","$": ";","%": "%","^": ":","&": "?","*": "*","(": "(",")": ")","q": "й","w": "ц","e": "у","r": "к","t": "е","y": "н","u": "г","i": "ш","o": "щ","p": "з","[": "х","]": "ъ","`": "ё","a": "ф","s": "ы","d": "в","f": "а","g": "п","h": "р","j": "о","k": "л","l": "д",";": "ж","'": "э","z": "я","x": "ч","c": "с","v": "м","b": "и","n": "т","m": "ь",",": "б",".": "ю","/": "."," ": " ",      "Q": "Й","W": "Ц","E": "У","R": "К","T": "Е","Y": "Н","U": "Г","I": "Ш","O": "Щ","P": "З","A": "Ф","S": "Ы","D": "В","F": "А","G": "П","H": "Р","J": "О","K": "Л","L": "Д","Z": "Я","X": "Ч","C": "С","V": "М","B": "И","N": "Т","M": "Ь"}
MK_reverse = {v: k for k, v in MK.items()}
@app.on_message (filters.me & filters.command("аой", ""))
@app.on_message(filters.me & filters.command("trl", "."))
async def translate(_, msg):   
    if not msg.reply_to_message:
    	await msg.edit(
    		"Чё? Где мой реплай?"
    		)
    	return
    if len(msg.text.split()) > 1:
        if "-r" in msg.text or "-р" in msg.text:
            await msg.edit("".join([MK_reverse[char] if char in MK_reverse else char for char in msg.reply_to_message.text]))
            return
    await msg.edit("".join([MK[char] if char in MK else char for char in msg.reply_to_message.text])) 
