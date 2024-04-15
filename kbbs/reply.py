from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



start_kb = ReplyKeyboardMarkup(
    keyboard =[
        [
            KeyboardButton(text='menu'),
            KeyboardButton(text='top_25'),
            KeyboardButton(text='new'),
            KeyboardButton(text='about_us'),
        ],
    ],
)