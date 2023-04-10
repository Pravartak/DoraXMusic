from pyrogram.types import InlineKeyboardButton


def song_markup(vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text="SG_B_2",
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text="SG_B_3",
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="CLOSE_BUTTON", callback_data="close"
            ),
        ],
    ]
    return buttons
