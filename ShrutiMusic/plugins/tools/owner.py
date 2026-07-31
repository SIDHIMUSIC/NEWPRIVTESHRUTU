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


# Owner welcome message ka text
def owner_welcome_text():
    return (
        f"<b>👑 ᴏᴡɴᴇʀ ʜᴀs ᴀʀʀɪᴠᴇᴅ</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"✨ <b>ᴡᴇʟᴄᴏᴍᴇ</b>\n"
        f"👤 <b><a href='https://t.me/{OWNER_USERNAME}'>{OWNER_NAME}</a></b>\n"
        f"🔗 @{OWNER_USERNAME}\n\n"
        f"<b>🛠️ ᴇxᴘᴇʀᴛɪsᴇ</b>\n"
        f"🎵 ᴍᴜsɪᴄ ʙᴏᴛs\n"
        f"🤖 ᴀɪ ʙᴏᴛs\n"
        f"⚡ ᴜsᴇʀʙᴏᴛs & ᴛᴏᴏʟs\n\n"
        f"💎 <i>ɢʀᴏᴜᴘ ᴍᴇɪɴ ᴏᴡɴᴇʀ ᴘʀᴇsᴇɴᴛ ʜᴀɪ</i> ❤️"
    )


# Welcome message ke neeche buttons (ek ke neeche ek)
def owner_welcome_buttons():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "❍ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ❍",
                    url=config.SUPPORT_CHANNEL,
                )
            ],
            [
                InlineKeyboardButton(
                    "❍ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ❍",
                    url=config.SUPPORT_GROUP,
                )
            ],
            [
                InlineKeyboardButton(
                    "❍ ᴏᴡɴᴇʀ ❍",
                    url=f"https://t.me/{OWNER_USERNAME}",
                )
            ],
        ]
    )


# Jab owner group mein naya join kare → welcome message
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

    # Sirf naya join hone pe (pehle left/banned tha)
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
    text = (
        f"<b>👑 ʙᴏᴛ ᴏᴡɴᴇʀ ᴘʀᴏғɪʟᴇ</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"✨ ᴛʜɪs ʙᴏᴛ ɪs ᴘʀᴏᴜᴅʟʏ ᴄʀᴀғᴛᴇᴅ,\n"
        f"ᴏᴡɴᴇᴅ ᴀɴᴅ ᴍᴀɴᴀɢᴇᴅ ʙʏ\n\n"
        f"👤 <b><a href='https://t.me/{OWNER_USERNAME}'>{OWNER_NAME}</a></b>\n"
        f"🔗 @{OWNER_USERNAME}\n\n"
        f"🚀 ᴀ ᴘᴀssɪᴏɴᴀᴛᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ & ᴛᴇᴄʜ ᴇɴᴛʜᴜsɪᴀsᴛ\n\n"
        f"<b>🛠️ ᴇxᴘᴇʀᴛɪsᴇ</b>\n"
        f"• 🎵 ᴍᴜsɪᴄ ʙᴏᴛs\n"
        f"• 🤖 ᴀɪ ʙᴏᴛs\n"
        f"• ⚡ ᴜsᴇʀʙᴏᴛs & ᴛᴏᴏʟs\n"
        f"• 🔐 sᴇᴄᴜʀᴇ sʏsᴛᴇᴍs\n"
        f"• 💎 sᴍᴏᴏᴛʜ ᴜx\n\n"
        f"<b>💡 ᴠɪsɪᴏɴ</b>\n"
        f"ᴄʀᴇᴀᴛɪɴɢ ᴘᴏᴡᴇʀғᴜʟ, ʀᴇʟɪᴀʙʟᴇ &\n"
        f"ᴜsᴇʀ-ғʀɪᴇɴᴅʟʏ ʙᴏᴛs\n"
        f"ᴛʜᴀᴛ ᴍᴀᴋᴇ ᴛᴇʟᴇɢʀᴀᴍ sᴍᴀʀᴛᴇʀ ⚡\n\n"
        f"👇 ᴄᴏɴɴᴇᴄᴛ & sᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ"
    )

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "❍ ᴏᴡɴᴇʀ ❍",
                    url=f"https://t.me/{OWNER_USERNAME}",
                )
            ],
            [
                InlineKeyboardButton(
                    "❍ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ❍",
                    url=config.SUPPORT_CHANNEL,
                )
            ],
            [
                InlineKeyboardButton(
                    "❍ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ❍",
                    url=config.SUPPORT_GROUP,
                )
            ],
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
