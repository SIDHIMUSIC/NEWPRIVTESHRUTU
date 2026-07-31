import asyncio
from pyrogram import filters
from pyrogram.types import Message
from ShrutiMusic import app
from ShrutiMusic.utils.database import get_assistant

OWNERS = [8170572505]  # list mein rakho


@app.on_message(filters.command("gadd") & filters.user(OWNERS))
async def add_all(_, message: Message):
    command_parts = message.text.split()
    if len(command_parts) != 2:
        await message.reply(
            "**⚠️ Invalid format.**\nUse: `/gadd @PRAGYA_ROBOT`"
        )
        return

    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0

        lol = await message.reply(f"🔄 **Adding {bot_username} in all chats...**")

        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1003389276372:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
            except Exception:
                failed += 1

            await lol.edit(
                f"**🔂 Adding {bot_username}**\n\n"
                f"**➥ Added in {done} chats ✅**\n"
                f"**➥ Failed in {failed} chats ❌**\n\n"
                f"**➲ By »** @{userbot.me.username}"
            )
            await asyncio.sleep(3)

        await lol.edit(
            f"**➻ {bot_username} added successfully 🎉**\n\n"
            f"**➥ Added in {done} chats ✅**\n"
            f"**➥ Failed in {failed} chats ❌**\n\n"
            f"**➲ By »** @{userbot.me.username}"
        )
    except Exception as e:
        await message.reply(f"**Error:** `{e}`")
