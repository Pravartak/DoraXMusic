from __future__ import unicode_literals

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
from pyrogram import Client, filters
import config

bot = Client(
          "DJ Adam",
          api_id=config.API_ID,
          api_hash=config.API_HASH,
          bot_token=config.BOT_TOKEN,
)

@bot.on_message(filters.command('start')) #Creating a command.
def command1(bot, message): #Creating a function.
       bot.send_message(message.chat.id, "Hello! Use /help for help on how to use me. Or use the menu button.") #Calling a method.

@bot.on_message(filters.command('help')) #Creating a command.
def command2(bot, message): #Creating a function.
       message.reply_text("Here is a list of commands that you can use-\n\n/start - You can start the bot. you have used this already!\n\n/help - List of commands will appear, you have this one also!\n\n/photo - You will get some photos provided by @No_me_no_no. If you want to add more photos, just dm them to my owner.\n\n/song1 - Ghode Pe Sawar Song\n\n/song2 - Blinding Lights Song\n\n/song3 - Apna Bana Le Song\n\n/song4 - Kesariya Song\n\n/video1 - Ghode Pe Sawar Song Video\n\n/video2 - Baarishein Song Video\n\nYou can also add me to your groups as a welcome bot! (Still in development)\n\nOwner will keep me updating and make sure I don't die.") #Calling a method.
     
#echobot  
#@bot.on_message(filters.text)
#def echobot(Client, message):
#     message.reply_text(message.text)

def extract_status_change(chat_member_update: ChatMemberUpdated) -> Optional[Tuple[bool, bool]]:
    """Takes a ChatMemberUpdated instance and extracts whether the 'old_chat_member' was a member
    of the chat and whether the 'new_chat_member' is a member of the chat. Returns None, if
    the status didn't change.
    """
    status_change = chat_member_update.difference().get("status")
    old_is_member, new_is_member = chat_member_update.difference().get("is_member", (None, None))

    if status_change is None:
        return None

    old_status, new_status = status_change
    was_member = old_status in [
        ChatMember.MEMBER,
        ChatMember.OWNER,
        ChatMember.ADMINISTRATOR,
    ] or (old_status == ChatMember.RESTRICTED and old_is_member is True)
    is_member = new_status in [
        ChatMember.MEMBER,
        ChatMember.OWNER,
        ChatMember.ADMINISTRATOR,
    ] or (new_status == ChatMember.RESTRICTED and new_is_member is True)

    return was_member, is_member
     
#welcomebot
# Keep track of which chats the bot is in
    application.add_handler(ChatMemberHandler(track_chats, ChatMemberHandler.MY_CHAT_MEMBER))
    application.add_handler(CommandHandler('getchats', getchats))

async def show_chats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Shows which chats the bot is in"""
    user_ids = ", ".join(str(uid) for uid in context.bot_data.setdefault("user_ids", set()))
    group_ids = ", ".join(str(gid) for gid in context.bot_data.setdefault("group_ids", set()))
    channel_ids = ", ".join(str(cid) for cid in context.bot_data.setdefault("channel_ids", set()))
    text = (
        f"@{context.bot.username} is currently in a conversation with the user IDs {user_ids}."
        f" Moreover it is a member of the groups with IDs {group_ids} "
        f"and administrator in the channels with IDs {channel_ids}."
    )
    await update.effective_message.reply_text(text)

async def greet_chat_members(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Greets new users in chats and announces when someone leaves"""
    result = extract_status_change(update.chat_member)
    if result is None:
        return

    was_member, is_member = result
    cause_name = update.chat_member.from_user.mention_html()
    member_name = update.chat_member.new_chat_member.user.mention_html()

    if not was_member and is_member:
        await update.effective_chat.send_message(
            f"{member_name} was added by {cause_name}. Welcome!",
            parse_mode=ParseMode.HTML,
        )
    elif was_member and not is_member:
        await update.effective_chat.send_message(
            f"{member_name} is no longer with us. Thanks a lot, {cause_name} ...",
            parse_mode=ParseMode.HTML,
        )

