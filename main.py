import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app import user_handlers, admin_handlers

async def start_bot():
    load_dotenv()
    bot = Bot(token=os.getenv('TG_TOKEN'))
    dp = Dispatcher()
    dp.include_router(user_handlers.user)
    dp.include_router(admin_handlers.admin)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        pass
