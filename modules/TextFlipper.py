from pyrogram import Client, filters


class Info:
    short_desc = "[Развлекательный] Переворачивает текст после команды вверх ногами."
    desc = "Переворачивает текст после команды вверх ногами."
    version = 0.7
    commands = {".flip [text(только на англ)]": "Переворачивает текст вверх ногами."}
    author = "@xllzevs"


REPLACEMENT_MAP = {
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ᴉ",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "B",
    "C": "Ɔ",
    "D": "D",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "K",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    "0": "0",
    "1": "Ɩ",
    "2": "ᄅ",
    "3": "Ɛ",
    "4": "ㄣ",
    "5": "ϛ",
    "6": "9",
    "7": "ㄥ",
    "8": "8",
    "9": "6",
    ",": "'",
    ".": "˙",
    "?": "¿",
    "!": "¡",
    '"': ",,",
    "'": ",",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    "&": "⅋",
    "_": "‾",
}


@Client.on_message(filters.command("flip", prefixes=".") & filters.me)
async def flip(_, message):
    if len(message.text.split()) < 2:
        await message.edit("Вы не ввели текст")
        return
    text = message.text.split(maxsplit=1)[1]
    await message.edit("".join([c if c not in REPLACEMENT_MAP else REPLACEMENT_MAP[c] for c in text]))