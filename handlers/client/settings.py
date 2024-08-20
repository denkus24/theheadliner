from aiogram import Router, F
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from data import localization
from database import Database

import keyboards
import logging

router = Router(name=__name__)


@router.message(F.text.in_(localization.settings.values()))
async def show_settings(message: Message, user_lang: str) -> None:
    messages_enabled = await Database.is_user_notifications_enabled(message.from_user.id)
    await message.answer(text=localization.choose_setting[user_lang],
                         reply_markup=keyboards.settings_keyboard(user_lang, messages_enabled))


@router.callback_query(keyboards.NotificationButton.filter())
async def update_notifications(call: CallbackQuery, callback_data: keyboards.NotificationButton,
                               user_lang: str) -> None:
    await Database.update_user_notification(call.from_user.id, not callback_data.state)
    await call.message.edit_text(text=localization.choose_setting[user_lang],
                                 reply_markup=keyboards.settings_keyboard(user_lang, not callback_data.state))
    if not callback_data.state:
        logging.info(f'User {call.from_user.id} enable notifications')
    else:
        logging.info(f'User {call.from_user.id} enable notifications')
