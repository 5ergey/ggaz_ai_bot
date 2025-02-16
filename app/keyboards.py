from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Чат c ИИ')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню')
