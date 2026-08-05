import random
import pyrogram
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from ..logging import LOGGER


BOOT_MEDIA = [
    "https://graph.org/file/8177ce4e792492d6a42b6-b0666d400e69ffa81b.mp4",
    "https://graph.org/file/3d8d031febeba8b435af3-43c26bbac2b8a6e143.mp4",
    "https://graph.org/file/881dae734ccdfb9c0eb02-f08c986bf85299fafd.mp4",
    "https://graph.org/file/8946cb933256633309d39-ba922ab92fa6e204fc.mp4",
    "https://graph.org/file/f85ba6c9b8841d847649d-06ed9f876d677105c4.mp4",
    "https://graph.org/file/0b6c160a27eeb4a8c0097-4f36363c14cac9f01b.mp4",
]


class Nand(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting bot...")
        super().__init__(
            name="ShrutiMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = self.me.mention

        button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="⦿ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ⦿",
                        url=f"https://t.me/{self.username}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="📢 ꜱᴜᴘᴘᴏʀᴛ",
                        url=config.SUPPORT_CHANNEL,
                    ),
                    InlineKeyboardButton(
                        text="💬 ɢʀᴏᴜᴘ",
                        url=config.SUPPORT_GROUP,
                    ),
                ],
            ]
        )

        caption = (
            f"<b>✦ ᴘʀᴀɢʏᴀ ᴍᴜꜱɪᴄ ᴏɴʟɪɴᴇ</b>\n"
            f"━━━━━━━━━━━━━━━━━━\n\n"
            f"<b>🎵 ɴᴀᴍᴇ :</b> {self.name}\n"
            f"<b>🔗 ᴜꜱᴇʀɴᴀᴍᴇ :</b> @{self.username}\n"
            f"<b>🆔 ɪᴅ :</b> <code>{self.id}</code>\n\n"
            f"<b>⚡ ꜱᴛᴀᴛᴜꜱ :</b> <code>ʀᴜɴɴɪɴɢ</code>\n"
            f"<b>💎 ᴍᴏᴅᴇ :</b> <code>ᴘʀᴇᴍɪᴜᴍ</code>\n\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"<i>✦ ʙᴏᴛ ɪꜱ ʀᴇᴀᴅʏ ᴛᴏ ꜱᴇʀᴠᴇ ✨</i>"
        )

        if config.LOG_GROUP_ID:
            try:
                await self.send_video(
                    config.LOG_GROUP_ID,
                    video=random.choice(BOOT_MEDIA),
                    caption=caption,
                    reply_markup=button,
                )
            except Exception:
                try:
                    await self.send_photo(
                        config.LOG_GROUP_ID,
                        photo=config.START_IMG_URL,
                        caption=caption,
                        reply_markup=button,
                    )
                except pyrogram.errors.ChatWriteForbidden:
                    LOGGER(__name__).error("Bot cannot write to the log group")
                except Exception as e:
                    LOGGER(__name__).error(f"Error while sending to log group: {e}")
        else:
            LOGGER(__name__).warning("LOG_GROUP_ID is not set")

        if config.LOG_GROUP_ID:
            try:
                chat_member_info = await self.get_chat_member(
                    config.LOG_GROUP_ID, self.id
                )
                if chat_member_info.status != ChatMemberStatus.ADMINISTRATOR:
                    LOGGER(__name__).error("Please promote Bot as Admin in Logger Group")
            except Exception as e:
                LOGGER(__name__).error(f"Error checking bot status: {e}")

        LOGGER(__name__).info(f"Music Bot Started as {self.name}")

    async def stop(self):
        await super().stop()
