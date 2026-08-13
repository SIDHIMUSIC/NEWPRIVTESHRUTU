from pyrogram import filters
from pyrogram.types import Message
from motor.motor_asyncio import AsyncIOMotorClient

import config
from ShrutiMusic import app

try:
    from config import OWNER_ID
except Exception:
    OWNER_ID = []

if isinstance(OWNER_ID, int):
    OWNERS = [OWNER_ID]
else:
    OWNERS = list(OWNER_ID) if OWNER_ID else []

SOURCE_DB = "Yukki"
# bot ke core/mongo.py mein jo naam hai wahi yahan likho
# tumhare repo mein: mongodb = _mongo_async_.Yukki
TARGET_DB = "Yukki"

COLLECTIONS = [
    "tgusersdb",
    "chats",
    "sudoers",
    "blockedusers",
    "assistants",
]


def _client():
    uri = getattr(config, "MONGO_DB_URI", None) or getattr(config, "MONGO_URL", None)
    if not uri:
        raise RuntimeError("MONGO_DB_URI not found in config")
    return AsyncIOMotorClient(uri)


@app.on_message(filters.command(["dbinfo"]) & filters.user(OWNERS))
async def db_info(_, message: Message):
    try:
        client = _client()
        source = client[SOURCE_DB]
        target = client[TARGET_DB]

        src_cols = await source.list_collection_names()
        t_cols = await target.list_collection_names()

        src_users = await source["tgusersdb"].count_documents({}) if "tgusersdb" in src_cols else 0
        src_chats = await source["chats"].count_documents({}) if "chats" in src_cols else 0
        tgt_users = await target["tgusersdb"].count_documents({}) if "tgusersdb" in t_cols else 0
        tgt_chats = await target["chats"].count_documents({}) if "chats" in t_cols else 0

        await message.reply_text(
            f"🗂 <b>DB INFO</b>\n\n"
            f"<b>Source ({SOURCE_DB}):</b>\n"
            f"• Users: <code>{src_users}</code>\n"
            f"• Chats: <code>{src_chats}</code>\n\n"
            f"<b>Target ({TARGET_DB}):</b>\n"
            f"• Users: <code>{tgt_users}</code>\n"
            f"• Chats: <code>{tgt_chats}</code>\n\n"
            f"{'⚠️ Source = Target (same DB)' if SOURCE_DB == TARGET_DB else '➡ /migrate chalao'}"
        )
    except Exception as e:
        await message.reply_text(f"❌ <code>{e}</code>")


@app.on_message(filters.command(["migrate"]) & filters.user(OWNERS))
async def migrate_db(_, message: Message):
    if SOURCE_DB == TARGET_DB:
        return await message.reply_text(
            "⚠️ Source aur Target dono <b>Yukki</b> hain.\n"
            "Bot pehle se Yukki use karta hai.\n\n"
            "Check karo: <code>ShrutiMusic/core/mongo.py</code>\n"
            "<code>mongodb = _mongo_async_.Yukki</code>\n\n"
            "Agar /stats kam dikha raha hai to alag issue hai, migrate se fix nahi hoga."
        )

    status = await message.reply_text("⏳ <b>Migrating...</b>")
    try:
        client = _client()
        source = client[SOURCE_DB]
        target = client[TARGET_DB]

        lines = [
            f"📂 Source: <code>{SOURCE_DB}</code>",
            f"📁 Target: <code>{TARGET_DB}</code>",
            "",
        ]
        src_cols = await source.list_collection_names()

        for name in COLLECTIONS:
            if name not in src_cols:
                lines.append(f"⏭ <code>{name}</code>: not found")
                continue

            docs = await source[name].find({}).to_list(length=None)
            if not docs:
                lines.append(f"📭 <code>{name}</code>: 0")
                continue

            inserted = skipped = 0
            for d in docs:
                d = dict(d)
                d.pop("_id", None)

                if name == "tgusersdb" and "user_id" in d:
                    if await target[name].find_one({"user_id": d["user_id"]}):
                        skipped += 1
                        continue
                elif name == "chats" and "chat_id" in d:
                    if await target[name].find_one({"chat_id": d["chat_id"]}):
                        skipped += 1
                        continue

                try:
                    await target[name].insert_one(d)
                    inserted += 1
                except Exception:
                    skipped += 1

            lines.append(
                f"✅ <code>{name}</code>: +{inserted} | skip {skipped} | src {len(docs)}"
            )

        t_cols = await target.list_collection_names()
        tu = await target["tgusersdb"].count_documents({}) if "tgusersdb" in t_cols else 0
        tc = await target["chats"].count_documents({}) if "chats" in t_cols else 0
        lines.append(f"\n📊 Target now: <b>{tu}</b> users | <b>{tc}</b> chats")
        await status.edit_text("\n".join(lines))
    except Exception as e:
        await status.edit_text(f"❌ <code>{e}</code>")
