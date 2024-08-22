from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from database import Database

import data.config

router = Router(name=__name__)


@router.message(Command('statistic'), F.from_user.id == int(data.config.ADMIN_ID))
async def statistic(message: Message):
    ping = await Database.ping()
    users = await Database.get_number_of_users()
    answer = (f'Database is reachable:{ping}\n'
              f'Number of users:{users}')
    await message.answer(answer)