async def start_private_chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Greets the user and records that they started a chat with the bot if it's a private chat.
    Since no `my_chat_member` update is issued when a user starts a private chat with the bot
    for the first time, we have to track it explicitly here.
    """
    user_name = update.effective_user.full_name
    chat = update.effective_chat
    if chat.type != Chat.PRIVATE or chat.id in context.bot_data.get("user_ids", set()):
        return

    logger.info("%s started a private chat with the bot", user_name)
    context.bot_data.setdefault("user_ids", set()).add(chat.id)

    await update.effective_message.reply_text(
        f"Welcome {user_name}. Use /show_chats to see what chats I'm in."
    )
        
# Handle members joining/leaving chats.
    application.add_handler(ChatMemberHandler(greet_chat_members, ChatMemberHandler.CHAT_MEMBER))

# = "Hiee $username ! $title me aapka swagat hai 😇"
#text = text.replace("$username", new_chat_member.first_name)
#text = text.replace("$title", )

#@bot.on_message(filters.chat() & filters.new_chat_members)

#def welcomebot(Client, message):
#     message.reply_text(WELCOME_MESSAGE)
     
#Send_photo
@bot.on_message(filters.photo & filters.private)
def photo(Client, message):
     message.reply(message.photo.file_id)

@bot.on_message(filters.command('photo'))
def command3(Client, message):
     bot.send_photo(message.chat.id, "https://imgur.com/t/anime_wallpaper/QLRTXVL")
     bot.send_photo(message.chat.id, "https://imgur.com/t/anime_wallpaper/toaUzHM")
     bot.send_photo(message.chat.id, "AgACAgUAAxkBAAICRGQXNzrruA740MOfigY_mmE8EAURAAILuDEb1Bm4VD-ekA1wt9AGAAgBAAMCAAN4AAceBA")
     
#Send_audio
@bot.on_message(filters.audio & filters.private)
def audio(Client, message):
     message.reply(message.audio.file_id)
     
@bot.on_message(filters.command('song1'))
def command4(Client, message):
     bot.send_audio(message.chat.id, "CQACAgUAAxkBAAIBgGQUMVb6H3dT_peXVA-cbzXZQWKsAALoBwAClslJVHzxHobLNHdjHgQ")
@bot.on_message(filters.command('song2'))
def command5(Client, message):
     bot.send_audio(message.chat.id, "CQACAgUAAxkBAAIBgmQUMWMlYA2XRosCGB7rEqWziv2tAAJ7CAACGXGAVDj0md0qWrP1HgQ")
@bot.on_message(filters.command('song3'))
def command6(Client, message):
     bot.send_audio(message.chat.id, "CQACAgUAAxkBAAIBhGQUMWetYsPYaWPezYWJ3e8QYF-QAAJ8CAACGXGAVBv-niW895zIHgQ")
@bot.on_message(filters.command('song4'))
def command7(Client, message):
     bot.send_audio(message.chat.id, "CQACAgUAAxkBAAIBhmQUMWtJBuL9d9Z8-IiqAVd_NHMsAAJ9CAACGXGAVOeHnOpieonIHgQ")
     
#Send_video
@bot.on_message(filters.video & filters.private)
def video(Client, message):
     message.reply(message.video.file_id)
     
@bot.on_message(filters.command('video1'))
def command8(Client, message):
     bot.send_video(message.chat.id, "BAACAgUAAxkBAAIBiGQUMXNzwTHbS6FdRm1uGRPrTSH9AAJOCAAC2-1JVM5wXJQ5qiQmHgQ")
@bot.on_message(filters.command('video2'))
def command9(Client, message):
     bot.send_video(message.chat.id, "BAACAgUAAxkBAAIBjGQUMpjZncQRUimRznI5W_o7q0jEAALxCAACTwABiFT8ZIeEsarF0x4E")

#@bot.on_message(filters.text)
#def delete_text(bot, message):
#     bot.delete_messages(message.chat.id, message_id)

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
from language import language, languageCB
from formatters import convert_bytes
from song import song_markup

# Command
SONG_COMMAND=('song', 'video')


@bot.on_message(
    filters.command(SONG_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@bot.on_edited_message(filters.command(SONG_COMMAND)
)
@language
async def song_command_group(client, message: Message, _):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["↗️ Open Private Chat"],
                    url=f"https://t.me/{app.username}?start=song",
                ),
            ]
        ]
    )
    await message.reply_text(_["You can download Music or Video from YouTube only in private chat. Please start me in private chat."], reply_markup=upl)


# Song Module


@bot.on_message(
    filters.command(SONG_COMMAND)
    & filters.private
    & ~BANNED_USERS
)
@bot.on_edited_message(filters.command(SONG_COMMAND)
)
@language
async def song_command_private(client, message: Message, _):
    await message.delete()
    url = await YouTube.url(message)
    if url:
        if not await YouTube.exists(url):
            return await message.reply_text(_["song_5"])
        mystic = await message.reply_text(_["play_1"])
        (
            title,
            duration_min,
            duration_sec,
            thumbnail,
            vidid,
        ) = await YouTube.details(url)
        if str(duration_min) == "None":
            return await mystic.edit_text(_["song_3"])
        if int(duration_sec) > SONG_DOWNLOAD_DURATION_LIMIT:
            return await mystic.edit_text(
                _["play_4"].format(
                    SONG_DOWNLOAD_DURATION, duration_min
                )
            )
        buttons = song_markup(_, vidid)
        await mystic.delete()
        return await message.reply_photo(
            thumbnail,
            caption=_["song_4"].format(title),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["song_2"])
    mystic = await message.reply_text(_["play_1"])
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
        return await mystic.edit_text(_["play_3"])
    if str(duration_min) == "None":
        return await mystic.edit_text(_["song_3"])
    if int(duration_sec) > SONG_DOWNLOAD_DURATION_LIMIT:
        return await mystic.edit_text(
            _["play_6"].format(SONG_DOWNLOAD_DURATION, duration_min)
        )
    buttons = song_markup(_, vidid)
    await mystic.delete()
    return await message.reply_photo(
        thumbnail,
        caption=_["song_4"].format(title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@bot.on_callback_query(
    filters.regex(pattern=r"song_back") & ~BANNED_USERS
)
@languageCB
async def songs_back_helper(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    stype, vidid = callback_request.split("|")
    buttons = song_markup(_, vidid)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@bot.on_callback_query(
    filters.regex(pattern=r"song_helper") & ~BANNED_USERS
)
@languageCB
async def song_helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    stype, vidid = callback_request.split("|")
    try:
        await CallbackQuery.answer(_["song_6"], show_alert=True)
    except:
        pass
    if stype == "audio":
        try:
            formats_available, link = await YouTube.formats(
                vidid, True
            )
        except:
            return await CallbackQuery.edit_message_text(_["song_7"])
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
                text=_["BACK_BUTTON"],
                callback_data=f"song_back {stype}|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"close"
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
            return await CallbackQuery.edit_message_text(_["song_7"])
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
                text=_["BACK_BUTTON"],
                callback_data=f"song_back {stype}|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"close"
            ),
        )
        return await CallbackQuery.edit_message_reply_markup(
            reply_markup=keyboard
        )


# Downloading Songs Here


@bot.on_callback_query(
    filters.regex(pattern=r"song_download") & ~BANNED_USERS
)
@languageCB
async def song_download_cb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer("Downloading")
    except:
        pass
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    stype, format_id, vidid = callback_request.split("|")
    mystic = await CallbackQuery.edit_message_text(_["song_8"])
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
            return await mystic.edit_text(_["song_9"].format(e))
        med = InputMediaVideo(
            media=file_path,
            duration=duration,
            width=width,
            height=height,
            thumb=thumb_image_path,
            caption=title,
            supports_streaming=True,
        )
        await mystic.edit_text(_["song_11"])
        await app.send_chat_action(
            chat_id=CallbackQuery.message.chat.id,
            action="upload_video",
        )
        try:
            await CallbackQuery.edit_message_media(media=med)
        except Exception as e:
            print(e)
            return await mystic.edit_text(_["song_10"])
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
            return await mystic.edit_text(_["song_9"].format(e))
        med = InputMediaAudio(
            media=filename,
            caption=title,
            thumb=thumb_image_path,
            title=title,
            performer=x["uploader"],
        )
        await mystic.edit_text(_["song_11"])
        await app.send_chat_action(
            chat_id=CallbackQuery.message.chat.id,
            action="upload_audio",
        )
        try:
            await CallbackQuery.edit_message_media(media=med)
        except Exception as e:
            print(e)
            return await mystic.edit_text(_["song_10"])
        os.remove(filename)

print("I AM ALIVE")
bot.run()
