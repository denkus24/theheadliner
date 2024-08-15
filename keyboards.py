from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from data import localization


def start_keyboard(user_lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton(text=localization.my_channels[user_lang]),
        KeyboardButton(text=localization.add_channel[user_lang]),
        KeyboardButton(text=localization.settings[user_lang])
    ]
    ])


def back_keyboard(user_lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[
        KeyboardButton(text=localization.back[user_lang])
    ]
    ])
