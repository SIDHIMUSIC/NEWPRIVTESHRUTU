import asyncio
import random
import time

from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from py_yt import VideosSearch
import config
from ShrutiMusic import app
from ShrutiMusic.misc import _boot_
from ShrutiMusic.plugins.sudo.sudoers import sudoers_list
from ShrutiMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from ShrutiMusic.utils import bot_sys_stats
from ShrutiMusic.utils.decorators.language import LanguageStart
from ShrutiMusic.utils.formatters import get_readable_time
from ShrutiMusic.utils.inline import help_pannel_page1, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string


START_GREETS = [
    "✦ ʜᴇʏ",
    "✦ ᴡᴇʟᴄᴏᴍᴇ ʙᴀᴄᴋ",
    "✦ ɢʟᴀᴅ ʏᴏᴜ'ʀᴇ ʜᴇʀᴇ",
    "✦ ʜᴇʟʟᴏ",
    "✦ ɴᴀᴍᴀꜱᴛᴇ",
    "✦ ᴡᴇʟᴄᴏᴍᴇ",
]

START_MEDIA = [
    # Photos
    {"type": "photo", "url": config.START_IMG_URL},
    {"type": "photo", "url": "https://graph.org/file/de732e8e438bd2270fb5c-49eba2969fc27376c6.jpg"},
    {"type": "photo", "url": "https://graph.org/file/6f0488aeb917424f678fd-3d298edc245847ce1f.jpg"},
    {"type": "photo", "url": "https://graph.org/file/6df72e2743d0e28cfa12e-03dd7cd8478659cc81.jpg"},
    {"type": "photo", "url": "https://graph.org/file/89adae0b36f3c7ed61f8a-29971bd09b2b067b9e.jpg"},
    {"type": "photo", "url": "https://graph.org/file/0a598b51a872c36d2a9c5-4f4aa6e6de87bea8d6.jpg"},
    {"type": "photo", "url": "https://graph.org/file/556615482003de63f32be-58c192c7e65004f9d4.jpg"},
    # Videos
    {"type": "video", "url": "https://graph.org/file/8177ce4e792492d6a42b6-b0666d400e69ffa81b.mp4"},
    {"type": "video", "url": "https://graph.org/file/3d8d031febeba8b435af3-43c26bbac2b8a6e143.mp4"},
    {"type": "video", "url": "https://graph.org/file/881dae734ccdfb9c0eb02-f08c986bf85299fafd.mp4"},
    {"type": "video", "url": "https://graph.org/file/8946cb933256633309d39-ba922ab92fa6e204fc.mp4"},
    {"type": "video", "url": "https://graph.org/file/f85ba6c9b8841d847649d-06ed9f876d677105c4.mp4"},
    {"type": "video", "url": "https://graph.org/file/0b6c160a27eeb4a8c0097-4f36363c14cac9f01b.mp4"},
]


async def send_start_media(message: Message, caption: str, reply_markup=None):
    media = random.choice(START_MEDIA)
    try:
        if media["type"] == "video":
            return await message.reply_video(
                video=media["url"],
                caption=caption,
                reply_markup=reply_markup,
                parse_mode=ParseMode.HTML,
            )
        else:
            return await message.reply_photo(
                photo=media["url"],
                caption=caption,
                reply_markup=reply_markup,
                parse_mode=ParseMode.HTML,
            )
    except Exception:
        return await message.reply_photo(
            photo=config.START_IMG_URL,
            caption=caption,
            reply_markup=reply_markup,
            parse_mode=ParseMode.HTML,
        )


async def start_animation(message: Message):
    try:
        greet = random.choice(START_GREETS)
        vip = await message.reply_text(f"**{greet} {message.from_user.mention}**")
        await asyncio.sleep(0.3)
        await vip.edit_text(f"**{greet} {message.from_user.mention} ✨**")
        await asyncio.sleep(0.3)
        await vip.edit_text("**✦ ʟᴏᴀᴅɪɴɢ ᴘʀᴇᴍɪᴜᴍ ᴜɪ ...**")
        await asyncio.sleep(0.3)
        await vip.edit_text("**✦ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ ꜱᴇʀᴠᴇʀ ...**")
        await asyncio.sleep(0.3)
        await vip.edit_text("**✦ ꜱʏꜱᴛᴇᴍ ʀᴇᴀᴅʏ**")
        await asyncio.sleep(0.3)
        await vip.edit_text("**✦ ᴘʀᴀɢʏᴀ ᴍᴜꜱɪᴄ ɪꜱ ʀᴇᴀᴅʏ 🎵**")
        await asyncio.sleep(0.4)
        await vip.delete()

        done = await message.reply_text("❤️‍🔥")
        await asyncio.sleep(0.4)
        await done.delete()
    except Exception:
        pass


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    try:
        await message.react("❤️‍🔥")
    except Exception:
        pass

    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel_page1(_)
            return await send_start_media(
                message,
                _["help_1"].format(config.SUPPORT_GROUP),
                keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOG_GROUP_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n"
                         f"<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n"
                         f"<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                    parse_mode=ParseMode.HTML,
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_GROUP),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
                parse_mode=ParseMode.HTML,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOG_GROUP_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n"
                         f"<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n"
                         f"<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                    parse_mode=ParseMode.HTML,
                )
            return
        if name == "start":
            out = private_panel(_)
            UP, CPU, RAM, DISK = await bot_sys_stats()
            await start_animation(message)
            await send_start_media(
                message,
                _["start_2"].format(
                    message.from_user.mention, app.mention, UP, DISK, CPU, RAM
                ),
                InlineKeyboardMarkup(out),
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOG_GROUP_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n"
                         f"<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n"
                         f"<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                    parse_mode=ParseMode.HTML,
                )
            return
    else:
        out = private_panel(_)
        UP, CPU, RAM, DISK = await bot_sys_stats()
        await start_animation(message)
        await send_start_media(
            message,
            _["start_2"].format(
                message.from_user.mention, app.mention, UP, DISK, CPU, RAM
            ),
            InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOG_GROUP_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n"
                     f"<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n"
                     f"<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                parse_mode=ParseMode.HTML,
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await send_start_media(
        message,
        _["start_1"].format(app.mention, get_readable_time(uptime)),
        InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except Exception:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_GROUP,
                        ),
                        disable_web_page_preview=True,
                        parse_mode=ParseMode.HTML,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await send_start_media(
                    message,
                    _["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
