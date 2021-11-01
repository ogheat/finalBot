from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import  subscribe_check

subscribe = InlineKeyboardMarkup (inline_keyboard=[
    [
    InlineKeyboardButton(text="Проверить подписку",callback_data = subscribe_check.new(check="check")),
    InlineKeyboardButton(text="Подписаться",url="https://t.me/testchennael")
    ],
    [
    InlineKeyboardButton(text="Ввести код вручную",callback_data=subscribe_check.new(check="manually"))
    ],
]
)


