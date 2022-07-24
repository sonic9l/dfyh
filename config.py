import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", " keto ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/1419d0015ff39ce626cce.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/1419d0015ff39ce626cce.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/1419d0015ff39ce626cce.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/1419d0015ff39ce626cce.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "keto_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "iOm3y")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ZEPD8")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZEPD8")
OWNER_NAME = getenv("OWNER_NAME", "iOm3y") 
DEV_NAME = getenv("DEV_NAME", "ZEPD8")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
