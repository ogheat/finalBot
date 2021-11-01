from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



from aiogram.utils import callback_data
from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData("buy","yes","id")



async def button_generator(id: int):

    button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Купить",
                    callback_data=buy_callback.new(yes="yes",id=f"{id}")
                ),
             ],

        ]
    )
    return button

