from typing import Union

from pyrogram import filters, types
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, Message

from ShrutiMusic import app
from ShrutiMusic.utils.database import get_lang
from ShrutiMusic.utils.decorators.language import LanguageStart, languageCB
from ShrutiMusic.utils.inline.help import (
    help_back_markup,
    private_help_panel,
    help_pannel_page1,
    help_pannel_page2,
    help_pannel_page3,
    help_pannel_page4,
)
from config import BANNED_USERS, START_IMG_URL, SUPPORT_GROUP
from strings import get_string, helpers


def _page_keyboard(page: int, _, start: bool = False):
    if page == 2:
        return help_pannel_page2(_, start)
    if page == 3:
        return help_pannel_page3(_, start)
    if page == 4:
        return help_pannel_page4(_, start)
    return help_pannel_page1(_, start)


async def _edit_help(update, text, keyboard):
    msg = update.message
    try:
        if msg.photo:
            await update.edit_message_caption(
                caption=text,
                reply_markup=keyboard,
                parse_mode=ParseMode.HTML,
            )
        else:
            await update.edit_message_text(
                text,
                reply_markup=keyboard,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
    except Exception:
        await update.edit_message_text(
            text,
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex(r"^help_page_1$") & ~BANNED_USERS)
async def helper_private(client, update: Union[types.Message, types.CallbackQuery]):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except Exception:
            pass
        language = await get_lang(update.message.chat.id)
        _ = get_string(language)
        await _edit_help(
            update,
            _["help_1"].format(SUPPORT_GROUP),
            help_pannel_page1(_, True),
        )
        return

    try:
        await update.delete()
    except Exception:
        pass
    language = await get_lang(update.chat.id)
    _ = get_string(language)
    await update.reply_photo(
        photo=START_IMG_URL,
        caption=_["help_1"].format(SUPPORT_GROUP),
        reply_markup=help_pannel_page1(_),
        parse_mode=ParseMode.HTML,
    )


@app.on_callback_query(filters.regex(r"^help_page_2$") & ~BANNED_USERS)
async def helper_page2(client, update: types.CallbackQuery):
    try:
        await update.answer()
    except Exception:
        pass
    language = await get_lang(update.message.chat.id)
    _ = get_string(language)
    await _edit_help(update, _["help_1"].format(SUPPORT_GROUP), help_pannel_page2(_, True))


@app.on_callback_query(filters.regex(r"^help_page_3$") & ~BANNED_USERS)
async def helper_page3(client, update: types.CallbackQuery):
    try:
        await update.answer()
    except Exception:
        pass
    language = await get_lang(update.message.chat.id)
    _ = get_string(language)
    await _edit_help(update, _["help_1"].format(SUPPORT_GROUP), help_pannel_page3(_, True))


@app.on_callback_query(filters.regex(r"^help_page_4$") & ~BANNED_USERS)
async def helper_page4(client, update: types.CallbackQuery):
    try:
        await update.answer()
    except Exception:
        pass
    language = await get_lang(update.message.chat.id)
    _ = get_string(language)
    await _edit_help(update, _["help_1"].format(SUPPORT_GROUP), help_pannel_page4(_, True))


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(
        _["help_2"],
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    cb = CallbackQuery.data.strip().split(None, 1)[1]

    page1 = {f"hb{i}" for i in range(1, 11)}
    page2 = {f"hb{i}" for i in range(11, 21)}
    page3 = {f"hb{i}" for i in range(21, 31)}
    page4 = {f"hb{i}" for i in range(31, 40)}

    if cb in page2:
        page = 2
    elif cb in page3:
        page = 3
    elif cb in page4:
        page = 4
    else:
        page = 1

    texts = {
        "hb1": helpers.HELP_1,
        "hb2": helpers.HELP_2,
        "hb3": helpers.HELP_3,
        "hb4": helpers.HELP_4,
        "hb5": helpers.HELP_5,
        "hb6": helpers.HELP_6,
        "hb7": helpers.HELP_7,
        "hb8": helpers.HELP_8,
        "hb9": helpers.HELP_9,
        "hb10": helpers.HELP_10,
        "hb11": helpers.HELP_11,
        "hb12": helpers.HELP_12,
        "hb13": helpers.HELP_13,
        "hb14": helpers.HELP_14,
        "hb15": helpers.HELP_15,
        "hb16": helpers.HELP_16,
        "hb17": helpers.HELP_17,
        "hb18": helpers.HELP_18,
        "hb19": helpers.HELP_19,
        "hb20": helpers.HELP_20,
        "hb21": helpers.HELP_21,
        "hb22": helpers.HELP_22,
        "hb23": helpers.HELP_23,
        "hb24": helpers.HELP_24,
        "hb25": helpers.HELP_25,
        "hb26": helpers.HELP_26,
        "hb27": helpers.HELP_27,
        "hb28": helpers.HELP_28,
        "hb29": helpers.HELP_29,
        "hb30": helpers.HELP_30,
        "hb31": helpers.HELP_31,
        "hb32": helpers.HELP_32,
        "hb33": helpers.HELP_33,
        "hb34": helpers.HELP_34,
        "hb35": helpers.HELP_35,
        "hb36": helpers.HELP_36,
        "hb37": helpers.HELP_37,
        "hb38": helpers.HELP_38,
        "hb39": helpers.HELP_39,
    }

    text = texts.get(cb)
    if not text:
        return
    await CallbackQuery.edit_message_text(
        text,
        reply_markup=help_back_markup(_, page=page),
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )
