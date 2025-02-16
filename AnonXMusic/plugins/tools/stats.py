import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import InputMediaPhoto, Message
from pytgcalls.__version__ import __version__ as pytgver

import config
from AnonXMusic import app
from AnonXMusic.core.userbot import assistants
from AnonXMusic.misc import SUDOERS, mongodb
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from AnonXMusic.utils.decorators.language import language, languageCB
from AnonXMusic.utils.inline.stats import back_stats_buttons, stats_buttons
from config import BANNED_USERS


@app.on_message(filters.command(["stats", "gstats"]) & filters.group & ~BANNED_USERS)
@language
async def stats_global(client, message: Message, _):
    upl = stats_buttons(_, True if message.from_user.id in SUDOERS else False)
    await message.reply_photo(
        photo=config.STATS_IMG_URL,
        caption=_["gstats_2"].format(app.mention),
        reply_markup=upl,
    )


@app.on_callback_query(filters.regex("stats_back") & ~BANNED_USERS)
@languageCB
async def home_stats(client, CallbackQuery, _):
    upl = stats_buttons(_, True if CallbackQuery.from_user.id in SUDOERS else False)
    await CallbackQuery.edit_message_text(
        text=_["gstats_2"].format(app.mention),
        reply_markup=upl,
    )


@app.on_callback_query(filters.regex("TopOverall") & ~BANNED_USERS)
@languageCB
async def overall_stats(client, CallbackQuery, _):
    # Allow sudo users and owner to use it from anywhere
    if CallbackQuery.from_user.id not in SUDOERS and CallbackQuery.from_user.id != OWNER_ID:
        if CallbackQuery.message.chat.username != "dragbackup":
            return await CallbackQuery.answer(
                "Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ @ᴅʀᴀɢʙᴀᴄᴋᴜᴘ.",
                show_alert=True,
            )

    # Fetch necessary stats
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    assistants_count = len(assistants)
    blocked_users = len(BANNED_USERS)
    modules_count = len(ALL_MODULES)
    sudoers_count = len(SUDOERS)

    # Short message for the pop-up (must be under 200 characters)
    text = (
        f"📊 Overall Stats 📊\n\n"
        f"🤖 Assistants: {assistants_count}\n"
        f"🚫 Blocked Users: {blocked_users}\n"
        f"📌 Active Chats: {served_chats}\n"
        f"🛠 Modules: {modules_count}\n"
        f"👑 Sudoers: {sudoers_count}"
    )

    await CallbackQuery.answer(text, show_alert=True)


"""@app.on_callback_query(filters.regex("bot_stats_sudo"))
@languageCB
async def bot_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id not in SUDOERS and CallbackQuery.from_user.id != OWNER_ID:
        if CallbackQuery.message.chat.username != "dragbackup":
            return await CallbackQuery.answer(
                "Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ɪɴ @ᴅʀᴀɢʙᴀᴄᴋᴜᴘ.",
                show_alert=True,
            )
        
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    used = hdd.used / (1024.0**3)
    free = hdd.free / (1024.0**3)
    call = await mongodb.command("dbstats")
    datasize = call["dataSize"] / 1024
    storage = call["storageSize"] / 1024
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    
    text = ("<b><u>{0} sᴛᴀᴛs ᴀɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :</u></b>\n\n<b>ᴍᴏᴅᴜʟᴇs :</b> <code>{1}</code>\n<b>ᴘʟᴀᴛғᴏʀᴍ :</b> <code>{2}</code>\n<b>ʀᴀᴍ :</b> <code>{3}</code>\n<b>ᴘʜʏsɪᴄᴀʟ ᴄᴏʀᴇs :</b> <code>{4}</code>\n<b>ᴛᴏᴛᴀʟ ᴄᴏʀᴇs :</b> <code>{5}</code>\n<b>ᴄᴘᴜ ғʀᴇǫᴜᴇɴᴄʏ :</b> <code>{6}</code>\n\n<b>ᴘʏᴛʜᴏɴ :</b> <code>{7}</code>\n<b>ᴘʏʀᴏɢʀᴀᴍ :</b> <code>{8}</code>\n<b>ᴘʏ-ᴛɢᴄᴀʟʟs :</b> <code>{9}</code>\n\n<b>sᴛᴏʀᴀɢᴇ ᴀᴠᴀɪʟᴀʙʟᴇ :</b> <code>{10} ɢɪʙ</code>\n<b>sᴛᴏʀᴀɢᴇ ᴜsᴇᴅ :</b> <code>{11} ɢɪʙ</code>\n<b>sᴛᴏʀᴀɢᴇ ʟᴇғᴛ :</b> <code>{12} ɢɪʙ</code>\n\n<b>sᴇʀᴠᴇᴅ ᴄʜᴀᴛs :</b> <code>{13}</code>\n<b>sᴇʀᴠᴇᴅ ᴜsᴇʀs :</b> <code>{14}</code>\n<b>ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs :</b> <code>{15}</code>\n<b>sᴜᴅᴏ ᴜsᴇʀs :</b> <code>{16}</code>\n\n<b>ᴛᴏᴛᴀʟ ᴅʙ sɪᴢᴇ :</b> <code>{17} ᴍʙ</code>\n<b>ᴛᴏᴛᴀʟ ᴅʙ sᴛᴏʀᴀɢᴇ :</b> <code>{18} ᴍʙ</code>\n<b>ᴛᴏᴛᴀʟ ᴅʙ ᴄᴏʟʟᴇᴄᴛɪᴏɴs :</b> <code>{19}</code>\n<b>ᴛᴏᴛᴀʟ ᴅʙ ᴋᴇʏs :</b> <code>{20}</code>")
        med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(media=med)
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text)
"""
