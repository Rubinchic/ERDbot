from aiogram import types
from aiogram import Dispatcher
from bot.keyboards.defaultkeyboards import OptionKeyboard
from bot.utils.user_data import clear_user_data


async def start_command(message: types.Message):
    await message.answer('📢 Вітаємо вас у чат-боті міжнародного обміну студентів! 🌍\n\n'
                         '✨ Тут ви можете:\n'
                         '1️⃣ Подати заявку на участь у програмі обміну\n'
                         '2️⃣ Поставити питання нашому відділу, і ми з радістю допоможемо!\n\n'
                         '🎓 Хто може брати участь у програмі обміну?\n'
                         'Здобувачі освіти 2-4 курсів бакалаврату\n'
                         'Необхідний рівень володіння англійською мовою: B2+\n'
                         'Середній бал у рейтингу успішності має бути вищим за 80', reply_markup=OptionKeyboard)
    user_id = message.chat.id
    clear_user_data(user_id)


def register_handlers_start(dp: Dispatcher):
    dp.message.register(start_command, lambda msg: msg.text == "/start")
