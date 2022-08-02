from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client


ANON = "https://telegra.ph/file/90552395a5e96d0e7fab9.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [Group manegement](t.me/lovely420_bot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [꧁༒︎༒︎༆༆𝚂𝚒𝚟𝚊𝚝𝚑𝚎𝚔𝚒𝚗𝚐༆༆༒︎༒︎꧂](t.me/Sivatheking_1)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**Group management bot sᴏᴜʀᴄᴇ ɪs ᴘʀɪᴠᴀᴛᴇ 🥺 sᴏʀʀʏ ʙᴜᴛ ᴜ ᴄᴀɴ ᴜsᴇ Group manegement bot ғᴏʀ ɢʀᴏᴜᴘs.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("•👑 ᴏᴡɴᴇʀ ʟᴇɢᴇɴᴅ 👑•", url="https://t.me/Sivatheking_1"
                    ),
                    InlineKeyboardButton(
                        "•💚sᴜᴘᴘᴏʀᴛ💚•",
                        url="https://t.me/pyrogram_support"
                    ),
                ],
                [
                    InlineKeyboardButton("• ➕ ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ➕ •", url="https://t.me/Lovely420_bot?startgroup=true"),     
                ],
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"

