from pyrogram import filters
from pyrogram.types import Message
from motor.motor_asyncio import AsyncIOMotorClient

import config
from ShrutiMusic import app

try:
    from config import OWNER_ID
except Exception:
    OWNER_ID = []

# agar OWNER_ID int hai to list bana do
if isinstance(OWNER_ID, int):
    OWNERS = [OWNER_ID]
else:
    OWNERS = list(OWNER_ID) if OWNER_ID else []

SOURCE_DB = "Yukki"
# jab URI mein DB name na ho to motor aksar 'test' use karta hai
FALLBACK_TARGET = "test"

COLLECTIONS = [
    "tgusersdb",
    "chats",
    "sudoers",
    "blockedusers",
    "assistants",
]


def _client():
    # config se URI lo (Heroku Config Vars)
    uri = getattr(config, "MONGO_DB_URI", None) or getattr(config, "MONGO_URL", None)
    if not uri:
        raise RuntimeError("MONGO_DB_URI not found in config")
    return AsyncIOMotorClient(uri)


@app.on_message(filters.command(["dbinfo"]) & filters.user(OWNERS))
async def db_info(_, message: Message):
    try:
        client = _client()
        source = client[SOURCE_DB]
        target = client.get_default_database()
        if target is None:
            target = client[FALLBACK_TARGET]

        src_users = await source["tgusersdb"].count_documents({})
        src_chats = (
            await source["chats"].count_documents({})
            if "chats" in await source.list_collection_names()
            else 0
        )

        t_cols = await target.list_collection_names()
        tgt_users = (
            await target["tgusersdb"].count_documents({})
            if "tgusersdb" in t_cols
            else 0
        )
        tgt_chats = (
            await target["chats"].count_documents({}) if "chats" in t_cols else 0
        )

        await message.reply_text(
            f"🗂 <b>DB INFO</b>\n\n"
            f"<b>Source ({SOURCE_DB}):</b>\n"
            f"• Users: <code>{src_users}</code>\n"
            f"• Chats: <code>{src_chats}</code>\n\n"
            f"<b>Target ({target.name}):</b>\n"
            f"• Users: <code>{tgt_users}</code>\n"
            f"• Chats: <code>{tgt_chats}</code>\n\n"
            f"➡ Ab <code>/migrate</code> chalao"
        )
    except Exception as e:
        await message.reply_text(f"❌ <code>{e}</code>")


@app.on_message(filters.command(["migrate"]) & filters.user(OWNERS))
async def migrate_db(_, message: Message):
    status = await message.reply_text("⏳ <b>Migrating from Yukki...</b>")
    try:
        client = _client()
        source = client[SOURCE_DB]
        target = client.get_default_database()
        if target is None:
            target = client[FALLBACK_TARGET]

        if source.name == target.name:
            return await status.edit_text(
                "⚠️ Source aur Target same DB hain.\n"
                "URI mein DB name hatao ya target alag karo."
            )

        lines = [
            f"📂 <b>Source:</b> <code>{source.name}</code>",
            f"📁 <b>Target:</b> <code>{target.name}</code>",
            "",
        ]

        src_cols = await source.list_collection_names()

        for name in COLLECTIONS:
            if name not in src_cols:
                lines.append(f"⏭ <code>{name}</code>: not in Yukki")
                continue

            docs = await source[name].find({}).to_list(length=None)
            if not docs:
                lines.append(f"📭 <code>{name}</code>: 0")
                continue

            inserted = 0
            skipped = 0

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
        lines.append(f"\n📊 <b>Target now:</b> {tu} users | {tc} chats")

        await status.edit_text("\n".join(lines))
    except Exception as e:
        await status.edit_text(f"❌ <code>{e}</code>")
