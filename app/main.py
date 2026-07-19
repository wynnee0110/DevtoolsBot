import asyncio

from aiogram import Bot, Dispatcher

from app.config import BOT_TOKEN
from app.handlers.start import router as start_router
from app.handlers.ping import router as ping_router
from app.handlers.password import router as password_router
from app.handlers.lorem import router as lorem_router
from app.handlers.qr import router as qr_router
from app.handlers.hash import router as hash_router
from app.handlers.base64 import router as base64_router
from app.handlers.ip import router as ip_router