import random
from pyrogram import filters
from pyrogram.types import Message
from ShrutiMusic import app


def get_random_sticker():
    stickers = [
        "CAACAgQAAx0Ce9_hCAACaEVlwn7HeZhgwyVfKHc3WUGC_447IAACLgwAAkQwKVPtub8VAR018x4E",
        "CAACAgIAAx0Ce9_hCAACaEplwn7dvj7G0-a1v3wlbN281RMX2QACUgwAAligOUoi7DhLVTsNsh4E",
        "CAACAgIAAx0Ce9_hCAACaFBlwn8AAZNB9mOUvz5oAyM7CT-5pjAAAtEKAALa7NhLvbTGyDLbe1IeBA",
        "CAACAgUAAx0CcmOuMwACldVlwn9ZHHF2-S-CuMSYabwwtVGC3AACOAkAAoqR2VYDjyK6OOr_Px4E",
        "CAACAgIAAx0Ce9_hCAACaFVlwn-fG58GKoEmmZpVovxEj4PodAACfwwAAqozQUrt2xSTf5Ac4h4E",
    ]
    return random.choice(stickers)


def get_morning_emoji():
    return random.choice(["🌞", "🌅", "☀️", "😊"])


def get_night_emoji():
    return random.choice(["😴", "😪", "💤"])


# Good Morning
@app.on_message(filters.command(["gm", "goodmorning", "good_morning"]))
async def goodmorning_command_handler(_, message: Message):
    sender = message.from_user.mention

    if random.choice([True, False]):
        await app.send_sticker(message.chat.id, get_random_sticker())

    await message.reply_text(
        f"❖ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ❖ ʜᴀᴠᴇ ᴀ ɴɪᴄᴇ ᴅᴀʏ ❖\n\n"
        f"❍ {sender} {get_morning_emoji()}\n\n"
        f"❖ sᴛᴀʀᴛ ʏᴏᴜʀ ᴅᴀʏ ➥ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ 😊"
    )


# Good Night
@app.on_message(filters.command(["gn", "goodnight", "good_night"]))
async def goodnight_command_handler(_, message: Message):
    sender = message.from_user.mention

    if random.choice([True, False]):
        await app.send_sticker(message.chat.id, get_random_sticker())

    await message.reply_text(
        f"❖ ɢᴏᴏᴅ ɴɪɢʜᴛ ❖ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍs ❖\n\n"
        f"❍ {sender} {get_night_emoji()}\n\n"
        f"❖ ɢᴏ ᴛᴏ ➥ sʟᴇᴇᴘ ᴇᴀʀʟʏ"
    )
