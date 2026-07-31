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


@app.on_chat_member_updated()
async def owner_joined(_, update: ChatMemberUpdated):
    if (
        update.new_chat_member
        and update.new_chat_member.user
        and update.new_chat_member.user.id == OWNER_ID
        and update.new_chat_member.status in (
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        )
    ):
        if (
            update.old_chat_member is None
            or update.old_chat_member.status in (
                ChatMemberStatus.LEFT,
                ChatMemberStatus.BANNED,
            )
        ):
            await app.send_message(
                update.chat.id,
                "👑 **Owner has arrived!**\nWelcome to the group ❤️",
            )


@app.on_message(filters.command("owner"))
async def owner_cmd(_, message: Message):
    text = (
        "<b>👑 ʙᴏᴛ ᴏᴡɴᴇʀ ᴘʀᴏғɪʟᴇ✨</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
        "✨ ᴛʜɪs ɪɴᴛᴇʟʟɪɢᴇɴᴛ ᴀɪ ʙᴏᴛ ɪs ᴘʀᴏᴜᴅʟʏ ᴄʀᴀғᴛᴇᴅ,\n"
        "ᴏᴡɴᴇᴅ ᴀɴᴅ ᴍᴀɴᴀɢᴇᴅ ʙʏ\n\n"
        f"👤 <b><a href='https://t.me/{OWNER_USERNAME}'>{OWNER_NAME}</a></b>\n"
        f"🔗 @{OWNER_USERNAME}\n\n"
        "🚀 ᴀ ᴘᴀssɪᴏɴᴀᴛᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ & ᴛᴇᴄʜ ᴇɴᴛʜᴜsɪᴀsᴛ\n"
        "• sᴍᴀʀᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴏɴ 🤖\n"
        "• sᴇᴄᴜʀᴇ sʏsᴛᴇᴍs 🔐\n"
        "• sᴍᴏᴏᴛʜ ᴜsᴇʀ ᴇxᴘᴇʀɪᴇɴᴄᴇ 💎\n\n"
        "💡 ᴠɪsɪᴏɴ\n"
        "ᴄʀᴇᴀᴛɪɴɢ ᴘᴏᴡᴇʀғᴜʟ, ʀᴇʟɪᴀʙʟᴇ ᴀɴᴅ\n"
        "ᴜsᴇʀ-ғʀɪᴇɴᴅʟʏ ᴀɪ ʙᴏᴛs\n"
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




