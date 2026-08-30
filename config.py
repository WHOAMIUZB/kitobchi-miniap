import os

# --- Asosiy sozlamalar (bot bilan BIR XIL BOT_TOKEN bo'lishi shart) ---
BOT_TOKEN = os.getenv("BOT_TOKEN", "8868993362:AAF3HS6NrXef2Sqpmr0ThksvZghS-cqGlJw")
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "7861165622").split(",") if x]

DB_PATH = os.getenv("DB_PATH", "books.db")

PAGE_CHARS = 900

XP_FOR_DOWNLOAD = 2
XP_FOR_REVIEW = 5
XP_FOR_QUIZ_CORRECT = 3
XP_FOR_REFERRAL = 10

BOOK_CLUB_CHAT_LINK = os.getenv("BOOK_CLUB_CHAT_LINK", "https://t.me/+your_invite_link_here")

SUPPORTED_LANGUAGES = ["uz", "ru", "en"]
DEFAULT_LANGUAGE = "uz"

# Render avtomatik beradigan port
PORT = int(os.getenv("PORT", "8000"))
