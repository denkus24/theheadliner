from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from database import Database

import data.config
import states
import logging

router = Router(name=__name__)

@router.message(F.from_user.id == data.config.ADMIN_ID)
@router.message(Command('statistic'))
async def statistic(message:Message):
    ping = await Database.ping()
    users = await Database.get_number_of_users()
    answer = (f'Database is reachable:{ping}\n'
               f'Number of users:{users}')
    await message.answer(answer)
