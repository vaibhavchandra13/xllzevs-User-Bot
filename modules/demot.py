from pyrogram import Client, filters
from pyrogram import types

from PIL import Image, ImageDraw, ImageFont, ImageChops
import imageio
import requests
import io, os, sys


#sys

#

#

#__module_info__ = {

#    'name': 'Demotivator',

#    'author': ['pelmeshke', '@pelmeshke'],

#    'version': 'v1.0',

#    'description': 'Creates demotivator from photo with caption (try it yourself to understand). Also creates "slavik meme"',

#    'commands': {

#        '.demot': {

#            'desc': 'Creating demotivator. As photo also takes gifs, stickers, video or user\'s photo. As caption takes text in command or photo\'s caption',

#            'func': 'command([\'demot\'], \'.\')'

#        },

#        '.slavik': {

#            'desc': 'Creating slavik meme. As photo also takes gifs, stickers, video or user\'s photo. As caption takes text in command or photo\'s caption',

#            'func': 'command([\'slavik\'], \'.\')'

#        },

#

#    },

#    'dependencies': ['PIL (or Python Image Library)', 'requests (for fonts)', 'imageio (for converting mp4 to gif)'],

#    'requirements':


class Info:
    short_desc = "[Развлекательный] Модуль для создания демотиватора и славик мема."
    desc = (
        "Создает демотиватор из фотографии с подписью (попробуйте сами разобраться). Также создает 'slavik name'. Создатель @pelmeshke.\n"
        "Требования: PIL; imageio"
        )
    version = 1.0
    author = "@pelmeshke"
    commands = {
       ".demot": "Генерировать демотиватор.",
       ".slavik": "Генерировать Славик мем."
    }
    


@Client.on_message(filters.me & filters.reply & filters.command('demot', '.'))
async def demotivator_handler(app, message):
    photo = message.reply_to_message.photo or \
            message.reply_to_message.sticker or \
            message.reply_to_message.animation or \
            message.reply_to_message.video or \
            message.reply_to_message.video_note or \
            message.reply_to_message.forward_from and \
            message.reply_to_message.forward_from.photo.big_file_id or \
            message.reply_to_message.from_user.photo.big_file_id

    await message.edit_text('🔄<b>Скачиваю фото</b>🔄')
    photo_path = await app.download_media(photo)

    caption = ' '.join(message.text.split(' ')[1:]) or \
              message.reply_to_message.text or \
              message.reply_to_message.caption or \
              'ГДЕ ПОДПИСЬ, БЛЯДЬ!!!'
    caption = '\n'.join([line.strip() for line in caption.split("\n")])
    await message.edit_text('🔄<b>Фотожоплю</b>🔄')

    if photo_path.endswith('.mp4'):
        gif_path = await convert_file(photo_path)
        out = await demotivator_gif(gif_path, caption)
        os.remove(photo_path)
        photo_path = gif_path
    elif photo_path.endswith('.gif'):
        out = await demotivator_gif(photo_path, caption)
    else:
        out = await demotivator(photo_path, caption)

    await message.edit_text('🔄<b>Отправляю</b>🔄')
    if photo_path.endswith('.gif'):
        await message.reply_to_message.reply_animation(out)
    else:
        await message.reply_to_message.reply_photo(out)

    await message.delete()
    os.remove(photo_path)

