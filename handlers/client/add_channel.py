from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from data import localization
from data.config import HOUR_DELAY
from database import Database

import re
import utils
import keyboards
import states
import logging

router = Router(name=__name__)


def url_validator(url: str) -> bool:
    return re.search(r'(https?://[^\s]+)', url) is not None


@router.message(F.text.in_(localization.add_channel.values()))
async def add_channel(message: Message, state: FSMContext) -> None:
    user_lang = message.from_user.language_code
    await message.answer(
        text=localization.enter_url[user_lang],
        reply_markup=keyboards.back_keyboard(user_lang))
    await state.set_state(states.AddChannel.channel_url)


@router.message(F.text.func(lambda text: url_validator(text)))
@router.message(states.AddChannel.channel_url)
async def get_channel_url(message: Message, state: FSMContext, scheduler: AsyncIOScheduler) -> None:
    user_lang = message.from_user.language_code

    if await Database.channel_exist(message.from_user.id, message.text):
        await message.answer('Channel already existing.', reply_markup=keyboards.start_keyboard(user_lang))
    else:
        if not url_validator(message.text):
            await message.answer('❌ URL is invalid. Please check it and try again.')
        else:
            info_message: Message = await message.answer(text='Adding channel...', reply_markup=None)
            try:
                channel_data = await Database.add_channel(message.from_user.id, message.text)
                scheduler.add_job(func=utils.send_info,
                                  kwargs={'bot': message.bot,
                                          'user_id': channel_data['id'],
                                          'rss_url': channel_data['rss'],
                                          'title': channel_data['title']},
                                  trigger='interval',
                                  hours=HOUR_DELAY)
                await info_message.delete()
                await message.answer(text=f"✅ Feed {channel_data['title']} added successfully",
                                     reply_markup=keyboards.start_keyboard(user_lang))

                logging.info(f'User {message.from_user.id} added new channel with URL:{message.text}')

            except Exception as e:
                await info_message.delete()
                await message.answer(text='❌ Error while adding channel',
                                     reply_markup=keyboards.start_keyboard(user_lang))

                logging.error(f'User {message.from_user.id} adding channel {message.text} finished due error: {e}')

            finally:
                if state is not None:
                    await state.clear()
