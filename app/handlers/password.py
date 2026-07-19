from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from services.password import generate_password

router = Router()


@router.message(Command("password"))
async def password(message: Message):
    parts = message.text.split()

    length = 16

    if len(parts) > 1:
        try:
            length = int(parts[1])
        except ValueError:
            await message.answer("❌ Length must be a number.")
            return

    if length < 8 or length > 128:
        await message.answer("❌ Length must be between 8 and 128.")
        return

    pwd = generate_password(length)

    await message.answer(
        f"🔐 Generated Password\n\n`{pwd}`",
        parse_mode="Markdown"
    )