import sqlalchemy
from sqlalchemy import Column, Integer, String, BigInteger, sql

from utils.db_api.db_gino import TimedBaseModel, BaseModel


class User(BaseModel):
    __tablename__ ='users'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    username = Column(String(100))
    balance = Column(BigInteger )
    refferal = Column(BigInteger)


    query: sql.Select




