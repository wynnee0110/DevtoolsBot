from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.hash import hash_text

router = Router()


@router.message(Command("hash"))
async def hash_handler(message: Message):
    parts = message.text.split(maxsplit=2)

    if len(parts) < 2:
        await message.answer(
            "Usage:\n"
            "/hash <text>\n"
            "/hash <algorithm> <text>"
        )
        return

    if len(parts) == 2:
        algorithm = "sha256"
        text = parts[1]
    else:
        algorithm = parts[1]
        text = parts[2]

    try:
        digest = hash_text(text, algorithm)

        await message.answer(
            f"🔐 <b>{algorithm.upper()}</b>\n\n"
            f"<code>{digest}</code>",
            parse_mode="HTML",
        )

    except ValueError:
        await message.answer(
            "❌ Unsupported algorithm.\n\n"
            "Use /hashlist to see available algorithms."
        )