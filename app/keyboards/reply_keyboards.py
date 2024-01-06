from aiogram.types import ReplyKeyboardMarkup, \
                          KeyboardButton

def get_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text='Быстрый мем'), KeyboardButton(text='Подобрать мем')],
        [KeyboardButton(text='Загрузить мем')],
        [KeyboardButton(text='Настройки')]
    ]
    
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
