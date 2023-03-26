import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters
from formatters import time_to_seconds

que = {}
SESSION_NAME = getenv("SESSION_NAME", "")

BOT_TOKEN = getenv("BOT_TOKEN", "")

BOT_NAME = getenv("BOT_NAME")

admins = {}
API_ID = int(getenv("API_ID", ""))

API_HASH = getenv("API_HASH", "")

BOT_USERNAME = getenv("BOT_USERNAME", "")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split( ))

BANNED_USERS = filters.user()

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "60")
)  # Remember to give value in Minutes

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)  # Remember to give value in Minutes

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)
