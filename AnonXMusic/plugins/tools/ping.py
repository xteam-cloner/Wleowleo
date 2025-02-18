from datetime import datetime
import asyncio
from platform import python_version as pyver
from pyrogram.enums import ChatType
from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver
from pytgcalls import __version__ as pytver
from pyrogram import filters
from pyrogram.types import Message
import config
from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils import bot_sys_stats
from AnonXMusic.utils.decorators.language import language
from AnonXMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL, OWNER_ID, SUPPORT_CHAT, BOT_USERNAME


@app.on_message(filters.command("ping") & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await Anony.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )


from AnonXMusic.utils.database import add_served_chat,add_served_user
#from MukeshRobot import SUPPORT_CHAT, pbot,BOT_USERNAME, OWNER_ID,BOT_NAME,START_IMG

async def member_permissions(chat_id: int, user_id: int):
    perms = []
    member = (await app.get_chat_member(chat_id, user_id)).privileges
    if not member:
        return []
    if member.can_post_messages:
        perms.append("can_post_messages")
    if member.can_edit_messages:
        perms.append("can_edit_messages")
    if member.can_delete_messages:
        perms.append("can_delete_messages")
    if member.can_restrict_members:
        perms.append("can_restrict_members")
    if member.can_promote_members:
        perms.append("can_promote_members")
    if member.can_change_info:
        perms.append("can_change_info")
    if member.can_invite_users:
        perms.append("can_invite_users")
    if member.can_pin_messages:
        perms.append("can_pin_messages")
    if member.can_manage_video_chats:
        perms.append("can_manage_video_chats")
    return perms

PHOTO = [
    "https://telegra.ph/file/d2a23fbe48129a7957887.jpg",
    "https://telegra.ph/file/ddf30888de58d77911ee1.jpg",
    "https://telegra.ph/file/268d66cad42dc92ec65ca.jpg",
    "https://telegra.ph/file/13a0cbbff8f429e2c59ee.jpg",
    "https://telegra.ph/file/bdfd86195221e979e6b20.jpg",
]

Xteam = [
    [
        InlineKeyboardButton(text="ɴᴏᴏʙ", user_id=OWNER_ID),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/xteam_cloner"),
    ],
    [
        InlineKeyboardButton(
            text="➕ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]



@app.on_message(filters.command("alive"))
async def alive(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(1)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(1)
    await accha.delete()
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await asyncio.sleep(1)
    await umm.delete()
    owner=await app.get_users(OWNER_ID)
    await m.reply_photo(
        PING_IMG_URL,
        caption=f"""<blockquote>» ʜᴇʏ, ɪ ᴀᴍ {app.mention}
   ━━━━━━━━━━━━━━━━━━━
  » ᴍʏ ᴏᴡɴᴇʀ : {owner.mention()}
  
  » ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ : {lver}
  
  » ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {tver}
  
  » ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ : {pver}
  
  » ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : {pyver()}
  
  » ᴘʏ-ᴛɢᴄᴀʟʟꜱ ᴠᴇʀꜱɪᴏɴ : {pytver}
   ━━━━━━━━━━━━━━━━━━━</blockquote>""",
        reply_markup=InlineKeyboardMarkup(Xteam)
    )

@app.on_message(group=1)
async def save_statss(_, m):
    try:
        if m.chat.type == ChatType.PRIVATE:
            add_served_user(m.from_user.id)
        elif m.chat.type==ChatType.SUPERGROUP:
            add_served_chat(m.chat.id)
        else:
            add_served_chat(m.chat.id)        

    except Exception as e:
        pass
       # await _.send_message(OWNER_ID,f"db error {e}")
