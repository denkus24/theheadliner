from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from data import localization
from database import Database

import data.config
import states
import keyboards
import logging

router = Router(name=__name__)


@router.message(Command('settings'))
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


@router.callback_query(F.data == 'write_to_developer')
async def write_to_developer_handler(call: CallbackQuery, user_lang: str, state: FSMContext) -> None:
    await call.message.delete()
    await call.message.answer(text=localization.write_message_for_dev[user_lang],
                              reply_markup=keyboards.back_keyboard(user_lang))

    await state.set_state(states.WriteToDeveloperUser.message)


@router.message(states.WriteToDeveloperUser.message)
async def send_message_to_developer(message: Message, state: FSMContext, user_lang: str) -> None:
    await message.bot.send_message(text=f'User {message.from_user.id}, {message.from_user.full_name} send a question:', chat_id=data.config.ADMIN_ID)  # Sending message for admin
    await message.copy_to(chat_id=data.config.ADMIN_ID,
                          text=f'User {message.from_user.id}, {message.from_user.full_name} write a message:\n{message.text}',
                          reply_markup=keyboards.answer_on_message(message.from_user.id, user_lang))

    await message.answer(text=localization.your_message_was_sent[user_lang],  # And for user
                         reply_markup=keyboards.start_keyboard(user_lang), parse_mode=ParseMode.HTML)
    logging.info(f'User {message.from_user.id} send a question for developer')

    await state.clear()
