from pyrogram.types import InlineKeyboardButton
import config
from ShrutiMusic import app

try:
    from pyrogram.enums import ButtonStyle
except Exception:
    ButtonStyle = None

PE = {
    "owner": "5323261373801571717",
    "support": "5019759554234156094",
    "channel": "6145175650190759830",
    "add": "6033108614724456536",
    "comman": "6118209143972040877",
    "network": "5375177250553487549",
    "source": "6118209143972040877",
    "back": "5215260113291455937",
    "pfp": "5256143829672672750",
    "igram": "4990082283701535678",
    "commn": "5246786354360105755",
    "ghub": "5933540612694347912",
    "ytune": "6325448939570989024",
    "dont": "5462975985630600496",
}


def btn(text, url=None, callback_data=None, user_id=None, pe_name=None, style=None):
    kwargs = {"text": text}
    if url:
        kwargs["url"] = url
    if callback_data:
        kwargs["callback_data"] = callback_data
    if user_id:
        kwargs["user_id"] = user_id
    if pe_name and pe_name in PE:
        kwargs["icon_custom_emoji_id"] = PE[pe_name]
    if style is not None:
        kwargs["style"] = style
    try:
        return InlineKeyboardButton(**kwargs)
    except TypeError:
        kwargs.pop("icon_custom_emoji_id", None)
        kwargs.pop("style", None)
        return InlineKeyboardButton(**kwargs)


def _s(name):
    if ButtonStyle is None:
        return None
    return getattr(ButtonStyle, name, name.lower())


def start_panel(_):
    return [
        [
            btn(_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true", pe_name="add", style=_s("PRIMARY")),
            btn(_["S_B_2"], url=config.SUPPORT_GROUP, pe_name="support", style=_s("SUCCESS")),
        ],
        [
            btn(_["E_X_1"], url="https://t.me/TG_BIO_STYLE", pe_name="source", style=_s("PRIMARY")),
            btn(_["S_B_11"], callback_data="about_page", pe_name="network", style=_s("SUCCESS")),
        ],
    ]


def private_panel(_):
    return [
        [
            btn(_["S_B_3"], url=f"https://t.me/{app.username}?startgroup=true", pe_name="add", style=_s("PRIMARY")),
        ],
        [
            btn(_["S_B_11"], callback_data="about_page", pe_name="network", style=_s("SUCCESS")),
            btn(_["S_B_12"], callback_data="owner_page", pe_name="pfp", style=_s("PRIMARY")),
        ],
        [
            btn(_["E_X_1"], callback_data="fork_repo", pe_name="source", style=_s("PRIMARY")),
            btn(_["S_B_5"], user_id=config.OWNER_ID, pe_name="owner", style=_s("DANGER")),
        ],
        [
            btn(_["S_B_4"], callback_data="help_page_1", pe_name="commn", style=_s("SUCCESS")),
        ],
    ]


def about_panel(_):
    return [
        [
            btn(_["S_B_6"], url=config.SUPPORT_CHANNEL, pe_name="channel", style=_s("PRIMARY")),
            btn(_["S_B_2"], url=config.SUPPORT_GROUP, pe_name="support", style=_s("SUCCESS")),
        ],
        [
            btn(_["BACK_BUTTON"], callback_data="settingsback_helper", pe_name="back", style=_s("DANGER")),
        ],
    ]


def owner_panel(_):
    return [
        [
            btn(_["S_H_1"], url=config.INSTAGRAM, pe_name="igram", style=_s("PRIMARY")),
            btn(_["S_H_2"], url=config.YOUTUBE, pe_name="ytune", style=_s("DANGER")),
        ],
        [
            btn(_["S_H_3"], url=config.GITHUB, pe_name="ghub", style=_s("PRIMARY")),
            btn(_["S_H_4"], url=config.DONATE, pe_name="dont", style=_s("SUCCESS")),
        ],
        [
            btn(_["BACK_BUTTON"], callback_data="settingsback_helper", pe_name="back", style=_s("DANGER")),
        ],
    ]