@Client.on_message(filters.me & filters.reply & filters.command('slavik', '.'))
async def slavik_handler(peluserbot, message):
    photo = message.reply_to_message.photo or \
            message.reply_to_message.sticker or \
            message.reply_to_message.animation or \
            message.reply_to_message.video or \
            message.reply_to_message.video_note or \
            message.reply_to_message.forward_from and \
            message.reply_to_message.forward_from.photo.big_file_id or \
            message.reply_to_message.from_user.photo.big_file_id

    await message.edit_text('🔄<b>Скачиваю фото</b>🔄')
    photo_path = await peluserbot.download_media(photo)

    caption = ' '.join(message.text.split(' ')[1:]) or \
              message.reply_to_message.text or \
              message.reply_to_message.caption or \
              'ГДЕ ПОДПИСЬ, БЛЯДЬ!!!'
    caption = "\n".join([line.strip() for line in caption.split("\n")])

    await message.edit_text('🔄<b>Фотожоплю</b>🔄')

    if photo_path.endswith('.mp4'):
        gif_path = await convert_file(photo_path)
        out = await slavik_gif(gif_path, caption)
        os.remove(photo_path)
        photo_path = gif_path
    elif photo_path.endswith('.gif'):
        out = await slavik_gif(photo_path, caption)
    else:
        out = await slavik(photo_path, caption)

    await message.edit_text('🔄<b>Отправляю</b>🔄')
    if photo_path.endswith('.gif'):
        await message.reply_to_message.reply_animation(out)
    else:
        await message.reply_to_message.reply_photo(out)

    await message.delete()
    os.remove(photo_path)




SIZE = (2160, 2160)
GIF_SIZE = (480, 480)

