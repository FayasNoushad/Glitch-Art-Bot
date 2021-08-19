# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
import glitchart
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
    "Glitch-Art-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """
Hello {}, I am a photo to glitch art telegram bot.

Made by @FayasNoushad
"""
START_BUTTONS = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton('Channel', url='https://telegram.me/FayasNoushad'),
        InlineKeyboardButton('Feedback', url='https://telegram.me/TheFayas')
    ]]
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True
    )

@Bot.on_message(filters.private & filters.photo)
async def glitch_art(bot, update):
    download_path = "./DOWNLOADS" + "/" + str(update.from_user.id) + "/"
    download_location = download_path + "photo.jpg"
    message = await update.reply_text(
        text="`Processing...`"
    )
    try:
        await update.download(
            file_name=download_location
        )
    except Exception as error:
        print(error)
        await message.edit_text(
            text="Something wrong. Contact @TheFayas."
        )
        return 
    await message.edit_text(
        text="`Converting to glitch...`"
    )
    try:
        glitch_art = glitchart.jpeg(download_location)
        glitch_art_path = download_path + "glitchart.jpg"
        with open(glitch_art_path, "wb") as file:
            file.write(glitch_art)
        await update.reply_photo(photo=glitch_art_path, quote=True)
        os.remove(download_location)
        os.remove(glitch_art_path)
    except Exception as error:
        print(error)
        await message.edit_text(
            text="Something wrong. Contact @TheFayas."
        )
        return
    await message.delete()


Bot.run()
