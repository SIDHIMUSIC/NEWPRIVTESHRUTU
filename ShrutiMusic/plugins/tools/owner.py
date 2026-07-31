from pyrogram import filters
from pyrogram.types import (
    Message,
    ChatMemberUpdated,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from pyrogram.enums import ChatMemberStatus
from ShrutiMusic import app
from ShrutiMusic.utils.database import add_served_chat
import config

OWNER_ID = 8170572505
OWNER_USERNAME = "SANATANI_BACCHA"
OWNER_NAME = "𓆩◕🇭𝐀𝐑𝐑𝐘◕𓆪 =‌𐏓 ⤨⃝🇮🇳™"

_welcomed_chats = set()


def owner_welcome_text():
    return (
        f"<tg-emoji emoji-id=\"6026292029179301727\">👑</tg-emoji> <b>ᴏᴡɴᴇʀ ʜᴀs ᴀʀʀɪᴠᴇᴅ</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"<tg-emoji emoji-id=\"5445284980978621387\">✨</tg-emoji> <b>ᴡᴇʟᴄᴏᴍᴇ</b>\n"
        f"<tg-emoji emoji-id=\"5379748062124056162\">👤</tg-emoji> <b><a href='https://t.me/{OWNER_USERNAME}'>{OWNER_NAME}</a></b>\n"
        f"🔗 @{OWNER_USERNAME}\n\n"
        f"<b>🛠️ ᴇxᴘᴇʀᴛɪsᴇ</b>\n"
        f"<tg-emoji emoji-id=\"6026256492619895014\">🎵</tg-emoji> ᴍᴜsɪᴄ ʙᴏᴛs\n"
        f"<tg-emoji emoji-id=\"6149728418603733657\">🤖</tg-emoji> ᴀɪ ʙᴏᴛs\n"
        f"<tg-emoji emoji-id=\"5416081784641168838\">⚡</tg-emoji> ᴜsᴇʀʙᴏᴛs & ᴛᴏᴏʟs\n\n"
        f"<tg-emoji emoji-id=\"5445284980978621387\">💎</tg-emoji> <i>ɢʀᴏᴜᴘ ᴍᴇɪɴ ᴏᴡɴᴇʀ ᴘʀᴇsᴇɴᴛ ʜᴀɪ</i> ❤️"
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
            parse_mode="HTML",
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
        parse_mode="HTML",
    )


@app.on_message(filters.command("owner"))
async def owner_cmd(_, message: Message):
    text = (
        f"<tg-emoji emoji-id=\"5368324170671202286\">👑</tg-emoji> <b>ʙᴏᴛ ᴏᴡɴᴇʀ ᴘʀᴏғɪʟᴇ</b>\n"
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
                    "👑 Owner",
                    url=f"https://t.me/{OWNER_USERNAME}",
                )
            ],
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
        ]
    )

    await message.reply_text(
        text,
        reply_markup=keyboard,
        disable_web_page_preview=True,
        parse_mode="HTML",
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
