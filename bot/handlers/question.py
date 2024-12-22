from aiogram import types
from aiogram import Dispatcher
from bot.utils.user_data import set_user_step, get_user_step, user_data
import logging  # Імпортуємо logging напряму



async def question_handler(message: types.Message):
    """Обробка вибору «Задати питання»."""
    user_id = message.chat.id
    logging.info(f"User {user_id} selected 'Задати питання'")
    await message.answer('Відправте запитання, яке ви хочете нам поставити:', reply_markup=types.ReplyKeyboardRemove())

    # Ініціалізація даних користувача
    user_data[user_id] = {'question': None}
    set_user_step(user_id, 'question')


async def collect_question(message: types.Message):
    """Обробка тексту запитання та перехід до форми."""
    user_id = message.chat.id
    step = get_user_step(user_id)
    logging.info(f"Collecting question for user {user_id}, current step: {step}")

    if step == 'question':
        user_data[user_id]['question'] = message.text
        set_user_step(user_id, 'faculty')
        logging.info(f"User {user_id} question saved: {message.text}")

        # Пропонуємо вибір факультету
        kb = [
            [types.KeyboardButton(text="Навчально-науковий інститут Кібербезпеки та захисту інформації")],
            [types.KeyboardButton(text="Навчально-науковий інститут Інформаційних технологій")],
            [types.KeyboardButton(text="Навчально-науковий інститут Телекомунікацій")],
            [types.KeyboardButton(text="Навчально-науковий інститут Менеджменту та підприємництва")]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer('Дякуємо за ваше питання! Тепер, будь ласка, оберіть назву інституту:',
                             reply_markup=keyboard)
    else:
        logging.warning(f"Unexpected step for user {user_id}: {step}")


def register_handlers_question(dp: Dispatcher):
    """Реєстрація обробників для роботи із запитаннями."""
    dp.message.register(question_handler, lambda msg: msg.text == 'Задати питання')
    dp.message.register(collect_question, lambda msg: get_user_step(msg.chat.id) == 'question')
