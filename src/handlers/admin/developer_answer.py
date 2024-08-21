from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.enums.parse_mode import ParseMode
from data import localization

import states
import keyboards
import logging

router = Router(name=__name__)


@router.callback_query(keyboards.AnswerOnMessage.filter())
async def answer_to_user(callback: CallbackQuery, callback_data: keyboards.AnswerOnMessage, state: FSMContext):
    await callback.message.answer('Enter answer for user:')
    await state.set_state(states.WriteToDeveloperAdmin.message)
    await state.set_data({'user_id': callback_data.user_id, 'user_lang': callback_data.user_lang})


@router.message(states.WriteToDeveloperAdmin.message)
async def send_answer_to_user(message: Message, state: FSMContext):
    state_data = await state.get_data()
    await message.bot.send_message(chat_id=state_data['user_id'], text=localization.developer_answer[state_data['user_lang']], parse_mode=ParseMode.HTML)
    await message.send_copy(chat_id=state_data['user_id'])
    await message.answer('Answer sent.')
    logging.info(f'Admin answered for user {state_data["user_id"]}')
    await state.clear()
