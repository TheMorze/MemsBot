from aiogram.types import ReplyKeyboardMarkup, \
                          KeyboardButton

def get_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton('Получить мем'), KeyboardButton('Загрузить мем')],
        [KeyboardButton('Настройки')]
    ]
    
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )