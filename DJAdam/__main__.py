import requests
from pyrogram import Client as Bot
from pytgcalls import idle

from DaisyXMusic.config import API_HASH, API_ID, BOT_TOKEN
from DaisyXMusic.services.pytgcalls import run

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="DJAdam.modules"),
)

bot.start()
run()
idle()
