from pyrogram.types import InlineKeyboardButton


def song_markup(vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔊 Audio",
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text="🎥 Video",
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗑 Close", callback_data="close"
            ),
        ],
    ]
    return buttons