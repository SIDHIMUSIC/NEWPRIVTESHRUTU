import asyncio
from pyrogram import filters
from pyrogram.types import Message
from motor.motor_asyncio import AsyncIOMotorClient

import config
from ShrutiMusic import app
from config import OWNER_ID

# Purana DB jahan 2553 users hain
SOURCE_DB_NAME = "Yukki"

COLLECTIONS = [
    "tgusersdb",
    "chats",
    "sudoers",
    "blockedusers",
    "assistants",
]


@app.on_message(filters.command("migrate") & filters.user(OWNER_ID))
async def migrate_db(_, message: Message):
    status = await message.reply_text("⏳ <b>Migration start...</b>")

    try:
        client = AsyncIOMotorClient(config.MONGO_DB_URI)
        
        # source = Yukki
        source = client[SOURCE_DB_NAME]
        
        # target = jo DB ab bot use kar raha hai
        # URI mein /Yukki nahi hai to motor default DB leti hai
        target = client.get_default_database()
        if target is None:
            # fallback — apna current DB name yahan likho
            target = client["test"]

        lines = [f"📂 Source: <code>{SOURCE_DB_NAME}</code>"]
        lines.append(f"📁 Target: <code>{target.name}</code>\n")

        for name in COLLECTIONS:
            colls = await source.list_collection_names()
            if name not in colls:
                lines.append(f"⏭ {name}: not found")
                continue

            docs = await source[name].find({}).to_list(length=None)
            if not docs:
                lines.append(f"📭 {name}: 0 docs")
                continue

            # _id hata ke insert (duplicate avoid alag se)
            clean = []
            for d in docs:
                d = dict(d)
                d.pop("_id", None)
                clean.append(d)

            inserted = 0
            skipped = 0
            for d in clean:
                # users: user_id se check
                if name == "tgusersdb" and "user_id" in d:
                    exists = await target[name].find_one({"user_id": d["user_id"]})
                    if exists:
                        skipped += 1
                        continue
                elif name == "chats" and "chat_id" in d:
                    exists = await target[name].find_one({"chat_id": d["chat_id"]})
                    if exists:
                        skipped += 1
                        continue
                try:
                    await target[name].insert_one(d)
                    inserted += 1
                except Exception:
                    skipped += 1

            lines.append(f"✅ {name}: +{inserted} | skip {skipped} | total {len(docs)}")

        # final count
        try:
            u = await target["tgusersdb"].count_documents({})
            c = await target["chats"].count_documents({})
            lines.append(f"\n📊 Target ab: <b>{u}</b> users | <b>{c}</b> chats")
        except Exception:
            pass

        await status.edit_text("\n".join(lines))
    except Exception as e:
        await status.edit_text(f"❌ Error:\n<code>{e}</code>")


@app.on_message(filters.command("dbinfo") & filters.user(OWNER_ID))
async def db_info(_, message: Message):
    try:
        client = AsyncIOMotorClient(config.MONGO_DB_URI)
        target = client.get_default_database()
        if target is None:
            target = client["test"]

        yukki = client["Yukki"]
        yu = await yukki["tgusersdb"].count_documents({})
        yc = await yukki["chats"].count_documents({}) if "chats" in await yukki.list_collection_names() else 0

        tu = await target["tgusersdb"].count_documents({}) if "tgusersdb" in await target.list_collection_names() else 0
        tc = await target["chats"].count_documents({}) if "chats" in await target.list_collection_names() else 0

        await message.reply_text(
            f"🗂 <b>DB INFO</b>\n\n"
            f"<b>Yukki:</b> {yu} users | {yc} chats\n"
            f"<b>Current ({target.name}):</b> {tu} users | {tc} chats\n\n"
            f"URI default DB: <code>{target.name}</code>"
        )
    except Exception as e:
        await message.reply_text(f"Error: {e}")
