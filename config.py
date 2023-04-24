import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters
from formatters import time_to_seconds

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQD8ElsAizFtPk4BDcidEtnbRYvQOaPe3Rju--BkBJTR3eqUHwGLC5omE8DaUUKBE8bQGRI3iWyacBbMcbQgV9EoknwflusVKf7mpATndZLnaCJRsesRwuBPsRoaJ_UU0Q3xYY8rv6B1z-xITwM4HSnNge1JfeR1xetlcl3NfTRvz761WtHWfJEey4GHwN4qSv84cXL31IpbU20pkcOHcn1bEjv18H3sz8MQ24i4qaGtjLxthc50-cViYVZd969l9VFPTjXWvAQ6PdH8N3tuOAuch5ihfayBa_htytHi8DRsLqNRpFmBWZIZDguu0pL0QBJO94pB6_3W3Ph1PnLDYB8nOGET8AAAAAFvehzpAQ")

BOT_TOKEN = getenv("BOT_TOKEN", "6165241065:AAHPgX6HbVbu2fceDToVKFwAa9g1aFs_6Z4")

BOT_NAME = getenv("BOT_NAME")

admins = {}
API_ID = int(getenv("API_ID", "16519771"))

API_HASH = getenv("API_HASH", "83754b17b54fe9d6a602e70c458afddb")

BOT_USERNAME = getenv("BOT_USERNAME", "Unique_Adam_Bot")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split( ))

BANNED_USERS = filters.user()

# Custom max audio(music) duration for voice chat. set DURATION_LIMIT in variables with your own time(mins), Default to 60 mins.
DURATION_LIMIT_MIN = int(
    getenv("DURATION_LIMIT", "70")
)  # Remember to give value in Minutes

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")
)  # Remember to give value in Minutes

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001796731397"))

OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5909153311").split())
)

START_IMG_URL = getenv("START_IMG_URL", "AgACAgUAAxkBAAIELmQ-twABOFJ_6-ffmhfZNW1npvWxwgAC77MxG3M7-VV4045r_WGiLgAIAQADAgADeAAHHgQ")

GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/Pravartak/TgCallBot")