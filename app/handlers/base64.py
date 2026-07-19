from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.base64 import encode_base64, decode_base64

router = Router()


@router.message(Command("base64"))
async def base64_handler(message: Message):
    parts = message.text.split(maxsplit=2)

    if len(parts) < 3:
        await message.answer(
            "📘 Usage:\n\n"
            "/base64 encode [text]\n"
            "/base64 decode [base64]"
        )
        return

    action = parts[1].lower()
    text = parts[2]

    try:
        if action == "encode":
            result = encode_base64(text)
        elif action == "decode":
            result = decode_base64(text)
        else:
            await message.answer("❌ Action must be 'encode' or 'decode'.")
            return

        await message.answer(
            f"<b>Base64 {action.title()}</b>\n\n"
            f"<code>{result}</code>",
            parse_mode="HTML"
        )

    except Exception:
        await message.answer("❌ Invalid Base64 input.")