from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start(message: Message):

    await message.answer(
        """
Toolbox

Available:

/ping [url]
/password [length]
/lorem [length/sentence/words]
/qr [data]
/hash [algorithm] [text]
/base64 [encode/decode] [text]


        """
    )