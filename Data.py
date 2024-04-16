# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b>Perintah untuk Pengguna BOT
/start - Mulai Bot
/about - Tentang Bot ini
/help - Bantuan Perintah Bot ini
/ping - Untuk mengecek bot hidup
/uptime - Untuk melihat status bot 
/users - Untuk melihat statistik pengguna bot
/batch - Untuk membuat link lebih dari satu file
/speedtest - Untuk Mengetes kecepatan server bot
/broadcast - Untuk mengirim pesan broadcast ke pengguna bot

Jasa Deploy BOT </b><a href='https://t.me/baksdudee'>@baksdudee</a>
"""

    close = [
        [InlineKeyboardButton("〤 ᴛᴜᴛᴜᴘ 〤", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("〤 ᴛᴜᴛᴜᴘ 〤", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton(text="ᴊᴀsᴀ ᴘᴇᴍʙᴜᴀᴛᴀɴ ʙᴏᴛ ✓", url=f"https://t.me/baksdudee"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Jasa Deploy BOT: <a href='https://t.me/baksdudee'>@baksdudee</a>
"""
