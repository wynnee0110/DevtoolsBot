from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

HASH_ALGORITHMS = [
    "md5",
    "sha1",
    "sha224",
    "sha256",
    "sha384",
    "sha512",
    "blake2b",
    "blake2s",
    "sha3_224",
    "sha3_256",
    "sha3_384",
    "sha3_512",
]


@router.message(Command("hashlist"))
async def hashlist_handler(message: Message):
    algorithms = "\n".join(f"• {algo}" for algo in HASH_ALGORITHMS)
    await message.answer(
        f"🔐 <b>Supported Hash Algorithms</b>\n\n{algorithms}",
        parse_mode="HTML"
    )