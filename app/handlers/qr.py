from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, BufferedInputFile

from services.qr import generate_qr

router = Router()


@router.message(Command("qr"))
async def qr_handler(message: Message):
    parts = message.text.split(maxsplit=1)

    if len(parts) < 2:
        await message.answer(
            "Usage:\n"
            "/qr https://github.com"
        )
        return

    data = parts[1]

    image = generate_qr(data)

    photo = BufferedInputFile(
        image.read(),
        filename="qr.png",
    )

    await message.answer_photo(photo)