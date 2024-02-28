# db 라이브러리
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


user_name = 'root' # db id 
user_pwd = 'futuremain9735' # db pwd
db_host = '127.0.0.1' # url
db_name = 'data' # skima 
db_port = 3307 # port 


DB_URL = f'mysql+pymysql://{user_name}:{user_pwd}@{db_host}:{db_port}/{db_name}?charset=utf8'



ENGINE = create_engine(
    DB_URL,
    # encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind=ENGINE
    )
)

# instance 
Base = declarative_base()
Base.query = session.query_property()