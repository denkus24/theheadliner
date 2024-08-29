import os

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from data import localization
from database import Database

import re
import keyboards
import states
import logging
import listparser

router = Router(name=__name__)


def parse_opml(opml_filename: str) -> list[dict]:
    with open(opml_filename, 'rb') as file:
        feed = listparser.parse(file.read())
        return feed['feeds']


@router.callback_query(F.data == 'import_opml')
async def import_opml(callback: CallbackQuery, user_lang: str):
    await callback.message.edit_text(text=localization.your_feed_will_be_cleared[user_lang],
                                     reply_markup=keyboards.delete_feed_keyaboard(user_lang))


@router.callback_query(keyboards.FeedClearAnswer.filter())
async def import_answer(callback: CallbackQuery, callback_data: keyboards.FeedClearAnswer, user_lang: str,
                        state: FSMContext):
    if callback_data.answer:
        await callback.message.edit_text(text=localization.send_me_file[user_lang])
        await state.set_state(states.ImportOPML.document)
    else:
        await callback.message.delete()


@router.message(F.document, states.ImportOPML.document)
async def importing_file(message: Message, user_lang: str, state: FSMContext):
    info_message = await message.answer(text=localization.importing_process[user_lang])

    try:
        file_path = f'{message.from_user.id}.opml'  # Downloading file
        await message.bot.download(message.document, file_path)

        feeds = parse_opml(file_path)  # Parsing OPML file

        await Database.clear_users_channels(message.from_user.id)

        for feed in feeds:  # Add every feed in databse
            await Database.add_channel(message.from_user.id, feed['url'])

        await info_message.edit_text(localization.importing_finished[user_lang])
        logging.info(f'User {message.from_user.id} import feeds')

    except Exception as e:
        await info_message.edit_text(localization.importing_error[user_lang])
        logging.error(f'User {message.from_user.id} have error while importing file: {e}')
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
        await state.clear()
