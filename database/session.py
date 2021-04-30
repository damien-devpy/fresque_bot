from os import environ
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

load_dotenv()

DB_PASSWORD = quote_plus(environ.get("DATABASE_PASSWORD"))
DB_USER = environ.get("DATABASE_USER")
DB_NAME = environ.get("DATABASE_NAME")

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}")
session = Session(engine)
