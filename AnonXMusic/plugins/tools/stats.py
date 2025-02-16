import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import InputMediaPhoto, Message
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
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

# Callback data
PING_CALLBACK = "ping_dialog"

@app.on_message(filters.command(["stats", "gstats"]) & filters.group & ~BANNED_USERS)
@language
async def stats_global(client, message: Message, _):
    response = await message.reply_photo(
        photo=config.STATS_IMG_URL,
        caption=_["gstats_2"].format(app.mention),
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔍 Check Ping", callback_data=PING_CALLBACK)]]
        ),
    )

@app.on_callback_query(filters.regex(PING_CALLBACK))
async def overall_stats(client, callback_query: CallbackQuery):
    await CallbackQuery.edit_message_text(_["gstats_1"].format(app.mention))
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    
    text = _["gstats_3"].format(
        app.mention,
        len(assistants),
        len(BANNED_USERS),
        served_chats,
        served_users,
        len(ALL_MODULES),
        len(SUDOERS),
        config.AUTO_LEAVING_ASSISTANT,
        config.DURATION_LIMIT_MIN,
    )
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text,   reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔍 Check Ping", callback_data=PING_CALLBACK)]]
        ),
        )


@app.on_callback_query()
async def callback_query(client, callback_query):
    if callback_query.data == "bot_stats_sudo":
        await callback_query.message.reply(_["gstats_1"].format(app.mention))
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
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
    text = _["gstats_5"].format(
        app.mention,
        len(ALL_MODULES),
        platform.system(),
        ram,
        p_core,
        t_core,
        cpu_freq,
        pyver.split()[0],
        pyrover,
        pytgver,
        str(total)[:4],
        str(used)[:4],
        str(free)[:4],
        served_chats,
        served_users,
        len(BANNED_USERS),
        len(await get_sudoers()),
        str(datasize)[:6],
        storage,
        call["collections"],
        call["objects"],
    )
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text, reply_markup=upl
        )
