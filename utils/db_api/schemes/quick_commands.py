import asyncio

from sqlalchemy import update
from sqlalchemy.orm import session

from loader import bot
from utils.db_api.db_gino import db
from utils.db_api.schemes.item import Item
from utils.db_api.schemes.order import Order
from utils.db_api.schemes.user import User
from asyncpg import UniqueViolationError







async def add_user(id: int, name: str, username: str,balance: int, refferal: int):
    try:
        user =  User(id=id,name=name,username=username,balance=balance,refferal=refferal)
        await user.create()

    except UniqueViolationError:
        pass



async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user

async def select_refferal(refferal: int):
    user = await User.query.where(User.refferal == refferal).gino.first()
    return user


async def count_users():
    users = await User.query.gino.all()
    total = users[-1].id
    return total

async def add_balance(refferal: int, quantity: int):
    user = await User.query.where(User.refferal == refferal).gino.first()
    balance  =  int(user.balance) + int(quantity)
    await user.update(balance=balance).apply()




async def add_item(id: int, name: str, title: str,price: int, image_url: str):
    try:
        item =  Item(id=id,name=name,title=title,price=price,image_url=image_url)
        await item.create()

    except UniqueViolationError:
        pass


async def select_all_items():
    items = await Item.query.gino.all()
    return items


async def select_item(id: int):
    item = await Item.query.where(Item.id == id).gino.first()
    return item

async def item_by_query(query: str):
    items = await Item.query.where(Item.name.ilike(f"%{query}%")).gino.all()
    return items

async def item_by_alphabet():
    items = await Item.query.order_by(Item.name).gino.all()
    return items

async def delete_item(id: int):
    item = await Item.query.where(Item.id == id).gino.first()
    await item.delete()


async def count_items():
    items = await Item.query.gino.all()
    if items:
        total = items[-1].id
        return total
    else:
        return 0


async def minus_balance(refferal: int, item_id: int):
    user = await User.query.where(User.refferal == refferal).gino.first()
    item = await Item.query.where(Item.id == item_id).gino.first()
    price = item.price

    balance = user.balance - price
    await user.update(balance=balance).apply()




async def check_balance(refferal: int,item_id: int):
    user = await User.query.where(User.refferal == refferal).gino.first()
    item = await Item.query.where(Item.id == item_id).gino.first()
    balance = user.balance
    price = item.price
    if balance < price:
        return False
    else:
        return True


async def get_orders(client_id: int):
    orders = await Order.query.where(Order.client_id == client_id).gino.all()
    return orders


async def add_order(client_id: int,item_id: int,status:str, adress: str):
    try:
        order =  Order(client_id=client_id,item_id=item_id,status=status,adress=adress)
        await order.create()

    except UniqueViolationError:
        pass

async def change_status(id: int, status: str):
    order = await Order.query.where(Order.id == id).gino.first()
    await order.update(status=status).apply()
    await bot.send_message(chat_id=order.client_id,text=f"Статус вашего заказа №{id} изменен на: {status}")

async def all_orders():
    orders = await Order.query.gino.all()
    return orders

async def get_order(id: int):
    orders = await Order.query.where(Order.id == id).gino.first()
    return orders

















