from aiogram.fsm.state import StatesGroup, State


class AddChannel(StatesGroup):
    channel_url = State()

class WriteToDeveloperUser(StatesGroup):
    message = State()

class WriteToDeveloperAdmin(StatesGroup):
    message = State()