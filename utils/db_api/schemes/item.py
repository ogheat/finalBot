import sqlalchemy
from sqlalchemy import Column, Integer, String, BigInteger, sql

from utils.db_api.db_gino import TimedBaseModel, BaseModel


class Item(BaseModel):
    __tablename__ ='items'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    title = Column(String(255))
    price = Column(Integer)
    image_url = Column(String(255))


    query: sql.Select