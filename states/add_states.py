from aiogram.dispatcher.filters.state import StatesGroup, State


class Add(StatesGroup):
    name= State()
    title = State()
    price = State()
    image_url = State()