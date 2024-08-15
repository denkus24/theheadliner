from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

import keyboards
from data import localization

router = Router(name=__name__)


@router.message(F.text.in_(localization.back.values()))
async def back(message: Message, state: FSMContext):
    user_lang = message.from_user.language_code
    await message.answer(localization.turned_back[user_lang], reply_markup=keyboards.start_keyboard(user_lang))
    await state.clear()
