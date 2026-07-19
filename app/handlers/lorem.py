from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.lorem import (
    generate_words,
    generate_sentence,
    generate_paragraphs,
)

router = Router()


@router.message(Command("lorem"))
async def lorem_handler(message: Message):
    parts = message.text.split()

    # /lorem
    if len(parts) == 1:
        await message.answer(generate_paragraphs())
        return

    arg = parts[1].lower()

    try:
        if arg == "sentence":
            await message.answer(generate_sentence())

        elif arg.endswith("p"):
            count = int(arg[:-1])
            await message.answer(generate_paragraphs(count))

        else:
            count = int(arg)
            await message.answer(generate_words(count))

    except ValueError:
        await message.answer(
            "Usage:\n"
            "/lorem\n"
            "/lorem 50\n"
            "/lorem sentence\n"
            "/lorem 3p"
        )