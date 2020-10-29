from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Адрес"),
            KeyboardButton(text="Почему живи стоя?"),
        ],
        [
            KeyboardButton(text="Сайт"),
            KeyboardButton(text="Код от дверей"),
        ]
    ],
    resize_keyboard=True
)
