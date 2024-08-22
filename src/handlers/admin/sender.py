from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from database import Database

import data.config
import states
import logging

router = Router(name=__name__)


@router.message(Command('sender'), F.from_user.id == int(data.config.ADMIN_ID))
async def admin_sender(message: Message, state: FSMContext):
    await message.answer('Enter a message:')
    await state.set_state(states.SenderAdmin.message)


@router.message(states.SenderAdmin.message, F.from_user.id == int(data.config.ADMIN_ID))
async def send_message(message: Message, state: FSMContext):
    all_users = await Database.get_user_ids()
    for id in all_users:
        try:
            await message.copy_to(chat_id=id)
        except:
            continue
    await message.answer('Message sended')
    logging.info('Admin message sended')
    await state.clear()
