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

bot = Client(
          "DJ Adam",
          api_id = 16519771,
          api_hash = "83754b17b54fe9d6a602e70c458afddb",
          bot_token = "6165241065:AAHPgX6HbVbu2fceDToVKFwAa9g1aFs_6Z4"
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
def command5(Client, message):
     bot.send_audio(message.chat.id, "CQACAgUAAxkBAAIBhGQUMWetYsPYaWPezYWJ3e8QYF-QAAJ8CAACGXGAVBv-niW895zIHgQ")
@bot.on_message(filters.command('song4'))
def command5(Client, message):
     bot.send_audio(message.chat.id, "CQACAgUAAxkBAAIBhmQUMWtJBuL9d9Z8-IiqAVd_NHMsAAJ9CAACGXGAVOeHnOpieonIHgQ")
     
#Send_video
@bot.on_message(filters.video & filters.private)
def video(Client, message):
     message.reply(message.video.file_id)
     
@bot.on_message(filters.command('video1'))
def command6(Client, message):
     bot.send_video(message.chat.id, "BAACAgUAAxkBAAIBiGQUMXNzwTHbS6FdRm1uGRPrTSH9AAJOCAAC2-1JVM5wXJQ5qiQmHgQ")
@bot.on_message(filters.command('video2'))
def command7(Client, message):
     bot.send_video(message.chat.id, "BAACAgUAAxkBAAIBjGQUMpjZncQRUimRznI5W_o7q0jEAALxCAACTwABiFT8ZIeEsarF0x4E")

#@bot.on_message(filters.text)
#def delete_text(bot, message):
#     bot.delete_messages(message.chat.id, message_id)

#———————————————————#

import asyncio
import math
import os
import time
from random import randint
from urllib.parse import urlparse

import aiofiles
import aiohttp
import requests
import wget
import yt_dlp
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos

from config import DURATION_LIMIT


@Client.on_message(filters.command('song'))
def command8(client, message):

    user_id = message.from_user.id
    user_name = message.from_user.first_name
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    query = " "
    for i in message.command[1:]:
        query += " " + str(i)
    print(query)
    m = message.reply("🔎 Finding the song...")
    ydl_opts = {"format": "bestaudio[ext=mp3]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        # print(results)
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)

        duration = results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]

    except Exception as e:
        m.edit("❌ Found Nothing.\n\nTry another keywork or maybe spell it properly.")
        print(str(e))
        return
    m.edit("Downloading the song ")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = "**🎵 Uploaded by DJ Adam**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit("❌ Error")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


def get_text(message: Message, str) -> str:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join(["🔴" for i in range(math.floor(percentage / 10))]),
            "".join(["🔘" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2),
        )
        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(
                    "{}\n**File Name:** `{}`\n{}".format(type_of_ps, file_name, tmp)
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit("{}\n{}".format(type_of_ps, tmp))
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass


def get_user(message: Message, text: str) -> str:
    if text is None:
        asplit = None
    else:
        asplit = text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text if text else None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_


def get_readable_time(seconds: int) -> int:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]


ydl_opts = {
    "format": "bestaudio/best",
    "writethumbnail": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}


def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


# Funtion To Download Song
async def download_song(url):
    song_name = f"{randint(6969, 6999)}.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(song_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return song_name


is_downloading = False


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


@Client.on_message(filters.command(["vsong", "video"]))
async def ytmusic(client, message: Message):
    global is_downloading
    if is_downloading:
        await message.reply_text(
            "Another download is in progress, try again after sometime."
        )
        return

    urlissed = get_text(message)

    pablo = await client.send_message(
        message.chat.id, f"`Getting {urlissed} From Youtube Servers. Please Wait.`"
    )
    if not urlissed:
        await pablo.edit("Invalid Command Syntax, Please Check Help Menu To Know More!")
        return

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    thums = mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        is_downloading = True
        with yt_dlp.YoutubeDL(opts) as ytdl:
            infoo = ytdl.extract_info(url, False)
            duration = round(infoo["duration"] / 60)

            if duration > DURATION_LIMIT:
                await pablo.edit(
                    f"❌ Videos longer than {DURATION_LIMIT} minute(s) aren't allowed, the provided video is {duration} minute(s)"
                )
                is_downloading = False
                return
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception:
        # await pablo.edit(event, f"**Failed To Download** \n**Error :** `{str(e)}`")
        is_downloading = False
        return

    c_time = time.time()
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**Video Name ➠** `{thum}` \n**Requested For :** `{urlissed}` \n**Channel :** `{thums}` \n**Link :** `{mo}`"
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        progress=progress,
        progress_args=(
            pablo,
            c_time,
            f"`Uploading {urlissed} Song From YouTube Music!`",
            file_stark,
        ),
    )
    await pablo.delete()
    is_downloading = False
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)


print("I AM ALIVE")
bot.run()
