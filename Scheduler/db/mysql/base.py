from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, CHAR
from sqlalchemy.orm import sessionmaker, scoped_session

from Scheduler.settings import mysql_conf

from Scheduler.logger_conf import logger

Base = declarative_base()


class Business(Base):
    __tablename__ = "Business"

    business_id = Column(CHAR(50), primary_key=True, )
    email = Column(String(50))
    mobile = Column(String(11))
    module = Column(String(100))


conf = mysql_conf['username'], mysql_conf['password'], mysql_conf['host'], mysql_conf['port'], mysql_conf['database']
conn_info = f"mysql+pymysql://{conf[0]}:{conf[1]}@{conf[2]}:{conf[3]}/{conf[4]}?charset=utf8"
logger.debug(conn_info)

engine = create_engine(conn_info,)
Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)
