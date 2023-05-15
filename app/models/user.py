# System imports
from enum import Enum
# Libs imports
from pydantic import BaseModel


class User(BaseModel):
    id_user: int = None
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