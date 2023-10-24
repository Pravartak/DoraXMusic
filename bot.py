import os
import asyncio
import sys
from datetime import datetime, timedelta
from typing import Union

from pyrogram import Client
from pyrogram.types import (BotCommand, InlineKeyboardMarkup, InlineKeyboardButton)
from pyrogram.errors import (ChatAdminRequired, UserAlreadyParticipant, UserNotParticipant)
import pytgcalls
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (AlreadyJoinedError, NoActiveGroupCall, TelegramServerError)
import config

############Log Section############
import logging
from logging.handlers import RotatingFileHandler

LOG_FILE_NAME = "Quackylogs.txt"

logging.basicConfig(
	level = logging.INFO,
	format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
	datefmt="%d-%b-%y %H:%M:%S",
	handlers = [
		RotatingFileHandler(
			LOG_FILE_NAME, maxBytes=5000000, backupCount=10
		),
		logging.StreamHandler(),
	],
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

def LOGGER(name: str) -> logging.Logger:
	return logging.getLogger(name)
################################

class Dorabot(Client):
	def __init__(self):
		LOGGER(__name__).info(f"Booting up bot 🤖⚡")
		super().__init__(
			"DoraemonXMusic",
			api_id=config.API_ID,
			api_hash=config.API_HASH,
			bot_token=config.BOT_TOKEN
		)
	
	async def start(self):
		await super().start()
		get_me = await self.get_me()
		self.username = get_me.username
		self.id = get_me.id
		try:
			await self.send_message(
				config.LOG_GROUP_ID, f"Doraemon has successfully booted up.\n\nEnjoy Music!"
			)
			
		except:
			LOGGER(__name__).error(
				"Please add your bot to the Log Group, make it Admin and try again"
			)
		
		if config.SET_CMD == True:
			try:
				await self.set_bot_commands(
					[
						BotCommand("start", "Boot up the Bot"),
						BotCommand("ping", "Check Server Status"),
						BotCommand("help", "Get Help Menu"),
						BotCommand("settings", "Change Bot Settings"),
						BotCommand("reload", "Reload Bot Server"),
						BotCommand("play", "Play music"),
						BotCommand("vplay", "Play music with video"),
						BotCommand("cplay", "Play music in a Channel"),
						BotCommand("cvplay", "Play music video in a Channel"),
						BotCommand("skip", "Skip music"),
						BotCommand("cskip", "Skip music in Channel"),
						BotCommand("seek", "Seek forward a Second"),
						BotCommand("cseek", "Seek forward in Channel"),
						BotCommand("seekback", "Seek back a Second"),
						BotCommand("cseekback", "Seek back in Channel"),
						BotCommand("pause", "Pause music"),
						BotCommand("cpause", "Pause music in Channel"),
						BotCommand("resume", "Resume music"),
						BotCommand("cresume", "Resume music in Channel"),
						BotCommand("end", "End vc"),
						BotCommand("stop", "Stop music"),
						BotCommand("cstop", "Stop music in Channel"),
						BotCommand("playlist", "Get Playlist"),
						BotCommand("queue", "Check queue"),
						BotCommand("cqueue", "Check queue in Channel"),
						BotCommand("lyrics", "Get Lyrics of Songs"),
						BotCommand("song", "Download music"),
						BotCommand("video", "Download music video"),
						BotCommand("owner", "Know the Owner"),
						BotCommand("update", "Update the Bot"),
						BotCommand("stats", "Get Stats of the Bot")
					]
				)
			except:
				pass
		
		else:
			pass
		
		a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
		if a.status != "administrator":
			LOGGER(__name__).error(
				"Please make sure the Bot is Admin in the Log Group and try again"
			)
		if get_me.last_name:
			self.name = get_me.first_name + " " + get_me.last_name
		
		else:
			self.name = get_me.first_name
		
		LOGGER(__name__).info(f"Music Bot has started.\nName:- {self.name}")
		
		
