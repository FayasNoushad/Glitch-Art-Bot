import os
import glitchart
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FayasNoushad = Client(
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

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True
    )

@FayasNoushad.on_message(filters.private & filters.photo)
async def glitchart(bot, update):
    download_location = ".DOWNLOADS" + "/" + str(update.from_user.id) + "/" + ".jpg"
    message = await update.reply_text("`Processing...`")
    try:
        await update.download(
            message=update,
            file_name=download_location
        )
    except Exception as error:
        print(error)
        await message.edit_text(
            text="Something wrong. Contact @TheFayas."
        )
        return
    try:
        glitchart = glitchart.jpeg(download_location)
        await update.reply(glitchart)
        os.remove(download_location)
    except Exception as error:
        print(error)
        await message.edit_text(
            text="Something wrong. Contact @TheFayas."
        )
        return
    await message.delete()

FayasNoushad.run()