async def demotivator(path, caption):
    image = Image.open(path)

    black_image = Image.new('RGB', SIZE, (0, 0, 0))

    image = image.resize((int(SIZE[0]*.8), int(SIZE[1]*.7)))

    black_image.paste(image, (int(SIZE[0]*.1), int(SIZE[1]*0.05)))

    txt = Image.new("RGB", black_image.size, (0, 0, 0))

    font = requests.get('https://github.com/pelmesh619/fonts/blob/main/TimesNewRoman.ttf?raw=true').content
    font = ImageFont.truetype(io.BytesIO(font), SIZE[1]//20)

    d = ImageDraw.Draw(txt)

    text_xy = d.multiline_textsize(caption, font=font)
    text_xy = (SIZE[0] - text_xy[0]) // 2, (SIZE[1]*0.25 - text_xy[1]) // 2 + SIZE[1]*0.75

    d.multiline_text(text_xy, caption, font=font, fill=(255, 255, 255), align='center')

    lines_xy = (
        int(SIZE[0]*.1 - SIZE[0]*.01), 
        int(SIZE[0]*.9 + SIZE[0]*.01), 
        int(SIZE[1]*0.05 - SIZE[1]*0.01), 
        int(SIZE[1]*0.75 + SIZE[1]*0.01),
    )

    d.line(
        ((lines_xy[0], lines_xy[2]), (lines_xy[0], lines_xy[3])),
        width=int(SIZE[0]*.005)
    )
    d.line(
        ((lines_xy[1], lines_xy[2]), (lines_xy[1], lines_xy[3])),
        width=int(SIZE[0]*.005)
    )
    d.line(
        ((lines_xy[0], lines_xy[2]), (lines_xy[1], lines_xy[2])),
        width=int(SIZE[0]*.005)
    )
    d.line(
        ((lines_xy[0], lines_xy[3]), (lines_xy[1], lines_xy[3])),
        width=int(SIZE[0]*.005)
    )

    out = ImageChops.add(black_image, txt)

    output = io.BytesIO()
    output.name = 'demot.png'
    out.save(output, "PNG")
    output.seek(0)

    return output


async def demotivator_gif(path, caption):
    gif = Image.open(path)
    #print(path, gif.format, gif.is_animated, gif.tell(), gif.tell(), gif.n_frames, gif.size)

    font = requests.get('https://github.com/pelmesh619/fonts/blob/main/TimesNewRoman.ttf?raw=true').content
    font = ImageFont.truetype(io.BytesIO(font), GIF_SIZE[1]//20)

    images = []

    black_image = Image.new('RGBA', GIF_SIZE, (0, 0, 0))
    txt = Image.new("RGBA", black_image.size, (0, 0, 0))
    d = ImageDraw.Draw(txt)

    text_xy = d.multiline_textsize(caption, font=font)
    text_xy = (GIF_SIZE[0] - text_xy[0]) // 2, (GIF_SIZE[1]*0.25 - text_xy[1]) // 2 + GIF_SIZE[1]*0.75

    lines_xy = (
        int(GIF_SIZE[0]*.1 - GIF_SIZE[0]*.01), 
        int(GIF_SIZE[0]*.9 + GIF_SIZE[0]*.01), 
        int(GIF_SIZE[1]*0.05 - GIF_SIZE[1]*0.01), 
        int(GIF_SIZE[1]*0.75 + GIF_SIZE[1]*0.01),
    )
    d.multiline_text(text_xy, caption, font=font, fill=(255, 255, 255), align='center')

    d.line(((lines_xy[0], lines_xy[2]), (lines_xy[0], lines_xy[3])), width=int(GIF_SIZE[0]*.005))
    d.line(((lines_xy[1], lines_xy[2]), (lines_xy[1], lines_xy[3])), width=int(GIF_SIZE[0]*.005))
    d.line(((lines_xy[0], lines_xy[2]), (lines_xy[1], lines_xy[2])), width=int(GIF_SIZE[0]*.005))
    d.line(((lines_xy[0], lines_xy[3]), (lines_xy[1], lines_xy[3])), width=int(GIF_SIZE[0]*.005))

    for i in range(gif.n_frames):
        gif.seek(i)
        image = gif.convert('RGBA')
        image = image.resize((int(GIF_SIZE[0]*.8), int(GIF_SIZE[1]*.7)))

        black_image_copy = black_image.copy()
        black_image_copy.paste(image, (int(GIF_SIZE[0]*.1), int(GIF_SIZE[1]*0.05)))

        out = ImageChops.add(black_image_copy, txt)
        # if i % 100 == 0:
        #     out.show()

        images.append(out)

    out = io.BytesIO()
    out.name = 'demot.gif'
    images[0].save(out, 'GIF', save_all=True, append_images=images[1:], optimize=True)

    #print('done')
    return out

async def slavik(path, caption):
    image = Image.open(path)
    d = ImageDraw.Draw(image)

    font_file = requests.get('https://github.com/pelmesh619/fonts/blob/main/Lobster.ttf?raw=true').content
    
    i = image.size[1]//12
    while i > 0:
        font = ImageFont.truetype(io.BytesIO(font_file), i)
        text_xy = d.multiline_textsize(caption, font=font)

        if text_xy[0] < image.size[0] * .9:
            break
        i -= 2

    text_xy = (image.size[0] - text_xy[0]) // 2, image.size[1] - image.size[1] // 8
    d.multiline_text((text_xy[0]+1, text_xy[1]+1), caption, font=font, fill=(0, 0, 0), align='center')
    d.multiline_text(text_xy, caption, font=font, fill=(255, 255, 255), align='center')

    out = io.BytesIO()
    out.name = 'slavik.png'
    image.save(out, "PNG")
    out.seek(0)
    
    #print('done')
    return out


async def slavik_gif(path, caption):
    gif = Image.open(path)
    size = gif.size

    font_file = requests.get('https://github.com/pelmesh619/fonts/blob/main/Lobster.ttf?raw=true').content

    images = []

    for i in range(gif.n_frames):
        gif.seek(i)
        image = gif.convert('RGBA')

        d = ImageDraw.Draw(image)
        
        if i == 0:
            j = size[1]//10
            while j > 0:
                font = ImageFont.truetype(io.BytesIO(font_file), j)
                text_xy = d.multiline_textsize(caption, font=font)

                if text_xy[0] < size[0] * .9:
                    break
                j -= 2

            text_xy = (size[0] - text_xy[0]) // 2, size[1] - size[1] // 7
        d.multiline_text((text_xy[0]+1, text_xy[1]+1), caption, font=font, fill=(0, 0, 0), align='center')
        d.multiline_text(text_xy, caption, font=font, fill=(255, 255, 255), align='center')

        images.append(image)

    out = io.BytesIO()
    out.name = 'slavik.gif'
    images[0].save(out, 'GIF', save_all=True, append_images=images[1:], optimize=True)

    #print('done')

    return out

async def convert_file(inputpath):
    """Reference: http://imageio.readthedocs.io/en/latest/examples.html#convert-a-movie"""
    outputpath = os.path.splitext(inputpath)[0] + '.gif'

    reader = imageio.get_reader(inputpath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputpath, fps=fps)
    for im in reader:
        writer.append_data(im)
    writer.close()
    return outputpath
