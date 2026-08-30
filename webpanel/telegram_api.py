from aiogram import Bot

from config import BOT_TOKEN

_bot: Bot | None = None


def get_bot() -> Bot:
    global _bot
    if _bot is None:
        _bot = Bot(token=BOT_TOKEN)
    return _bot


async def get_file_bytes(file_id: str) -> tuple[bytes, str]:
    """Telegram serveridan fayl baytlarini yuklab oladi (token brauzerga chiqmasligi uchun serverda proksi qilinadi)."""
    bot = get_bot()
    file = await bot.get_file(file_id)
    buf = await bot.download_file(file.file_path)
    return buf.read(), file.file_path


_bot_username: str | None = None


async def get_bot_username() -> str:
    global _bot_username
    if _bot_username is None:
        bot = get_bot()
        me = await bot.get_me()
        _bot_username = me.username
    return _bot_username
