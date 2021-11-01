from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.default.menu_button import menu
from keyboards.inline.callback_data import subscribe_check
from keyboards.inline.subscribe import subscribe
from loader import dp, bot
from states.invite_code import Invite
from utils.db_api.schemes import quick_commands


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    args = message.get_args()
    user_id = message.from_user.id
    if not args and not await quick_commands.select_refferal(int(user_id)) :
        await message.answer("Вы пришли без инвайт кода.Чтобы пользоваться ботом,подпишитесь на канал",reply_markup=subscribe)
    else:
        if await quick_commands.select_refferal(int(user_id)):
            await message.answer(f"Здраствуйте, {message.from_user.full_name}",reply_markup=menu)

        elif await quick_commands.select_refferal(refferal=int(args)):
            all = len(await quick_commands.select_all_users())
            id = all + 1
            name = message.from_user.full_name
            username = message.from_user.username
            await quick_commands.add_user(id,name,username,0,user_id)
            await message.answer(f"Добро пожаловать, {message.from_user.full_name}.Вас пригласил id:{args}",reply_markup=menu)
            await quick_commands.add_balance(int(args),10)
            # reffer = await quick_commands.select_refferal(int(args))
            await bot.send_message(chat_id=args,text="По вашей реферальной ссылке пришел пользователь.Вам начислено 10 rub")
        elif not await quick_commands.select_user(id=int(args)):
            await message.answer(f"Сcылка,по которой вы перешли , имеет неверный инвайт код.Чтобы пользоваться ботом подпишитесь на канал или введите код вручную.",reply_markup=subscribe)


@dp.callback_query_handler(subscribe_check.filter(check="check"))
async def check(call: CallbackQuery):
    user_id = call.from_user.id
    print(user_id)
    user_channel_status = await bot.get_chat_member(chat_id='@testchennael', user_id=user_id)
    if user_channel_status["status"] != 'left':
        await call.answer(cache_time=60)
        all = len(await quick_commands.select_all_users())
        id = all + 1
        name = call.from_user.full_name
        username = call.from_user.username
        await quick_commands.add_user(id, name, username, 0, user_id)
        await call.message.answer("Спасибо за подписку.Теперь вы можете пользоваться ботом!",reply_markup=menu)
    else:
        await bot.send_message(call.from_user.id, 'Вы не подписались на канал!',reply_markup=subscribe)


@dp.callback_query_handler(subscribe_check.filter(check="manually"))
async def manually(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Введите ваш реферальный код ниже")
    await Invite.write.set()


@dp.message_handler(state=Invite.write)
async def check_invite(message: types.Message, state: FSMContext):
    code = message.text
    if await quick_commands.select_refferal(refferal=int(code)):
        count = await quick_commands.count_users()
        id = count + 1
        user_id = message.from_user.id
        name = message.from_user.full_name
        username = message.from_user.username
        await quick_commands.add_user(id, name, username, 0, user_id)
        await message.answer(f"Добро пожаловать, {message.from_user.full_name}.Вас пригласил id:{code}",reply_markup=menu)
        await quick_commands.add_balance(int(code), 10)
        await bot.send_message(chat_id=code,text="По вашей реферальной ссылке пришел пользователь.Вам начислено 10 rub")
    else:
        await message.answer("Вы ввели неверный код.Чтобы пользоваться ботом подпишитесь на канал или попробуйте еще раз",reply_markup=subscribe)
    await state.finish()









