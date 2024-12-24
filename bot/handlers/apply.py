from aiogram import types
from aiogram import Dispatcher
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from bot.utils.user_data import set_user_step, get_user_step, user_data, clear_user_data
import logging  # Імпортуємо logging напряму
from bot.config import ADMIN_CHAT_ID  # Імпортуємо лише ADMIN_CHAT_ID із config


async def apply_handler(message: types.Message):
    """Обробка вибору «Подати заявку на обмін студентів»."""
    kb = [
        [KeyboardButton(text="Навчально-науковий інститут Кібербезпеки та захисту інформації")],
        [KeyboardButton(text="Навчально-науковий інститут Інформаційних технологій")],
        [KeyboardButton(text="Навчально-науковий інститут Телекомунікацій")],
        [KeyboardButton(text="Навчально-науковий інститут Менеджменту та підприємництва")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('Оберіть назву інституту:', reply_markup=keyboard)
    set_user_step(message.chat.id, 'faculty')


async def collect_data(message: types.Message):
    """Збір даних заявки на обмін студентів."""
    user_id = message.chat.id
    step = get_user_step(user_id)

    if step == 'faculty':
        user_data[user_id]['faculty'] = message.text
        kb = [
            [KeyboardButton(text="2 курс"), KeyboardButton(text="3 курс")],
            [KeyboardButton(text="4 курс")]
        ]
        keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        await message.answer('Оберіть номер курсу:', reply_markup=keyboard)
        set_user_step(user_id, 'course')

    elif step == 'course':
        user_data[user_id]['course'] = message.text
        await message.answer('Введіть назву та номер групи:', reply_markup=types.ReplyKeyboardRemove())
        set_user_step(user_id, 'group')

    elif step == 'group':
        user_data[user_id]['group'] = message.text
        await message.answer('Введіть ваші ПІБ:')
        set_user_step(user_id, 'name')

    elif step == 'name':
        user_data[user_id]['name'] = message.text
        await message.answer('Введіть ваш номер телефону для звʼязку з вами:')
        set_user_step(user_id, 'phone')

    elif step == 'phone':
        user_data[user_id]['phone'] = message.text

        # Формування повідомлення для адміністратора
        user_info = user_data[user_id]
        try:
            text = (f"❓ Запитання від користувача:\n"
                    f"Питання: {user_info['question']}\n"
                    f"Інститут: {user_info['faculty']}\n"
                    f"Курс: {user_info['course']}\n"
                    f"Група: {user_info['group']}\n"
                    f"ПІБ: {user_info['name']}\n"
                    f"Телефон: {user_info['phone']}\n"
                    f"Юзернейм: @{message.from_user.username if message.from_user.username else 'Не вказано'}")
        except:
            text = (f"📚 Заявка на обмін студентів:\n"
                    f"Інститут: {user_info['faculty']}\n"
                    f"Курс: {user_info['course']}\n"
                    f"Група: {user_info['group']}\n"
                    f"ПІБ: {user_info['name']}\n"
                    f"Телефон: {user_info['phone']}\n"
                    f"Юзернейм: @{message.from_user.username if message.from_user.username else 'Не вказано'}")

        # Відправка повідомлення адміністраторам
        try:
            await message.bot.send_message(ADMIN_CHAT_ID, text)
            logging.info(f"Sent application to admin chat ID {ADMIN_CHAT_ID}")
            await message.answer('Ми отримали вашу заявку й звʼяжемося з вами найближчим часом! Щоб подати ще одну заявку, відправте команду /start.')
        except Exception as e:
            logging.error(f"Failed to send message to admin: {e}")
            await message.answer('Сталася помилка під час відправки вашої заявки. Спробуйте ще раз.')

        # Очистка даних користувача
        clear_user_data(user_id)
        logging.info(f"Cleared user data for {user_id}")


def register_handlers_apply(dp: Dispatcher):
    """Реєстрація обробників для роботи із заявками."""
    dp.message.register(apply_handler, lambda msg: msg.text == 'Подати заявку на обмін студентів')
    dp.message.register(collect_data, lambda msg: msg.chat.id in user_data)
