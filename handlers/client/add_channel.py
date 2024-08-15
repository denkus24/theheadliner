from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import utils
from database import Database
import keyboards
from data import localization

import states

router = Router(name=__name__)


@router.message(F.text.in_(localization.add_channel.values()))
async def add_channel(message: Message, state: FSMContext):
    user_lang = message.from_user.language_code
    await message.answer(
        text=localization.enter_url[user_lang],
        reply_markup=keyboards.back_keyboard(user_lang))
    await state.set_state(states.AddChannel.channel_url)


@router.message(states.AddChannel.channel_url)
async def get_channel_url(message: Message, state: FSMContext, scheduler: AsyncIOScheduler):
    user_lang = message.from_user.language_code

    if await Database.channel_exist(message.from_user.id, message.text):
        await message.answer('Channel already existing.', reply_markup=keyboards.start_keyboard(user_lang))
    else:
        data = await Database.add_channel(message.from_user.id, message.text)
        scheduler.add_job(func=utils.send_info,
                          kwargs={'bot': message.bot,
                                  'user_id': data['id'],
                                  'rss_url': data['rss'],
                                  'title': data['title']},
                          trigger='interval',
                          hours=1)
        await message.answer(text=localization.channel_added[user_lang],
                             reply_markup=keyboards.start_keyboard(user_lang))

    await state.clear()
