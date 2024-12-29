from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

ChooseCourse1 = [
            [KeyboardButton(text="1 курс"), KeyboardButton(text="2 курс")],
            [KeyboardButton(text="3 курс"), KeyboardButton(text="4 курс")]
        ]
KeyboardChooseCourse1Markup = ReplyKeyboardMarkup(keyboard=ChooseCourse1, resize_keyboard=True)


ChooseCourse2 = [
            [KeyboardButton(text="2 курс"), KeyboardButton(text="3 курс")],
            [KeyboardButton(text="4 курс")]
        ]
KeyboardChooseCourse2Markup = ReplyKeyboardMarkup(keyboard=ChooseCourse2, resize_keyboard=True)

FacultyChoose = [
    [KeyboardButton(text="Навчально-науковий інститут Кібербезпеки та захисту інформації")],
    [KeyboardButton(text="Навчально-науковий інститут Інформаційних технологій")],
    [KeyboardButton(text="Навчально-науковий інститут Телекомунікацій")],
    [KeyboardButton(text="Навчально-науковий інститут Менеджменту та підприємництва")]
]
FacultyKeyboard = ReplyKeyboardMarkup(keyboard=FacultyChoose, resize_keyboard=True)

OptionChoose = [
    [KeyboardButton(text="Подати заявку на обмін студентів")],
    [KeyboardButton(text="Поставити питання")]
]
OptionKeyboard = ReplyKeyboardMarkup(keyboard=OptionChoose, resize_keyboard=True)

