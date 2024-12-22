from aiogram import types
from aiogram import Dispatcher
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from bot.utils.user_data import set_user_step

async def start_command(message: types.Message):
    kb = [
        [KeyboardButton(text="Подати заявку на обмін студентів")],
        [KeyboardButton(text="Задати питання")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('Вітаємо! Оберіть опцію:', reply_markup=keyboard)

def register_handlers_start(dp: Dispatcher):
    dp.message.register(start_command, lambda msg: msg.text == "/start")
