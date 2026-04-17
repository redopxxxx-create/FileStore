import os
import logging
from os import environ
from logging.handlers import RotatingFileHandler

# Bot Configuration (Heroku Environment Variables)
LOG_FILE_NAME = "bot.log"
PORT = os.environ.get('PORT', '5010')
OWNER_ID = int(os.environ.get("OWNER_ID", "6497757690"))
SESSION = os.environ.get("SESSION", "yato")

# Telegram API Configuration
TOKEN = os.environ.get("TOKEN", "642712") # Replace or set in Heroku
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
WORKERS = int(os.environ.get("WORKERS", "5"))

# Database Configuration
DB_URI = os.environ.get("DB_URI", "mongodb")
DB_NAME = os.environ.get("DB_NAME", "yato")
DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1003453786108")) # Aapki storage channel ID

# Shortener Configuration
SHORT_URL = os.environ.get("SHORT_URL", "linkshortify.com")
SHORT_API = os.environ.get("SHORT_API", "") 
SHORT_TUT = os.environ.get("SHORT_TUT", "https://t.me/How_to_Download_7x/26")

# Force Subscription (FSub)
# [channel_id, request_enabled, timer_in_minutes]
FSUBS = [[-1003016571084, True, 10]] 

# Auto Delete & Security
AUTO_DEL = int(os.environ.get("AUTO_DEL", "300"))
ADMINS = [int(admin) for admin in os.environ.get("ADMINS", "6497757690 6103092779").split()]
DISABLE_BTN = True
PROTECT = True
MSG_EFFECT = 5046509860389126442

# UI & Messages Configuration
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!!, {first} ~ <blockquote>ʟᴏᴠᴇ ᴘᴏʀɴʜᴡᴀ? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ғɪɴᴅ ᴡʜᴀᴛ ʏᴏᴜ aʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.</blockquote></b>",
    "FSUB": "<b><blockquote>›› ʜᴇʏ ×</blockquote>\n  ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b>",
    "ABOUT": "<b>›› ғᴏʀ ᴍᴏʀᴇ: @Nova_Flix \n <blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/codeflix_bots'>Cʟɪᴄᴋ ʜᴇʀᴇ</a> \n›› ᴏᴡɴᴇʀ: @ProYato\n›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @cosmic_freak</b></blockquote>",
    "REPLY": "<b>For More Join - @Hanime_Arena</b>",
    "SHORT_MSG": "<b>📊 ʜᴇʏ {first}, \n\n‼️ ɢᴇᴛ ᴀʟʟ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱɪɴɢʟᴇ ʟɪɴᴋ ‼️\n\n ⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>",
    "START_PHOTO": os.environ.get("START_PHOTO", "https://graph.org/file/510affa3d4b6c911c12e3.jpg"),
    "FSUB_PHOTO": os.environ.get("FSUB_PHOTO", "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg"),
    "SHORT_PIC": os.environ.get("SHORT_PIC", "https://telegra.ph/file/7a16ef7abae23bd238c82-b8fbdcb05422d71974.jpg"),
    "SHORT": "https://telegra.ph/file/8aaf4df8c138c6685dcee-05d3b183d4978ec347.jpg"
}

# Logger Setup
def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
