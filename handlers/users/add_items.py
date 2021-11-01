from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp
from states.add_states import Add
from utils.db_api.schemes import quick_commands


@dp.message_handler(Command("add"))
async def bot_start(message: types.Message):
    if message.from_user.id in ADMINS:
        await message.answer(f"Access approved")
        await message.answer("Введите имя товара")
        await Add.name.set()

    else:
        await message.answer(f"access denied")


@dp.message_handler(state=Add.name)
async def add_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Введите описание товара")
    await Add.title.set()


@dp.message_handler(state=Add.title)
async def add_title(message: types.Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)
    await message.answer("Введите цену товара")
    await Add.price.set()


@dp.message_handler(state=Add.price)
async def add_title(message: types.Message, state: FSMContext):
    price = message.text
    await state.update_data(price=price)
    await message.answer("Введите ссылку на фото товара")
    await Add.image_url.set()


@dp.message_handler(state=Add.image_url)
async def add_title(message: types.Message, state: FSMContext):
    image_url = message.text
    await state.update_data(image_url=image_url)
    data = await state.get_data()
    await state.reset_state()
    id = await quick_commands.count_items() + 1
    await quick_commands.add_item(id=id, name=f"{data['name']}", title=f"{data['title']}", price=int(data['price']), image_url=f"{data['image_url']}")
    result = await quick_commands.select_item(id)
    await message.answer(text=f"Товар {result.id}\nИмя {result.name}\nОписание {result.title}\nЦена:{result.price}\nСыылка {result.image_url}\n\nУспешно добавлен")








