import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.ping import router as ping_router
from handlers.password import router as password_router
from handlers.lorem import router as lorem_router
from handlers.qr import router as qr_router
from handlers.hash import router as hash_router
from handlers.base64 import router as base64_router


async def main():

    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(ping_router)
    dp.include_router(password_router)
    dp.include_router(lorem_router)
    dp.include_router(qr_router)
    dp.include_router(hash_router)
    dp.include_router(base64_router)

    print("Bot started")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())