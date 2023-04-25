from typing import Union

from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from Adam import bot
from config import GITHUB_REPO, OWNER_ID

def private_panel(BOT_USERNAME, OWNER):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎 How to Use? Commands Menu.", callback_data="settingsback_helper"
            )
        ]
    ]
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text="👤 Bot Owner", user_id=OWNER),
                InlineKeyboardButton(
                    text="Source Code", url=f"{GITHUB_REPO}"
                ),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="Source Code", url=f"{GITHUB_REPO}"
                    ),
                ]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text="Group me lelo 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    return buttons

def help_panel(START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text="🗑 Close Menu", callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text="⬅ Back",
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text="🗑 Close Menu", callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Basic Commands",
                    callback_data="basic_commands",
                ),
                InlineKeyboardButton(
                    text="Photo Command",
                    callback_data="help_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Pre-Saved Songs",
                    callback_data="help_callback hb3",
                ),
                InlineKeyboardButton(
                    text="Pre-Saved Videos",
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Song/Video Search",
                    callback_data="help_callback hb5",
                ),
            ],
            mark,
        ]
    )
    return upl
