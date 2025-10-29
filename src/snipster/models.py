import os

from dotenv import load_dotenv
from sqlmodel import Field, SQLModel, create_engine

load_dotenv()
PROD_DB = os.environ["PROD_DB"]

engine = create_engine(PROD_DB, echo=False)


class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: float
