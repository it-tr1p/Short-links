from aiogram.fsm.state import State, StatesGroup


class GetLink(StatesGroup):
    get_link = State()
    short_link = State()
    get_title = State()
