from aiogram.filters.callback_data import CallbackData
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

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


class ChannelCallback(CallbackData, prefix="channel"):
    id: str


def user_channels_keyboard(channels: list[dict]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for channel in channels:
        builder.row(
            InlineKeyboardButton(
                text=f'➖ {channel["title"]}',
                callback_data=ChannelCallback(id=str(channel['_id'])).pack()
            )
        )
    return builder.as_markup()


class NotificationButton(CallbackData, prefix='notification'):
    state: bool


def settings_keyboard(user_lang: str, messages_enabled: bool) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text=localization.disable_messages[user_lang] if messages_enabled else localization.enable_messages[user_lang],
        callback_data=NotificationButton(state=messages_enabled).pack()
    ))

    builder.row(InlineKeyboardButton(
        text=localization.write_to_developer[user_lang],
        callback_data='write_to_developer'
    ))

    return builder.as_markup()
