from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import sudo_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ **Welcome {message.from_user.first_name}** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME})𝐀𝐥𝐥𝐨𝐰 𝐘𝐨𝐮 𝐓𝐨 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐎𝐧 𝐆𝐫𝐨𝐮𝐩𝐬 𝐓𝐡𝐫𝐨𝐮𝐠𝐡 𝐓𝐡𝐞 𝐍𝐞𝐰 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦'𝐬 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭𝐬 😇

💡 𝐅𝐢𝐧𝐝 𝐎𝐮𝐭 𝐀𝐥𝐥 𝐓𝐡𝐞 𝐁𝐨𝐭'𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐀𝐧𝐝 𝐇𝐨𝐰 𝐓𝐡𝐞𝐲 𝐖𝐨𝐫𝐤 𝐁𝐲 𝐂𝐥𝐢𝐜𝐤𝐢𝐧𝐠 𝐎𝐧 𝐓𝐡𝐞 » 📚 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 !

❓ 𝐅𝐨𝐫 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧 𝐀𝐛𝐨𝐮𝐭 𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞 𝐎𝐟 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭, 𝐉𝐮𝐬𝐭 𝐓𝐲𝐩𝐞 /help

🥀 𝐃𝐄𝐕𝐎𝐋𝐎𝐏𝐄𝐑: @akshhhxx 🖤
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    
                ]
            ]
        ),
     disable_web_page_preview=FALSE
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **bot is running**\n<b>💠 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "💥 Hᴏᴡ Tᴏ Usᴇ Mᴇ", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "💫 Cᴏᴍᴍᴀɴᴅs", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "🥀 𝗢𝗪𝗡𝗘𝗥", url=f"https://t.me/akshhhxx")
                ],[
                    InlineKeyboardButton(
                        "👥 Oғғɪᴄɪᴀʟ Gʀᴏᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Oғғɪᴄɪᴀʟ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}")
              
                
                
     Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}")
              
                
                
            
       
    
       
       
    

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **Hello** {message.from_user.mention()}</b>

**Please press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="❔ HOW TO USE ME", callback_data=f"cbguide"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>💡 Hello {message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Owner Cmd", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 Fun Cmd", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🏓 `PONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
