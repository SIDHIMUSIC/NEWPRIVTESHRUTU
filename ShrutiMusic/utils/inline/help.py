from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ShrutiMusic import app

PE = {
    "admin": "6129805886383723340",
    "auth": "6147603715462271535",
    "broadcast": "4940559206244680622",
    "support": "5276032951342088188",
    "back": "5213358684024877471",
    "help": "6082592230021795516",
    "back2": "6267119710278522544",
    "home": "5873147866364514353",
}


def btn(text, callback_data=None, url=None, pe_name=None):
    kwargs = {"text": text}
    if callback_data:
        kwargs["callback_data"] = callback_data
    if url:
        kwargs["url"] = url
    if pe_name and pe_name in PE:
        kwargs["icon_custom_emoji_id"] = PE[pe_name]
    try:
        return InlineKeyboardButton(**kwargs)
    except TypeError:
        kwargs.pop("icon_custom_emoji_id", None)
        return InlineKeyboardButton(**kwargs)


def help_pannel_page1(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                btn(_["H_B_1"], callback_data="help_callback hb1", pe_name="admin"),
                btn(_["H_B_2"], callback_data="help_callback hb2", pe_name="admin"),
            ],
            [
                btn(_["H_B_3"], callback_data="help_callback hb3", pe_name="broadcast"),
                btn(_["H_B_4"], callback_data="help_callback hb4", pe_name="support"),
            ],
            [
                btn(_["H_B_5"], callback_data="help_callback hb5", pe_name="support"),
                btn(_["H_B_6"], callback_data="help_callback hb6", pe_name="help"),
                btn(_["H_B_7"], callback_data="help_callback hb7", pe_name="help"),
            ],
            [
                btn(_["H_B_8"], callback_data="help_callback hb8", pe_name="help"),
                btn(_["H_B_9"], callback_data="help_callback hb9", pe_name="help"),
                btn(_["H_B_10"], callback_data="help_callback hb10", pe_name="help"),
            ],
            [
                btn("⏮", callback_data="help_page_4", pe_name="back"),
                btn(
                    _["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                    pe_name="back",
                ),
                btn("⏭", callback_data="help_page_2", pe_name="back2"),
            ],
        ]
    )


def help_pannel_page2(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                btn(_["H_B_11"], callback_data="help_callback hb11", pe_name="help"),
                btn(_["H_B_12"], callback_data="help_callback hb12", pe_name="help"),
            ],
            [
                btn(_["H_B_13"], callback_data="help_callback hb13", pe_name="help"),
                btn(_["H_B_14"], callback_data="help_callback hb14", pe_name="help"),
            ],
            [
                btn(_["H_B_15"], callback_data="help_callback hb15", pe_name="help"),
                btn(_["H_B_16"], callback_data="help_callback hb16", pe_name="help"),
                btn(_["H_B_17"], callback_data="help_callback hb17", pe_name="help"),
            ],
            [
                btn(_["H_B_18"], callback_data="help_callback hb18", pe_name="help"),
                btn(_["H_B_19"], callback_data="help_callback hb19", pe_name="help"),
                btn(_["H_B_20"], callback_data="help_callback hb20", pe_name="help"),
            ],
            [
                btn("⏮", callback_data="help_page_1", pe_name="back"),
                btn(
                    _["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                    pe_name="back",
                ),
                btn("⏭", callback_data="help_page_3", pe_name="back2"),
            ],
        ]
    )


def help_pannel_page3(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                btn(_["H_B_21"], callback_data="help_callback hb21", pe_name="help"),
                btn(_["H_B_22"], callback_data="help_callback hb22", pe_name="help"),
            ],
            [
                btn(_["H_B_23"], callback_data="help_callback hb23", pe_name="help"),
                btn(_["H_B_24"], callback_data="help_callback hb24", pe_name="help"),
            ],
            [
                btn(_["H_B_25"], callback_data="help_callback hb25", pe_name="help"),
                btn(_["H_B_26"], callback_data="help_callback hb26", pe_name="help"),
                btn(_["H_B_27"], callback_data="help_callback hb27", pe_name="help"),
            ],
            [
                btn(_["H_B_28"], callback_data="help_callback hb28", pe_name="help"),
                btn(_["H_B_29"], callback_data="help_callback hb29", pe_name="help"),
                btn(_["H_B_30"], callback_data="help_callback hb30", pe_name="help"),
            ],
            [
                btn("⏮", callback_data="help_page_2", pe_name="back"),
                btn(
                    _["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                    pe_name="back",
                ),
                btn("⏭", callback_data="help_page_4", pe_name="back2"),
            ],
        ]
    )


def help_pannel_page4(_, START: Union[bool, int] = None):
    return InlineKeyboardMarkup(
        [
            [
                btn(_["H_B_31"], callback_data="help_callback hb31", pe_name="help"),
                btn(_["H_B_32"], callback_data="help_callback hb32", pe_name="help"),
            ],
            [
                btn(_["H_B_33"], callback_data="help_callback hb33", pe_name="help"),
                btn(_["H_B_34"], callback_data="help_callback hb34", pe_name="help"),
            ],
            [
                btn(_["H_B_35"], callback_data="help_callback hb35", pe_name="help"),
                btn(_["H_B_37"], callback_data="help_callback hb37", pe_name="help"),
            ],
            [
                btn(_["H_B_38"], callback_data="help_callback hb38", pe_name="help"),
                btn(_["H_B_39"], callback_data="help_callback hb39", pe_name="help"),
            ],
            [
                btn(_["H_B_36"], callback_data="help_callback hb36", pe_name="help"),
            ],
            [
                btn("⏮", callback_data="help_page_3", pe_name="back"),
                btn(
                    _["BACK_BUTTON"] if START else _["CLOSE_BUTTON"],
                    callback_data="settingsback_helper" if START else "close",
                    pe_name="back",
                ),
                btn("⏭", callback_data="help_page_1", pe_name="back2"),
            ],
        ]
    )


def help_back_markup(_, page: int = 1):
    return InlineKeyboardMarkup(
        [
            [
                btn(_["BACK_BUTTON"], callback_data=f"help_page_{page}", pe_name="home"),
            ]
        ]
    )


def private_help_panel(_):
    return [
        [
            btn(
                _["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
                pe_name="help",
            ),
        ]
    ]
