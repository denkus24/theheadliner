from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from database import Database
from aiogram.enums.parse_mode import ParseMode
from data import localization

import keyboards
import logging

router = Router(name=__name__)


@router.message(CommandStart())
async def start(message: Message):
    user_lang = message.from_user.language_code

    if await Database.user_exist(message.from_user.id):
        await message.answer(text=localization.start_message[user_lang],
                             reply_markup=keyboards.start_keyboard(user_lang),
                             parse_mode=ParseMode.HTML)
    else:
        await message.answer(text=localization.welcome_message[user_lang],
                             reply_markup=keyboards.start_keyboard(user_lang),
                             parse_mode=ParseMode.HTML)
        await Database.add_user(message.from_user.id,
                                message.from_user.full_name,
                                message.from_user.username)
        logging.info(f'User {message.from_user.id} added')
