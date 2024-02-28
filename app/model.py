from sqlalchemy import Column,Integer,String
from pydantic import BaseModel
from db import Base , ENGINE


class UserTable(Base):
    __tablename__ = 'user' # 테이블명
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False)
    age = Column(Integer)



class User(BaseModel):
    id : int
    name : str
    age : int




class FruitTable(Base):
    __tablename__ = 'fruit'
    fid = Column(Integer,primary_key=True,autoincrement=True)
    fname = Column(String(10),nullable=False)
    fprice = Column(Integer)



class Fruit(BaseModel): # db와 변수명이 같아야함
    fid : int
    fname : str
    fprice : int