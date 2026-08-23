from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.enums import ParseMode

from ShrutiMusic import app
import config

PE = {
    "lock": "5291873529464122510",
    "doc": "5357315181649076022",
    "support": "5301096984617166561",
    "user": "5208604387156448480",
}


def pe(name: str, fallback: str = "👀") -> str:
    eid = PE.get(name)
    if not eid:
        return fallback
    return f'<emoji id="{eid}">{fallback}</emoji>'


@app.on_message(filters.command(["privacy", "Privacy"]))
async def privacy(client, message: Message):
    text = (
        f"{pe('lock', '🔒')} <b>Privacy Policy for {app.mention}</b>\n\n"
        f"Your privacy is important to us. To learn more about how we collect, "
        f"use, and protect your data, please review our Privacy Policy.\n\n"
        f"{pe('user', '👤')} If you have any questions, contact our "
        f"<a href=\"https://t.me/HARRYASHU\">support team</a>."
    )

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="View Privacy Policy",
                    url=config.PRIVACY_LINK,
                    icon_custom_emoji_id=int(PE["doc"]),
                )
            ],
            [
                InlineKeyboardButton(
                    text="Support",
                    url=config.SUPPORT_GROUP,
                    icon_custom_emoji_id=int(PE["support"]),
                )
            ],
        ]
    )

    await message.reply_text(
        text,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )
