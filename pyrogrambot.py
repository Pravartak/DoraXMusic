from __future__ import unicode_literals

import wolverine
from telegram import Chat, ChatMember, ChatMemberUpdated, Update
from telegram.ext import (
    Application,
    ChatMemberHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from typing import Optional, Tuple
from pyrogram import filters
from Adam import bot
import config
from help import (private_panel, help_panel)

@bot.on_message(
	filters.command('start')
	& filters.private) #Creating a command.

async def start_comm(bot, message):
    
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_panel()
            return await message.reply_text(
                "Here is a list of commands that you can use-\n\n/start - You can start the bot. you have used this already!\n\n/help - List of commands will appear, you have this one also!\n\n/photo - You will get some photos provided by @No_me_no_no. If you want to add more photos, just dm them to my owner.\n\n/song1 - Ghode Pe Sawar Song\n\n/song2 - Blinding Lights Song\n\n/song3 - Apna Bana Le Song\n\n/song4 - Kesariya Song\n\n/video1 - Ghode Pe Sawar Song Video\n\n/video2 - Baarishein Song Video\n\nYou can download songs too (Still in development)\n\nOwner will keep me updating and make sure I don't die.", reply_markup=keyboard
            )
    else:
        try:
            await bot.resolve_peer(peer_id(config.OWNER_ID[0]))
            
        except:
            OWNER = config.OWNER_ID[0]
        out = private_panel(config.BOT_USERNAME, OWNER)
        if config.START_IMG_URL:
            try:
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption="Hello! my name is Adam.\n\nI am a bot made for fun by my owner 😋, but I can download songs for you and I have already saved some songs and videos incase I get into some problems 😅.\n\n Please don't mind if I get offline, because I am constantly improving ❤️‍🩹, trying to get you new features 🫶.",
                    reply_markup=InlineKeyboardMarkup(out),
                )
            except:
                await message.reply_text(
                    "Hello! my name is Adam.\n\nI am a bot made for fun by my owner 😋, but I can download songs for you and I have already saved some songs and videos incase I get into some problems 😅.\n\n Please don't mind if I get offline, because I am constantly improving ❤️‍🩹, trying to get you new features 🫶.",
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await message.reply_text(
                "Hello! my name is Adam.\n\nI am a bot made for fun by my owner 😋, but I can download songs for you and I have already saved some songs and videos incase I get into some problems 😅.\n\n Please don't mind if I get offline, because I am constantly improving ❤️‍🩹, trying to get you new features 🫶.",
                reply_markup=InlineKeyboardMarkup(out),
            )

@bot.on_message(filters.command('help')) #Creating a command.
async def command2(bot, message): #Creating a function.
 keyboard = help_panel()
 return await message.reply_text("Here is a list of commands that you can use-\n\n/start - You can start the bot. you have used this already!\n\n/help - List of commands will appear, you have this one also!\n\n/photo - You will get some photos provided by @No_me_no_no. If you want to add more photos, just dm them to my owner.\n\n/song1 - Ghode Pe Sawar Song\n\n/song2 - Blinding Lights Song\n\n/song3 - Apna Bana Le Song\n\n/song4 - Kesariya Song\n\n/video1 - Ghode Pe Sawar Song Video\n\n/video2 - Baarishein Song Video\n\nYou can download songs too (Still in development)\n\nOwner will keep me updating and make sure I don't die.", reply_markup=keyboard) #Calling a method.
     
#Send_photo
@bot.on_message(filters.photo & filters.private)
def photo(Client, message):
     message.reply(message.photo.file_id)

@bot.on_message(filters.command('photo'))
async def command3(Client, message):
     await message.delete()
     await bot.send_photo(message.chat.id, "https://imgur.com/t/anime_wallpaper/QLRTXVL")
     await bot.send_photo(message.chat.id, "https://imgur.com/t/anime_wallpaper/toaUzHM")
     await bot.send_photo(message.chat.id, "AgACAgUAAxkBAAICRGQXNzrruA740MOfigY_mmE8EAURAAILuDEb1Bm4VD-ekA1wt9AGAAgBAAMCAAN4AAceBA")
     
#Send_audio
@bot.on_message(filters.audio & filters.private)
def audio(Client, message):
     message.reply(message.audio.file_id)
     
@bot.on_message(filters.command('song1'))
async def command4(Client, message):
     await message.delete()
     await bot.send_audio(message.chat.id, "CQACAgUAAxkBAAIBgGQUMVb6H3dT_peXVA-cbzXZQWKsAALoBwAClslJVHzxHobLNHdjHgQ")
@bot.on_message(filters.command('song2'))
async def command5(Client, message):
     await message.delete()
     await bot.send_audio(message.chat.id, "CQACAgUAAxkBAAIBgmQUMWMlYA2XRosCGB7rEqWziv2tAAJ7CAACGXGAVDj0md0qWrP1HgQ")
@bot.on_message(filters.command('song3'))
async def command6(Client, message):
     await message.delete()
     await bot.send_audio(message.chat.id, "CQACAgUAAxkBAAIBhGQUMWetYsPYaWPezYWJ3e8QYF-QAAJ8CAACGXGAVBv-niW895zIHgQ")
@bot.on_message(filters.command('song4'))
async def command7(Client, message):
     await message.delete()
     await bot.send_audio(message.chat.id, "CQACAgUAAxkBAAIBhmQUMWtJBuL9d9Z8-IiqAVd_NHMsAAJ9CAACGXGAVOeHnOpieonIHgQ")
     
#Send_video
@bot.on_message(filters.video & filters.private)
def video(Client, message):
     message.reply(message.video.file_id)
     
@bot.on_message(filters.command('video1'))
async def command8(Client, message):
     await message.delete()
     await bot.send_video(message.chat.id, "BAACAgUAAxkBAAIBiGQUMXNzwTHbS6FdRm1uGRPrTSH9AAJOCAAC2-1JVM5wXJQ5qiQmHgQ")
@bot.on_message(filters.command('video2'))
async def command9(Client, message):
     await message.delete()
     await bot.send_video(message.chat.id, "BAACAgUAAxkBAAIBjGQUMpjZncQRUimRznI5W_o7q0jEAALxCAACTwABiFT8ZIeEsarF0x4E")

#———————Song Module———————#

import os
import re

import yt_dlp
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaAudio,
                            InputMediaVideo, Message)

