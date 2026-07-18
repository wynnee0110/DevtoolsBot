from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.ping import ping_website

router = Router()


@router.message(Command("ping"))
async def ping(message: Message):
    parts = message.text.split(maxsplit=1)

    if len(parts) < 2:
        await message.answer(
            "Usage:\n"
            "/ping google.com"
        )
        return

    url = parts[1]

    try:
        result = await ping_website(url)

        await message.answer(
            f"🌐 {result['url']}\n\n"
            f"Status: {result['status']}\n"
            f"Response: {result['time']} ms"
        )

    except Exception as e:
        await message.answer(f"❌ Error:\n{e}")