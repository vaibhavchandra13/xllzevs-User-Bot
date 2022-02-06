from pyrogram import Client, filters
import io
import os
from PIL import Image, ImageFont, ImageDraw
import requests
import textwrap

class Info:
    short_desc = desc = "[Развлекательный] Генерировать цитату."
    commands = {"qu": desc}

@Client.on_message(filters.me & filters.command('qu', prefix))
async def mqcmd(peluserbot, message):
    """.mq <реплай на текст>"""
    bw = False if message.text.split()[1:] else True
    reply = message.reply_to_message
    if not reply and not reply.text:
        await message.edit_text("<b>Ответь командой на умную цитату!</b>")
        return
    
    pfp = message.reply_to_message.from_user.photo
    await message.edit_text("<i>И сказал этот гений...</i>")
    if not pfp:
        pfp = b'BM:\x00\x00\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\x04\x00\x00\x00\xc4\x0e\x00\x00\xc4\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\x00'
    else:
        file_path = '/'.join(__file__.split('/')[:-1]+[f'{message.from_user.id}.png'])
        await peluserbot.download_media(pfp.big_file_id, 
            file_name=file_path
        )
        pfp = open(file_path, 'rb').read()
        os.remove(file_path)
    text = "\n".join(textwrap.wrap(reply.text, 30))
    text = "“"+text+"„"
    bf = requests.get("https://raw.githubusercontent.com/KeyZenD/l/master/times.ttf").content
    font = ImageFont.truetype(io.BytesIO(bf), 50)

    im = Image.open(io.BytesIO(pfp))
    if bw:
        im = im.convert("L")
    im = im.convert("RGBA").resize((1024, 1024))
    w, h = im.size
    w_, h_ = 20*(w//100), 20*(h//100)
    im_ = Image.new("RGBA", (w-w_, h-h_), (0, 0, 0))
    im_.putalpha(150) 
    im.paste(im_, (w_//2, h_//2), im_)
    draw = ImageDraw.Draw(im)
    _w, _h = draw.textsize(text=text, font=font)
    x, y = (w-_w)//2, (h-_h)//2
    draw.text((x, y), text=text, font=font, fill="#fff", align="center")
    output=io.BytesIO()
    im.save(output, "PNG")
    output.seek(0)
    output.name = 'genius.png'
    await peluserbot.send_photo(message.chat.id, photo=output)
    await message.delete()
        
