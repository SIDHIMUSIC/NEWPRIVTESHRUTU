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
                btn(_["H_B_2"], callback_data="help_callback hb2", pe_name="auth"),
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
                btn("⏭", callback_data="help_page_2", pe_name="back"),
            ],
        ]
    )
