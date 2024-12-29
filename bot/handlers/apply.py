from aiogram import types
from aiogram import Dispatcher
from bot.utils.user_data import set_user_step, get_user_step, user_data, clear_user_data
from bot.keyboards.defaultkeyboards import KeyboardChooseCourse1Markup, KeyboardChooseCourse2Markup, FacultyKeyboard, OptionKeyboard
import logging
from bot.config import ADMIN_CHAT_ID  # Імпортуємо лише ADMIN_CHAT_ID із config


async def apply_handler(message: types.Message):
    """Обробка вибору «Подати заявку на обмін студентів»."""
    await message.answer('Оберіть ваш інститут:', reply_markup=FacultyKeyboard)
    set_user_step(message.chat.id, 'faculty')


async def collect_data(message: types.Message):
    """Збір даних заявки на обмін студентів."""
    user_id = message.chat.id
    step = get_user_step(user_id)

    if step == 'faculty':
        user_data[user_id]['faculty'] = message.text
        await message.answer('Оберіть номер курсу:', reply_markup=KeyboardChooseCourse2Markup)
        set_user_step(user_id, 'course')

    elif step == 'faculty_question':
        user_data[user_id]['faculty'] = message.text
        await message.answer('Оберіть номер курсу:', reply_markup=KeyboardChooseCourse1Markup)
        set_user_step(user_id, 'course')

    elif step == 'course':
        user_data[user_id]['course'] = message.text
        await message.answer('Введіть вашу групу:', reply_markup=types.ReplyKeyboardRemove())
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
            await message.answer('Ми отримали вашу заявку й звʼяжемося з вами найближчим часом! Щоб подати ще одну '
                                 'заявку, відправте команду /start або оберіть опцію на клавіатурі.',
                                 reply_markup=OptionKeyboard)
        except Exception as e:
            logging.error(f"Failed to send message to admin: {e}")
            await message.answer('Сталася помилка під час відправки вашої заявки. Спробуйте ще раз.', reply_markup=OptionKeyboard)

        # Очистка даних користувача
        clear_user_data(user_id)
        logging.info(f"Cleared user data for {user_id}")


def register_handlers_apply(dp: Dispatcher):
    """Реєстрація обробників для роботи із заявками."""
    dp.message.register(apply_handler, lambda msg: msg.text == 'Подати заявку на обмін студентів')
    dp.message.register(collect_data, lambda msg: msg.chat.id in user_data)
