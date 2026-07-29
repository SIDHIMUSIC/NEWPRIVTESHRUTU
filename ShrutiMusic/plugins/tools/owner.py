from pyrogram import filters
from pyrogram.types import (
    Message,
    ChatMemberUpdated,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from pyrogram.enums import ChatMemberStatus
from ShrutiMusic import app

OWNER_ID = 8170572505
OWNER_USERNAME = "SANATANI_BACCHA"


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
        # only when owner newly joins (not already was member)
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
    await message.reply_photo(
        photo="https://telegra.ph/file/41ec8f174b98e691047f7.png",
        caption="👑 **Bot Owner**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👑 Owner",
                        url=f"https://t.me/{OWNER_USERNAME}",
                    )
                ]
            ]
        ),
    )
