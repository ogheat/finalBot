from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import  subscribe_check



from aiogram.utils import callback_data
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.menu import menu_callback_data

top_up_callback = CallbackData("top_up","yes")
top_up_choose_callback = CallbackData("choose","payment")


top_up_profile = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Пополнить баланс",
                    callback_data=top_up_callback.new(yes="yes")
                ),

             ],
            [
InlineKeyboardButton(
                    text="Вернуться в главное меню",
                    callback_data=menu_callback_data.new(action="main")
                ),
            ],

        ]
    )


top_up = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Пополнить баланс",
                    callback_data=top_up_callback.new(yes="yes")
                ),
             ],

        ]
    )


choose = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Qiwi",
                    callback_data=top_up_choose_callback.new(payment="qiwi")
                ),
             ],
[
                InlineKeyboardButton(
                    text="Ltc",
                    callback_data=top_up_choose_callback.new(payment="ltc")
                ),
             ],

        ]
    )


paid = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Оплатил",
                    callback_data="paid"
                ),
             ],
            [
                InlineKeyboardButton(
                    text="Отмена",
                    callback_data="cancel"
                ),
            ],

        ]
    )