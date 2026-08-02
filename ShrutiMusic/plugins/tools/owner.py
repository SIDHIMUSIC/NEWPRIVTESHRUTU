from pyrogram import filters
from pyrogram.types import (
    Message,
    ChatMemberUpdated,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from pyrogram.enums import ChatMemberStatus, ParseMode
from ShrutiMusic import app
from ShrutiMusic.utils.database import add_served_chat
import config

OWNER_ID = 8170572505
OWNER_USERNAME = "SANATANI_BACCHA"
OWNER_NAME = "𓆩◕🇭𝐀𝐑𝐑𝐘◕𓆪 =‌𐏓 ⤨⃝🇮🇳™"

_welcomed_chats = set()

# ================= PREMIUM EMOJI =================
PE = {
    "crown": "6026292029179301727",
    "star": "6026162407066309019",
    "fire": "6321353301707203203",
    "heart": "6267140231632262769",
    "owner": "6147603715462271535",
    "support": "6145175650190759830",
    "case": "6242199485393409396",
    "human": "5408846628763217930",
    "music": "5276352986535194063",
    "ai": "6242225001794114994",
    "light": "5895215494230709454",
    "lock": "5278573677900752088",
    "vision": "5422439311196834318",
    "here": "6062367259089703519",
    "brain": "6026243612012974483",
    "expert": "6082420869416619509",
}


def pe(name: str, fallback: str = "✨") -> str:
    eid = (PE.get(name) or "").strip()
    if not eid or not eid.isdigit():
        return fallback
    return f'<emoji id="{eid}">{fallback}</emoji>'


def pe_works(name: str) -> bool:
    eid = (PE.get(name) or "").strip()
    return bool(eid and eid.isdigit())


def make_btn(text: str, url: str = None, callback_data: str = None, pe_name: str = None):
    kwargs = {"text": text}
    if url:
        kwargs["url"] = url
    if callback_data:
        kwargs["callback_data"] = callback_data

    if pe_name and pe_works(pe_name):
        kwargs["icon_custom_emoji_id"] = PE[pe_name].strip()

    try:
        return InlineKeyboardButton(**kwargs)
    except TypeError:
        kwargs.pop("icon_custom_emoji_id", None)
        return InlineKeyboardButton(**kwargs)


def owner_welcome_text():
    crown = pe("crown", "👑")
    star = pe("star", "✨")
    heart = pe("heart", "💎")
    human = pe("human", "👤")
    case = pe("case", "🔗")
    expert = pe("expert", "🛠️")
    music = pe("music", "🎵")
    ai = pe("ai", "🤖")
    light = pe("light", "⚡")

    return (
        f"<b>{crown} ᴏᴡɴᴇʀ ʜᴀs ᴀʀʀɪᴠᴇᴅ</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{star} <b>ᴡᴇʟᴄᴏᴍᴇ</b>\n"
        f"{human} <b><a href='https://t.me/{OWNER_USERNAME}'>{OWNER_NAME}</a></b>\n"
        f"{case} @{OWNER_USERNAME}\n\n"
        f"<b>{expert} ᴇxᴘᴇʀᴛɪsᴇ</b>\n"
        f"{music} ᴍᴜsɪᴄ ʙᴏᴛs\n"
        f"{ai} ᴀɪ ʙᴏᴛs\n"
        f"{light} ᴜsᴇʀʙᴏᴛs & ᴛᴏᴏʟs\n\n"
        f"{heart} <i>ɢʀᴏᴜᴘ ᴍᴇɪɴ ᴏᴡɴᴇʀ ᴘʀᴇsᴇɴᴛ ʜᴀɪ</i> {heart}"
    )


def owner_welcome_buttons():
    return InlineKeyboardMarkup(
        [
            [make_btn("❍ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ❍", url=config.SUPPORT_CHANNEL, pe_name="support")],
            [make_btn("❍ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ❍", url=config.SUPPORT_GROUP, pe_name="support")],
            [make_btn("❍ ᴏᴡɴᴇʀ ❍", url=f"https://t.me/{OWNER_USERNAME}", pe_name="light")],
        ]
    )


@app.on_chat_member_updated()
async def owner_joined(_, update: ChatMemberUpdated):
    if not (update.new_chat_member and update.new_chat_member.user):
        return

    if update.new_chat_member.user.id != OWNER_ID:
        return

    if update.new_chat_member.status not in (
        ChatMemberStatus.MEMBER,
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.OWNER,
    ):
        return

    if update.old_chat_member is None or update.old_chat_member.status in (
        ChatMemberStatus.LEFT,
        ChatMemberStatus.BANNED,
    ):
        chat_id = update.chat.id
        _welcomed_chats.add(chat_id)
        await app.send_message(
            chat_id,
            owner_welcome_text(),
            reply_markup=owner_welcome_buttons(),
            disable_web_page_preview=True,
            parse_mode=ParseMode.HTML,
        )


@app.on_message(filters.group & filters.user(OWNER_ID), group=8)
async def owner_first_message(_, message: Message):
    chat_id = message.chat.id
    if chat_id in _welcomed_chats:
        return

    _welcomed_chats.add(chat_id)
    await message.reply_text(
        owner_welcome_text(),
        reply_markup=owner_welcome_buttons(),
        disable_web_page_preview=True,
        parse_mode=ParseMode.HTML,
    )


@app.on_message(filters.command("owner"))
async def owner_cmd(_, message: Message):
    crown = pe("crown", "👑")
    star = pe("star", "✨")
    fire = pe("fire", "🚀")
    heart = pe("heart", "💎")
    human = pe("human", "👤")
    case = pe("case", "🔗")
    expert = pe("expert", "🛠️")
    music = pe("music", "🎵")
    ai = pe("ai", "🤖")
    light = pe("light", "⚡")
    lock = pe("lock", "🔐")
    vision = pe("vision", "💡")
    here = pe("here", "👇")

    text = (
        f"<b>{crown} ʙᴏᴛ ᴏᴡɴᴇʀ ᴘʀᴏғɪʟᴇ {star}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{star} ᴛʜɪs ʙᴏᴛ ɪs ᴘʀᴏᴜᴅʟʏ ᴄʀᴀғᴛᴇᴅ,\n"
        f"ᴏᴡɴᴇᴅ ᴀɴᴅ ᴍᴀɴᴀɢᴇᴅ ʙʏ\n\n"
        f"{human} <b><a href='https://t.me/{OWNER_USERNAME}'>{OWNER_NAME}</a></b>\n"
        f"{case} @{OWNER_USERNAME}\n\n"
        f"{fire} ᴀ ᴘᴀssɪᴏɴᴀᴛᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ & ᴛᴇᴄʜ ᴇɴᴛʜᴜsɪᴀsᴛ\n\n"
        f"<b>{expert} ᴇxᴘᴇʀᴛɪsᴇ</b>\n"
        f"• {music} ᴍᴜsɪᴄ ʙᴏᴛs\n"
        f"• {ai} ᴀɪ ʙᴏᴛs\n"
        f"• {light} ᴜsᴇʀʙᴏᴛs & ᴛᴏᴏʟs\n"
        f"• {lock} sᴇᴄᴜʀᴇ sʏsᴛᴇᴍs\n"
        f"• sᴍᴏᴏᴛʜ ᴜx {heart}\n\n"
        f"<b>{vision} ᴠɪsɪᴏɴ</b>\n"
        f"ᴄʀᴇᴀᴛɪɴɢ ᴘᴏᴡᴇʀғᴜʟ, ʀᴇʟɪᴀʙʟᴇ &\n"
        f"ᴜsᴇʀ-ғʀɪᴇɴᴅʟʏ ʙᴏᴛs\n"
        f"ᴛʜᴀᴛ ᴍᴀᴋᴇ ᴛᴇʟᴇɢʀᴀᴍ sᴍᴀʀᴛᴇʀ {light}\n\n"
        f"{here} ᴄᴏɴɴᴇᴄᴛ & sᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ"
    )

    keyboard = InlineKeyboardMarkup(
        [
            [make_btn("❍ ᴏᴡɴᴇʀ ❍", url=f"https://t.me/{OWNER_USERNAME}", pe_name="owner")],
            [make_btn("❍ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ❍", url=config.SUPPORT_CHANNEL, pe_name="support")],
            [make_btn("❍ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ❍", url=config.SUPPORT_GROUP, pe_name="light")],
        ]
    )

    await message.reply_text(
        text,
        reply_markup=keyboard,
        disable_web_page_preview=True,
        parse_mode=ParseMode.HTML,
    )


@app.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message: Message):
    await add_served_chat(message.chat.id)
