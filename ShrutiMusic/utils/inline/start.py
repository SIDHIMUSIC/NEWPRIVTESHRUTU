from pyrogram.types import InlineKeyboardButton
import config
from ShrutiMusic import app

# Premium emoji IDs
PE = {
    "owner": "6147603715462271535",
    "support": "6145175650190759830",
    "channel": "6145175650190759830",
    "add": "6026292029179301727",
    "help": "5413702412983389863",
    "network": "6026162407066309019",
    "source": "5416081784641168838",
    "back": "5215260113291455937",
}


def btn(text, url=None, callback_data=None, user_id=None, pe_name=None):
    kwargs = {"text": text}
    if url:
        kwargs["url"] = url
    if callback_data:
        kwargs["callback_data"] = callback_data
    if user_id:
        kwargs["user_id"] = user_id
    if pe_name and pe_name in PE:
        kwargs["icon_custom_emoji_id"] = PE[pe_name]
    try:
        return InlineKeyboardButton(**kwargs)
    except TypeError:
        kwargs.pop("icon_custom_emoji_id", None)
        return InlineKeyboardButton(**kwargs)


def start_panel(_):
    return [
        [
            btn(_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true", pe_name="add"),
            btn(_["S_B_2"], url=config.SUPPORT_GROUP, pe_name="support"),
        ],
        [
            btn(_["E_X_1"], url=config.UPSTREAM_REPO, pe_name="source"),
            btn(_["S_B_11"], callback_data="about_page", pe_name="network"),
        ],
    ]


def private_panel(_):
    return [
        [
            btn(_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true", pe_name="add"),
        ],
        [
            btn(_["S_B_11"], callback_data="about_page", pe_name="network"),
            btn(_["S_B_12"], callback_data="owner_page", pe_name="owner"),
        ],
        [
            btn(_["E_X_1"], callback_data="fork_repo", pe_name="source"),
            btn(_["S_B_5"], user_id=config.OWNER_ID, pe_name="owner"),
        ],
        [
            btn(_["S_B_4"], callback_data="help_page_1", pe_name="help"),
        ],
    ]


def about_panel(_):
    return [
        [
            btn(_["S_B_6"], url=config.SUPPORT_CHANNEL, pe_name="channel"),
            btn(_["S_B_2"], url=config.SUPPORT_GROUP, pe_name="support"),
        ],
        [
            btn(_["BACK_BUTTON"], callback_data="settingsback_helper", pe_name="back"),
        ],
    ]


def owner_panel(_):
    return [
        [
            InlineKeyboardButton(text=_["S_H_1"], url=config.INSTAGRAM),
            InlineKeyboardButton(text=_["S_H_2"], url=config.YOUTUBE),
        ],
        [
            InlineKeyboardButton(text=_["S_H_3"], url=config.GITHUB),
            InlineKeyboardButton(text=_["S_H_4"], url=config.DONATE),
        ],
        [
            btn(_["BACK_BUTTON"], callback_data="settingsback_helper", pe_name="back"),
        ],
    ]
