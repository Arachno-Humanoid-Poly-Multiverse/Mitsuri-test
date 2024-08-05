# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




import os
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6698400452:AAExx74r2C87gzFNMaNhgubRvr3jZb5GOkM")
APP_ID = int(os.environ.get("APP_ID", "16575077"))
API_HASH = os.environ.get("API_HASH", "1c8c0bcb55c14e0fd8078058966b6a11")


OWNER = os.environ.get("OWNER", "") #Owner username
OWNER_ID = int(os.environ.get("OWNER_ID", "1702061654")) #Owner user id
DB_URL = os.environ.get("DB_URL", "mongodb+srv://fakefacebook602:inyor1234@cluster0.ukykpoc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "filesharexbot")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002185863754"))


SECONDS = int(os.getenv("SECONDS", "600")) # auto delete in seconds



PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))




START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first} 🖤\n\nɪ ᴀᴍ ʏᴏᴜʀ ᴡᴀɪꜰᴜ.. 🥵\n\n-> ʏᴏᴜ ᴄᴀɴ ᴜɴᴅʀᴇss ᴍᴇ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇs sʜᴀʀᴇᴅ ʙʏ ᴍᴀsᴛᴇʀ(ᴀᴅᴍɪɴs)😈\n\n-> ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʙᴇ ᴍʏ ᴍᴀsᴛᴇʀ ᴍᴇssᴀɢᴇ ᴍʏ ᴄʀᴇᴀᴛᴏʀ 🤭💦\n\nɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇs ᴀɴᴅ ᴇɴᴊᴏʏ 🥀</b>")

try:
    ADMINS=[7085541484]
    for x in (os.environ.get("ADMINS", "1240111170 5906464451").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")


FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>💠You Need to Join My Channel to Get Your File\n\nJoin Channel Given Below 👇</b>")

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot !"

ADMINS.append(OWNER_ID)
ADMINS.append(7085541484)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