from config import (BANNED_USERS, SONG_DOWNLOAD_DURATION,
SONG_DOWNLOAD_DURATION_LIMIT)
from Youtube import YouTubeAPI
from formatters import convert_bytes
from song import song_markup

YouTube = YouTubeAPI()

# Command
SONG_COMMAND=("song|video")


@bot.on_message(
    filters.command(SONG_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@bot.on_edited_message(filters.command(SONG_COMMAND)
)

async def song_command_group(client, message: Message):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="↗️ Open Private Chat",
                    url=f"https://t.me/Unique_Adam_Bot?start=song",
                ),
            ]
        ]
    )
    await message.reply_text("You can download Music or Video from YouTube only in private chat. Please start me in private chat.", reply_markup=upl)


# Song Module


@bot.on_message(
    filters.command(SONG_COMMAND)
    & filters.private
    & ~BANNED_USERS
)
@bot.on_edited_message(filters.command(SONG_COMMAND)
)

async def song_command_private(client, message: Message):
    await message.delete()
    url = await YouTube.url(message)
    if url:
        if not await YouTube.exists(url):
            return await message.reply_text("Not a valid Youtube Link")
        mystic = await message.reply_text("🔄 Processing Query... Please Wait!")
        (
            title,
            duration_min,
            duration_sec,
            thumbnail,
            vidid,
        ) = await YouTube.details(url)
        if str(duration_min) == "None":
            return await mystic.edit_text("Live Link Detected. I am not able to download live youtube videos.")
        if int(duration_sec) > SONG_DOWNLOAD_DURATION_LIMIT:
            return await mystic.edit_text(
                "🖇 **Admins Only Play**\nOnly Admins and Auth Users can play music in this group.\n\nChange mode via /playmode and if you're already admin, reload admincache via /admincache".format(
                    SONG_DOWNLOAD_DURATION, duration_min
                )
            )
        buttons = song_markup(vidid)
        await mystic.delete()
        return await message.reply_photo(
            thumbnail,
            caption="**🔗Title:**- {0}\n\nSelect the type in which you want to download.".format(title),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        if len(message.command) < 2:
            return await message.reply_text("**Usage:**\n\n/song [Music Name] or [Youtube Link]")
    mystic = await message.reply_text("🔄 Processing Query... Please Wait!")
    query = message.text.split(None, 1)[1]
    try:
        (
            title,
            duration_min,
            duration_sec,
            thumbnail,
            vidid,
        ) = await YouTube.details(query)
    except:
        return await mystic.edit_text("Failed to Process Query!")
    if str(duration_min) == "None":
        return await mystic.edit_text("Live Link Detected. I am not able to download live youtube videos.")
    if int(duration_sec) > SONG_DOWNLOAD_DURATION_LIMIT:
        return await mystic.edit_text(
            "**Duration Limit Exceeded**\n\n**Allowed Duration: **{0} minute(s)\n**Received Duration:** {1} hour(s)".format(SONG_DOWNLOAD_DURATION, duration_min)
        )
    buttons = song_markup(vidid)
    await mystic.delete()
    return await message.reply_photo(
        thumbnail,
        caption="**🔗Title:**- {0}\n\nSelect the type in which you want to download.".format(title),
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@bot.on_callback_query(
    filters.regex(pattern=r"song_back") & ~BANNED_USERS
)
async def songs_back_helper(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    stype, vidid = callback_request.split("|")
    buttons = song_markup(vidid)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@bot.on_callback_query(
    filters.regex(pattern=r"song_helper") & ~BANNED_USERS
)

async def song_helper_cb(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    stype, vidid = callback_request.split("|")
    try:
        await CallbackQuery.answer("Getting Formats.. \n\nPlease Wait..", show_alert=True)
    except:
        pass
    if stype == "audio":
        try:
            formats_available, link = await YouTube.formats(
                vidid, True
            )
        except:
            return await CallbackQuery.edit_message_text("Failed to get available formats for the video. Please try any other track.")
        keyboard = InlineKeyboard()
        done = []
        for x in formats_available:
            check = x["format"]
            if "audio" in check:
                if x["filesize"] is None:
                    continue
                form = x["format_note"].title()
                if form not in done:
                    done.append(form)
                else:
                    continue
                sz = convert_bytes(x["filesize"])
                fom = x["format_id"]
                keyboard.row(
                    InlineKeyboardButton(
                        text=f"{form} Quality Audio = {sz}",
                        callback_data=f"song_download {stype}|{fom}|{vidid}",
                    ),
                )
        keyboard.row(
            InlineKeyboardButton(
                text="⬅ Back",
                callback_data=f"song_back {stype}|{vidid}",
            ),
            InlineKeyboardButton(
                text="🗑 Close", callback_data=f"close"
            ),
        )
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=keyboard
        )
    else:
        try:
            formats_available, link = await YouTube.formats(
                vidid, True
            )
        except Exception as e:
            print(e)
            return await CallbackQuery.edit_message_text("Failed to get available formats for the video. Please try any other track.")
        keyboard = InlineKeyboard()
        # AVC Formats Only [ Unique Adam Bot ]
        done = [160, 133, 134, 135, 136, 137, 298, 299, 264, 304, 266]
        for x in formats_available:
            check = x["format"]
            if x["filesize"] is None:
                continue
            if int(x["format_id"]) not in done:
                continue
            sz = convert_bytes(x["filesize"])
            ap = check.split("-")[1]
            to = f"{ap} = {sz}"
            keyboard.row(
                InlineKeyboardButton(
                    text=to,
                    callback_data=f"song_download {stype}|{x['format_id']}|{vidid}",
                )
            )
        keyboard.row(
            InlineKeyboardButton(
                text="⬅ Back",
                callback_data=f"song_back {stype}|{vidid}",
            ),
            InlineKeyboardButton(
                text="🗑 Close", callback_data=f"close"
            ),
        )
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=keyboard
        )


# Downloading Songs Here
import ffmpeg


@bot.on_callback_query(
    filters.regex(pattern=r"song_download") & ~BANNED_USERS
)
async def song_download_cb(client, CallbackQuery):
    try:
        await CallbackQuery.answer("Downloading")
    except:
        pass
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    stype, format_id, vidid = callback_request.split("|")
    mystic = await CallbackQuery.edit_message_text("Download Started\n\nDownloading speed could be slow. Please hold on..")
    yturl = f"https://www.youtube.com/watch?v={vidid}"
    with yt_dlp.YoutubeDL({"quiet": True}) as ytdl:
        x = ytdl.extract_info(yturl, download=False)
    title = (x["title"]).title()
    title = re.sub("\W+", " ", title)
    thumb_image_path = await CallbackQuery.message.download()
    duration = x["duration"]
    if stype == "video":
        thumb_image_path = await CallbackQuery.message.download()
        width = CallbackQuery.message.photo.width
        height = CallbackQuery.message.photo.height
        try:
            file_path = await YouTube.download(
                yturl,
                mystic,
                songvideo=True,
                format_id=format_id,
                title=title,
            )
        except Exception as e:
            return await mystic.edit_text("Failed to download song from Youtube-DL\n\n**Reason:** {0}".format(e))
        med = InputMediaVideo(
            media=file_path,
            duration=duration,
            width=width,
            height=height,
            thumb=thumb_image_path,
            caption=title,
            supports_streaming=True,
        )
        await mystic.edit_text("Uploading Started\n\nUploading speed could be slow. Please hold on..")
        await app.send_chat_action(
            chat_id=CallbackQuery.message.chat.id,
            action="upload_video",
        )
        try:
            await CallbackQuery.edit_message_media(media=med)
        except Exception as e:
            print(e)
            return await mystic.edit_text("Failed to upload on telegram from servers.")
        os.remove(file_path)
    elif stype == "audio":
        try:
            filename = await YouTube.download(
                yturl,
                mystic,
                songaudio=True,
                format_id=format_id,
                title=title,
            )
        except Exception as e:
            return await mystic.edit_text("Failed to download song from Youtube-DL\n\n**Reason:** {0}".format(e))
        med = InputMediaAudio(
            media=filename,
            caption=title,
            thumb=thumb_image_path,
            title=title,
            performer=x["uploader"],
        )
        await mystic.edit_text("Uploading Started\n\nUploading speed could be slow. Please hold on..")
        await app.send_chat_action(
            chat_id=CallbackQuery.message.chat.id,
            action="upload_audio",
        )
        try:
            await CallbackQuery.edit_message_media(media=med)
        except Exception as e:
            print(e)
            return await mystic.edit_text("Failed to upload on telegram from servers.")
        os.remove(filename)

print("Bot chalu ho gaya")
bot.run()