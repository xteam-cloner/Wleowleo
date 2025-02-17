from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app


start_txt = """
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

̶꯭꯭⎯̶꯭̽❝꯭꯭♥️xᴛᴇᴀᴍ ᴍᴜsɪᴄ 🥀🤍꯭᪳𝆺̶꯭𝅥⎯̶̶꯭̽

❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ 🇹‌𝗵𝗮𝗻𝘂 ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ support.
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("owner", url="https://t.me/teamx-clone"),
          InlineKeyboardButton("repo", url="https://t.me/teamx-clone"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/S7U.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
