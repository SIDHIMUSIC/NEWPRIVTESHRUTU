from typing import Union

from pyrogram.types import InlineKeyboardButton

try:
    from pyrogram.enums import ButtonStyle
except Exception:
    ButtonStyle = None


def _s(name):
    if ButtonStyle is None:
        return None
    return getattr(ButtonStyle, name, name.lower())


R = _s("DANGER")
G = _s("SUCCESS")
B = _s("PRIMARY")


def setting_markup(_):
    return [
        [
            InlineKeyboardButton(text=_["ST_B_1"], callback_data="AU", style=R),
            InlineKeyboardButton(text=_["ST_B_3"], callback_data="LG", style=B),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_2"], callback_data="PM", style=G),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_4"], callback_data="VM", style=B),
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=R),
        ],
    ]


def vote_mode_markup(_, current, mode: Union[bool, str] = None):
    return [
        [
            InlineKeyboardButton(text="Vᴏᴛɪɴɢ ᴍᴏᴅᴇ ➜", callback_data="VOTEANSWER", style=B),
            InlineKeyboardButton(
                text=_["ST_B_5"] if mode is True else _["ST_B_6"],
                callback_data="VOMODECHANGE",
                style=G if mode is True else R,
            ),
        ],
        [
            InlineKeyboardButton(text="-2", callback_data="FERRARIUDTI M", style=R),
            InlineKeyboardButton(
                text=f"ᴄᴜʀʀᴇɴᴛ : {current}",
                callback_data="ANSWERVOMODE",
                style=B,
            ),
            InlineKeyboardButton(text="+2", callback_data="FERRARIUDTI A", style=G),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settings_helper", style=R),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=R),
        ],
    ]


def auth_users_markup(_, status: Union[bool, str] = None):
    return [
        [
            InlineKeyboardButton(text=_["ST_B_7"], callback_data="AUTHANSWER", style=B),
            InlineKeyboardButton(
                text=_["ST_B_8"] if status is True else _["ST_B_9"],
                callback_data="AUTH",
                style=G if status is True else R,
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_1"], callback_data="AUTHLIST", style=G),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settings_helper", style=R),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=R),
        ],
    ]


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    return [
        [
            InlineKeyboardButton(text=_["ST_B_10"], callback_data="SEARCHANSWER", style=B),
            InlineKeyboardButton(
                text=_["ST_B_11"] if Direct is True else _["ST_B_12"],
                callback_data="MODECHANGE",
                style=G if Direct is True else R,
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_13"], callback_data="AUTHANSWER", style=B),
            InlineKeyboardButton(
                text=_["ST_B_8"] if Group is True else _["ST_B_9"],
                callback_data="CHANNELMODECHANGE",
                style=G if Group is True else R,
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_14"], callback_data="PLAYTYPEANSWER", style=B),
            InlineKeyboardButton(
                text=_["ST_B_8"] if Playtype is True else _["ST_B_9"],
                callback_data="PLAYTYPECHANGE",
                style=G if Playtype is True else R,
            ),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settings_helper", style=R),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=R),
        ],
    ]
