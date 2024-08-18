from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from data import localization
from database import Database

import keyboards
import logging

router = Router(name=__name__)


@router.callback_query(keyboards.ChannelCallback.filter())
async def delete_from_channel_list(callback: CallbackQuery, callback_data: keyboards.ChannelCallback, user_lang: str) -> None:
    await Database.delete_channel(callback_data.id)
    await callback.message.edit_text(localization.channel_deleted[user_lang])


@router.message(F.text.in_(localization.my_channels.values()))
async def channel_list(message: Message, state: FSMContext, user_lang: str) -> None:
    user_channels = await Database.get_user_channels(message.from_user.id)
    await message.answer(text='Press on channel if you want to unsubscribe',
                         reply_markup=keyboards.user_channels_keyboard(user_channels))
    logging.info(f'User {message.from_user.id} looked up his channels')
