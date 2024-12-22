from aiogram import types
from aiogram import Dispatcher
import logging


async def diagnostic_handler(message: types.Message):
    """Діагностичний обробник для перевірки отримання повідомлень."""
    logging.info(f"Received message from {message.chat.id}: {message.text}")
    await message.answer(f"Я отримав ваше повідомлення: {message.text}")


def register_handlers_diagnostics(dp: Dispatcher):
    """Реєстрація діагностичного обробника."""
    dp.message.register(diagnostic_handler)
