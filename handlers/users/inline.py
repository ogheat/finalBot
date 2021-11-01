import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.config import ADMINS
from keyboards.inline.buy_callback_data import button_generator, buy_callback
from keyboards.inline.top_up import top_up, top_up_callback, choose
from loader import dp, bot
from states.adress import Adress
from utils.db_api.schemes import quick_commands
from utils.misc.qiwi import Payment


@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    items = await quick_commands.item_by_query(query["query"])
    alphabet = await quick_commands.item_by_alphabet()
    result = []
    if query["query"] == "":
        for item in alphabet:
            result.append(types.InlineQueryResultArticle(
                        id=f"{item.id}",
                        title=f"{item.name}",
                        description=f"{item.title}",
                        thumb_url=f"{item.image_url}",
                        input_message_content=types.InputTextMessageContent(
                            message_text=f"{item.id}"
                        ),


                    ),)
        await query.answer(
            results=result
        )
    else:
        for item in items:
            result.append(types.InlineQueryResultArticle(
                id=f"{item.id}",
                title=f"{item.name}",
                description=f"{item.title}",
                thumb_url=f"{item.image_url}",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"{item.id}"
                ),

            ), )
        await query.answer(
            results=result
        )






@dp.chosen_inline_handler()
async def good(chosen_inline_query: types.ChosenInlineResult):
    user_id = chosen_inline_query.from_user.id
    item_id = chosen_inline_query.result_id
    item = await quick_commands.select_item(int(item_id))
    button = await  button_generator(item_id)
    await bot.send_photo(chat_id=user_id,photo=f"{item.image_url}",caption=f"<b>{item.name}</b>\n\n{item.title}\n\nЦена:<b>{item.price}</b>",reply_markup=button)



@dp.callback_query_handler(buy_callback.filter(yes="yes"))
async def buy(call: CallbackQuery,callback_data: dict,state: FSMContext):
    id = callback_data.get("id")
    item = await quick_commands.select_item(int(id))
    user_id = call.from_user.id
    await call.answer(cache_time=60)
    if await quick_commands.check_balance(int(user_id),int(id)) == True:
        await call.message.answer(text=f"Вы купили товар номер {id}")
        await quick_commands.minus_balance(int(user_id),int(id))
        await call.message.answer("Успешно оплачено.Напишите адресс в формате: Имя, Фамилия, улица дом, квартира, город, индекс.")
        await Adress.name.set()
        await state.update_data(id=id)
    else:
        await call.answer(cache_time=60)
        await call.message.answer(text=f"Недостаточно средств",reply_markup=top_up)



@dp.message_handler(state=Adress.name)
async def add_name(message: types.Message, state: FSMContext):
    client_id = message.from_user.id
    adress = message.text
    data = await state.get_data()
    id = data["id"]
    await quick_commands.add_order(int(client_id),int(id),"Оплачен",adress)
    await message.answer(f"Успешно отправлено.Товар номер {id}.Адресс:{adress}")
    admin = ADMINS[0]
    await bot.send_message(chat_id=admin,text=f"<b>Новый ордер.</b> <b>id клиента:</b>{client_id} <b>Товар номер:</b> {id}. <b>Адресс:</b> {adress}")
    await state.reset_state()



















