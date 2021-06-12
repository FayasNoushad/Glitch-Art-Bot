import os
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
    message = await update.reply_text("`Processing...`")
    medianame = "./DOWNLOADS/" + str(update.from_user.id) + "/glitchart.jpeg"
    try:
        await update.download(file_name=medianame)
    except Exception as error:
        print(error)
        await message.edit_text("Something wrong. Contact @TheFayas.")
        return
    try:
        glitchart = glitchart.jpeg(medianame)
        try:
            await os.remove(medianame)
        except:
            pass
        video = await update.reply_video(glitchart)
    except Exception as error:
        print(error)
        try:
            await os.remove(medianame)
        except:
            pass
        await message.edit_text("Something wrong. Contact @TheFayas.")
        return
    await message.delete()

FayasNoushad.run()
