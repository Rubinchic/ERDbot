import asyncio
from aiogram import Bot, Dispatcher
from bot.config import API_TOKEN
from bot.handlers.start import register_handlers_start
from bot.handlers.apply import register_handlers_apply
from bot.handlers.question import register_handlers_question
import logging
from dotenv import load_dotenv  # Підключаємо бібліотеку для роботи з .env

# Завантаження змінних з .env
load_dotenv()

async def main():
    # Ініціалізація бота
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    # Реєструємо обробники
    register_handlers_start(dp)
    register_handlers_question(dp)
    register_handlers_apply(dp)

    # Запуск
    await dp.start_polling(bot)

if __name__ == '__main__':
    # Налаштування логування
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
