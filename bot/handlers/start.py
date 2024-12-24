from aiogram import types
from aiogram import Dispatcher
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


async def start_command(message: types.Message):
    kb = [
        [KeyboardButton(text="Подати заявку на обмін студентів")],
        [KeyboardButton(text="Задати питання")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('📢 Вітаємо вас у чат-боті міжнародного обміну студентів! 🌍\n'
                         '🎓 Хто може брати участь у програмі?\n'
                         'Студенти та студентки 2-4 курсів бакалаврату\n'
                         'Необхідний рівень володіння англійською мовою: B2+\n'
                         'Середній бал у рейтингу успішності має бути вищим за 80\n'
                         '✨ Тут ви можете:\n'
                         '1️⃣ Подати заявку на участь у програмі\n'
                         '2️⃣ Задати питання нашому відділу, і ми з радістю допоможемо!', reply_markup=keyboard)


def register_handlers_start(dp: Dispatcher):
    dp.message.register(start_command, lambda msg: msg.text == "/start")
