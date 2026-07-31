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

# Groups jahan owner ko already welcome mil chuka (bot restart tak)
_welcomed_chats = set()

# ================= PREMIUM EMOJI =================
PE = {
    "crown": "6026292029179301727",
    "star": "6026162407066309019",
    "fire": "6321353301707203203",
    "heart": "6267140231632262769",
    "owner": "6147603715462271535",
    "support": "6145175650190759830",
}


# Message text ke liye premium emoji (Pyrogram format)
def pe(name: str, fallback: str = "✨") -> str:
    eid = (PE.get(name) or "").strip()
    if not eid or not eid.isdigit():
        return fallback
    return f'<emoji id="{eid}">{fallback}</emoji>'


# Check: emoji ID valid hai ya nahi
def pe_works(name: str) -> bool:
    eid = (PE.get(name) or "").strip()
    return bool(eid and eid.isdigit())


# Button banata hai — pe_name se icon_custom_emoji_id try karega
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


# Owner welcome message ka text
def owner_welcome_text():
    crown = pe("crown", "👑")
    star = pe("star", "✨")
    heart = pe("heart", "💎")

    return (
        f"<b>{crown} ᴏᴡɴᴇʀ ʜᴀs ᴀʀʀɪᴠᴇᴅ</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{star} <b>ᴡᴇʟᴄᴏᴍᴇ</b>\n"
        f"👤 <b><a href='https://t.me/{OWNER_USERNAME}'>{OWNER_NAME}</a></b>\n"
        f"🔗 @{OWNER_USERNAME}\n\n"
        f"<b>🛠️ ᴇxᴘᴇʀᴛɪsᴇ</b>\n"
        f"🎵 ᴍᴜsɪᴄ ʙᴏᴛs\n"
        f"🤖 ᴀɪ ʙᴏᴛs\n"
        f"⚡ ᴜsᴇʀʙᴏᴛs & ᴛᴏᴏʟs\n\n"
        f"{heart} <i>ɢʀᴏᴜᴘ ᴍᴇɪɴ ᴏᴡɴᴇʀ ᴘʀᴇsᴇɴᴛ ʜᴀɪ</i> ❤️"
    )


# Welcome message ke neeche buttons (ek ke neeche ek)
def owner_welcome_buttons():
    return InlineKeyboardMarkup(
        [
            [make_btn("❍ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ❍", url=config.SUPPORT_CHANNEL, pe_name="support")],
            [make_btn("❍ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ❍", url=config.SUPPORT_GROUP, pe_name="support")],
            [make_btn("❍ ᴏᴡɴᴇʀ ❍", url=f"https://t.me/{OWNER_USERNAME}", pe_name="owner")],
        ]
    )


# Jab owner group mein naya join kare → welcome
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


# Agar owner already group mein hai → pehle message pe welcome
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


# /owner command → owner profile + buttons
@app.on_message(filters.command("owner"))
async def owner_cmd(_, message: Message):
    crown = pe("crown", "👑")
    star = pe("star", "✨")
    fire = pe("fire", "🚀")
    heart = pe("heart", "💎")

    text = (
        f"<b>{crown} ʙᴏᴛ ᴏᴡɴᴇʀ ᴘʀᴏғɪʟᴇ {star}</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{star} ᴛʜɪs ʙᴏᴛ ɪs ᴘʀᴏᴜᴅʟʏ ᴄʀᴀғᴛᴇᴅ,\n"
        f"ᴏᴡɴᴇᴅ ᴀɴᴅ ᴍᴀɴᴀɢᴇᴅ ʙʏ\n\n"
        f"👤 <b><a href='https://t.me/{OWNER_USERNAME}'>{OWNER_NAME}</a></b>\n"
        f"🔗 @{OWNER_USERNAME}\n\n"
        f"{fire} ᴀ ᴘᴀssɪᴏɴᴀᴛᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ & ᴛᴇᴄʜ ᴇɴᴛʜᴜsɪᴀsᴛ\n\n"
        f"<b>🛠️ ᴇxᴘᴇʀᴛɪsᴇ</b>\n"
        f"• 🎵 ᴍᴜsɪᴄ ʙᴏᴛs\n"
        f"• 🤖 ᴀɪ ʙᴏᴛs\n"
        f"• ⚡ ᴜsᴇʀʙᴏᴛs & ᴛᴏᴏʟs\n"
        f"• 🔐 sᴇᴄᴜʀᴇ sʏsᴛᴇᴍs\n"
        f"• sᴍᴏᴏᴛʜ ᴜx {heart}\n\n"
        f"<b>💡 ᴠɪsɪᴏɴ</b>\n"
        f"ᴄʀᴇᴀᴛɪɴɢ ᴘᴏᴡᴇʀғᴜʟ, ʀᴇʟɪᴀʙʟᴇ &\n"
        f"ᴜsᴇʀ-ғʀɪᴇɴᴅʟʏ ʙᴏᴛs\n"
        f"ᴛʜᴀᴛ ᴍᴀᴋᴇ ᴛᴇʟᴇɢʀᴀᴍ sᴍᴀʀᴛᴇʀ ⚡\n\n"
        f"👇 ᴄᴏɴɴᴇᴄᴛ & sᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ"
    )

    keyboard = InlineKeyboardMarkup(
        [
            [make_btn("❍ ᴏᴡɴᴇʀ ❍", url=f"https://t.me/{OWNER_USERNAME}", pe_name="owner")],
            [make_btn("❍ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ❍", url=config.SUPPORT_CHANNEL, pe_name="support")],
            [make_btn("❍ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ❍", url=config.SUPPORT_GROUP, pe_name="support")],
        ]
    )

    await message.reply_text(
        text,
        reply_markup=keyboard,
        disable_web_page_preview=True,
        parse_mode=ParseMode.HTML,
    )


# Group mein hi/hello/gm etc. pe chat ko database mein save karna
@app.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message: Message):
    await add_served_chat(message.chat.id)
