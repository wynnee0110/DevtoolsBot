from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.services.ip import lookup_ip

router = Router()


@router.message(Command("ip"))
async def ip_handler(message: Message):

    parts = message.text.split()

    if len(parts) < 2:
        await message.answer(
            "Usage:\n/ip 8.8.8.8"
        )
        return

    ip = parts[1]

    data = await lookup_ip(ip)

    if data["status"] == "private":
        await message.answer(
            "🏠 Private IP Address\n\n"
            "This IP is inside a local network.\n\n"
            "It cannot have:\n"
            "• Country\n"
            "• City\n"
            "• ISP\n"
            "• Location"
        )
        return


    if data.get("status") != "success":
        await message.answer(
            "❌ IP lookup failed."
        )
        return


    await message.answer(
        f"🌍 <b>IP Information</b>\n\n"
        f"IP: <code>{data['query']}</code>\n"
        f"Country: {data['country']}\n"
        f"Region: {data['regionName']}\n"
        f"City: {data['city']}\n"
        f"ISP: {data['isp']}\n"
        f"ASN: {data['as']}\n"
        f"Timezone: {data['timezone']}",
        parse_mode="HTML"
    )