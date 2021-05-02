from sqlalchemy import BigInteger, Column, DateTime, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CounterTable(Base):
    __tablename__ = "counter"

    id = Column(Integer, primary_key=True)
    counter = Column(BigInteger)
    date = Column(DateTime)
