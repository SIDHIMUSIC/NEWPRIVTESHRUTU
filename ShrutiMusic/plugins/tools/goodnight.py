import random
from pyrogram import filters
from pyrogram.types import Message
from ShrutiMusic import app

# ------------------ STICKERS ------------------

MORNING_STICKERS = [
    "CAACAgUAAxkBAAEFywJqaqDVlAAB4--LikTmdBzvXLQwfAADghAAAv5P-Fd7RWzhbK6qfz0E",
    "CAACAgUAAxkBAAEFywRqaqDxkqtsXjBMbOVn6jU6Jnv0SQAC1xIAAsLb-FdlII0pgKoyJD0E",
    "CAACAgUAAxkBAAEFywZqaqEKMrvUFPc0BLHy6M7-ZU7eDQACDxMAAm3G-FfhbWLirz0OQj0E",
    "CAACAgUAAxkBAAEFywhqaqEp38zc-inKk4Jrxc61QS8VJwACNBQAAsqW8FdUQcNjlgZtnD0E",
]

NIGHT_STICKERS = [
    "CAACAgQAAx0Ce9_hCAACaEVlwn7HeZhgwyVfKHc3WUGC_447IAACLgwAAkQwKVPtub8VAR018x4E",
    "CAACAgIAAx0Ce9_hCAACaEplwn7dvj7G0-a1v3wlbN281RMX2QACUgwAAligOUoi7DhLVTsNsh4E",
    "CAACAgIAAx0Ce9_hCAACaFBlwn8AAZNB9mOUvz5oAyM7CT-5pjAAAtEKAALa7NhLvbTGyDLbe1IeBA",
    "CAACAgUAAx0CcmOuMwACldVlwn9ZHHF2-S-CuMSYabwwtVGC3AACOAkAAoqR2VYDjyK6OOr_Px4E",
    "CAACAgIAAx0Ce9_hCAACaFVlwn-fG58GKoEmmZpVovxEj4PodAACfwwAAqozQUrt2xSTf5Ac4h4E",
]

# ------------------ EMOJIS ------------------

MORNING_EMOJIS = ["🌞", "🌅", "☀️", "😊"]
NIGHT_EMOJIS = ["😴", "😪", "💤"]


async def send_morning(message: Message):
    sender = message.from_user.mention

    if MORNING_STICKERS:
        await app.send_sticker(
            message.chat.id,
            random.choice(MORNING_STICKERS)
        )

    await message.reply_text(
        f"❖ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ❖ ʜᴀᴠᴇ ᴀ ɴɪᴄᴇ ᴅᴀʏ ❖\n\n"
        f"❍ {sender} {random.choice(MORNING_EMOJIS)}\n\n"
        f"❖ sᴛᴀʀᴛ ʏᴏᴜʀ ᴅᴀʏ ➥ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ 😊"
    )


async def send_night(message: Message):
    sender = message.from_user.mention

    await app.send_sticker(
        message.chat.id,
        random.choice(NIGHT_STICKERS)
    )

    await message.reply_text(
        f"❖ ɢᴏᴏᴅ ɴɪɢʜᴛ ❖ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs ❖\n\n"
        f"❍ {sender} {random.choice(NIGHT_EMOJIS)}\n\n"
        f"❖ ɢᴏ ᴛᴏ ➥ sʟᴇᴇᴘ ᴇᴀʀʟʏ"
    )


# /gm
@app.on_message(filters.command(["gm", "goodmorning"]))
async def gm_cmd(_, message: Message):
    await send_morning(message)


# /gn
@app.on_message(filters.command(["gn", "goodnight"]))
async def gn_cmd(_, message: Message):
    await send_night(message)


# gm (without /)
@app.on_message(
    filters.regex(r"^(?i)(gm|good morning|Gm|Goodmorning|goodmorning)$"))
async def gm_text(_, message: Message):
    await send_morning(message)


# gn (without /)
@app.on_message(
    filters.regex(r"^(?i)(gn|Goodnight|Gn|good night|goodnight)$")
)
async def gn_text(_, message: Message):
    await send_night(message)
