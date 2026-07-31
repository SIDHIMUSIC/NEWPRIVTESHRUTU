from pyrogram import filters
from pyrogram.types import (
    Message,
    ChatMemberUpdated,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from pyrogram.enums import ChatMemberStatus
from ShrutiMusic import app
import config

OWNER_ID = 8170572505
OWNER_USERNAME = "SANATANI_BACCHA"
OWNER_NAME = "𓆩◕🇭𝐀𝐑𝐑𝐘◕𓆪 =‌𐏓 ⤨⃝🇮🇳™"

# groups jahan owner ko already welcome mil chuka hai (bot restart tak)
_welcomed_chats = set()


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


def owner_welcome_buttons():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📢 Support Channel",
                    url=config.SUPPORT_CHANNEL,
                ),
                InlineKeyboardButton(
                    "💬 Support Group",
                    url=config.SUPPORT_GROUP,
                ),
            ],
            [
                InlineKeyboardButton(
                    "👑 Owner",
                    url=f"https://t.me/{OWNER_USERNAME}",
                )
            ],
        ]
    )

@app.on_chat_member_updated()
async def owner_joined(_, update: ChatMemberUpdated):
    """Owner jab group join kare tab welcome"""
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

    # sirf naya join hone pe
    if update.old_chat_member is None or update.old_chat_member.status in (
        ChatMemberStatus.LEFT,
        ChatMemberStatus.BANNED,
    ):
        chat_id = update.chat.id
        _welcomed_chats.add(chat_id)
        await app.send_message(
            chat_id,
            owner_welcome_text(),
            disable_web_page_preview=True,
        )


@app.on_message(filters.group & filters.user(OWNER_ID), group=8)
async def owner_first_message(_, message: Message):
    """Agar owner already group mein hai, pehle message pe welcome"""
    chat_id = message.chat.id
    if chat_id in _welcomed_chats:
        return

    _welcomed_chats.add(chat_id)
    await message.reply_text(
        owner_welcome_text(),
        disable_web_page_preview=True,
    )


@app.on_message(filters.command("owner"))
async def owner_cmd(_, message: Message):
    text = (
        "<b>👑 ʙᴏᴛ ᴏᴡɴᴇʀ ᴘʀᴏғɪʟᴇ ✨</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "✨ ᴛʜɪs ʙᴏᴛ ɪs ᴘʀᴏᴜᴅʟʏ ᴄʀᴀғᴛᴇᴅ,\n"
        "ᴏᴡɴᴇᴅ ᴀɴᴅ ᴍᴀɴᴀɢᴇᴅ ʙʏ\n\n"
        f"👤 <b><a href='https://t.me/{OWNER_USERNAME}'>{OWNER_NAME}</a></b>\n"
        f"🔗 @{OWNER_USERNAME}\n\n"
        "🚀 ᴀ ᴘᴀssɪᴏɴᴀᴛᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ & ᴛᴇᴄʜ ᴇɴᴛʜᴜsɪᴀsᴛ\n\n"
        "🛠️ <b>ᴇxᴘᴇʀᴛɪsᴇ</b>\n"
        "• 🎵 ᴍᴜsɪᴄ ʙᴏᴛs\n"
        "• 🤖 ᴀɪ ʙᴏᴛs\n"
        "• ⚡ ᴜsᴇʀʙᴏᴛs & ᴛᴏᴏʟs\n"
        "• 🔐 sᴇᴄᴜʀᴇ sʏsᴛᴇᴍs\n"
        "• 💎 sᴍᴏᴏᴛʜ ᴜx\n\n"
        "💡 <b>ᴠɪsɪᴏɴ</b>\n"
        "ᴄʀᴇᴀᴛɪɴɢ ᴘᴏᴡᴇʀғᴜʟ, ʀᴇʟɪᴀʙʟᴇ &\n"
        "ᴜsᴇʀ-ғʀɪᴇɴᴅʟʏ ʙᴏᴛs\n"
        "ᴛʜᴀᴛ ᴍᴀᴋᴇ ᴛᴇʟᴇɢʀᴀᴍ sᴍᴀʀᴛᴇʀ ⚡\n\n"
        "👇 ᴄᴏɴɴᴇᴄᴛ & sᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ"
    )

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "❍ 𝐎ᴡɴᴇʀ ❍",
                    url=f"https://t.me/{OWNER_USERNAME}",
                )
            ],
            [
                InlineKeyboardButton(
                    "❍ Support Channel ❍",
                    url=config.SUPPORT_CHANNEL,
                )
            ],
        ]
    )

    await message.reply_text(
        text,
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )



# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"] ,prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


# --------------------------------------------------------------------------------- #




