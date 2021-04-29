from sqlalchemy import BigInteger, Column, DateTime, Integer, Table


class CounterTable(Table):
    Column('id', Integer, primary_key=True)
    Column('counter', BigInteger)
    Column('date', DateTime)
