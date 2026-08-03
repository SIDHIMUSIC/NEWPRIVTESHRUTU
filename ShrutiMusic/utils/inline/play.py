import math
from pyrogram.types import InlineKeyboardButton
from ShrutiMusic.utils.formatters import time_to_seconds
from config import BOT_USERNAME, SUPPORT_GROUP, SUPPORT_CHANNEL

PE = {
    "support": "5019759554234156094",
    "channel": "6145175650190759830",
    "close": "5215260113291455937",
    "play": "5208607440878197365",
    "pause": "5449885191600366307",
    "skip": "6311812139233316820",
    "stop": "6271674836628541366",
    "replay": "5904754092609114390",
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


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            btn(_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}", pe_name="play"),
            btn(_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}", pe_name="play"),
        ],
        [
            btn(_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}", pe_name="close"),
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "◉—————————"
    elif 10 < umm < 20:
        bar = "—◉————————"
    elif 20 <= umm < 30:
        bar = "——◉———————"
    elif 30 <= umm < 40:
        bar = "———◉——————"
    elif 40 <= umm < 50:
        bar = "————◉—————"
    elif 50 <= umm < 60:
        bar = "—————◉————"
    elif 60 <= umm < 70:
        bar = "——————◉———"
    elif 70 <= umm < 80:
        bar = "———————◉——"
    elif 80 <= umm < 95:
        bar = "————————◉—"
    else:
        bar = "—————————◉"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            btn("", callback_data=f"ADMIN Resume|{chat_id}", pe_name="play"),
            btn("", callback_data=f"ADMIN Pause|{chat_id}", pe_name="pause"),
            btn("", callback_data=f"ADMIN Replay|{chat_id}", pe_name="replay"),
            btn("", callback_data=f"ADMIN Skip|{chat_id}", pe_name="skip"),
            btn("", callback_data=f"ADMIN Stop|{chat_id}", pe_name="stop"),
        ],
        [
            btn("sᴜᴘᴘᴏʀᴛ", url=SUPPORT_GROUP, pe_name="support"),
            btn("ᴄʜᴀɴɴᴇʟ", url=SUPPORT_CHANNEL, pe_name="channel"),
        ],
        [
            btn(_["CLOSE_BUTTON"], callback_data="close", pe_name="close"),
        ],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            btn("", callback_data=f"ADMIN Resume|{chat_id}", pe_name="play"),
            btn("", callback_data=f"ADMIN Pause|{chat_id}", pe_name="pause"),
            btn("", callback_data=f"ADMIN Replay|{chat_id}", pe_name="replay"),
            btn("", callback_data=f"ADMIN Skip|{chat_id}", pe_name="skip"),
            btn("", callback_data=f"ADMIN Stop|{chat_id}", pe_name="stop"),
        ],
        [
            btn(_["CLOSE_BUTTON"], callback_data="close", pe_name="close"),
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            btn(_["P_B_1"], callback_data=f"NandPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}", pe_name="play"),
            btn(_["P_B_2"], callback_data=f"NandPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}", pe_name="play"),
        ],
        [
            btn(_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}", pe_name="close"),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            btn(_["P_B_3"], callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}", pe_name="play"),
        ],
        [
            btn(_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}", pe_name="close"),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            btn(_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}", pe_name="play"),
            btn(_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}", pe_name="play"),
        ],
        [
            btn("◁", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}", pe_name="skip"),
            btn(_["CLOSE_BUTTON"], callback_data=f"forceclose {query}|{user_id}", pe_name="close"),
            btn("▷", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}", pe_name="play"),
        ],
    ]
    return buttons
