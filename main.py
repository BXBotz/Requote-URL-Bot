# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/FayasNoushad/Requote-URL-Bot/blob/main/LICENSE

import os
from requests.utils import requote_uri
from pyrogram import Client, filters


Bot = Client(
    "Requote-URL-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


@Bot.on_message(filters.text)
async def filter(bot, update):
    await update.reply_text(
        text=f"`{requote_uri(update.text)}`\n\nMade by @FayasNoushad",
        disable_web_page_preview=True,
        quote=True
    )


Bot.run()
