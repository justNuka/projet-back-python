# System imports

# Libs imports
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy import Table, Column
# Local imports
from config.db import meta
from models.user import User

users = Table(
    "user",meta,
    Column("id",Integer,primary_key=True),
    Column("name",String(255)),
    Column("surname",String(255)),
    Column("email",String(255)),
    Column("password_hash",String(255)),
    Column("tel",String(255)),
)

class User(BaseModel):
    id: int = None
    name: str
    surname: str
    email: str
    password_hash: str
    tel: str

class UserOptionnalFields(BaseModel):
    name: str = None
    surname: str = None
    email: str = None
    password_hash: str = None
    tel: str = None