from aiogram.fsm.state import StatesGroup, State


class AddChannel(StatesGroup):
    channel_url = State()
