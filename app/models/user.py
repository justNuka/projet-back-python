# System imports
from enum import Enum
# Libs imports
from pydantic import BaseModel


class User(BaseModel):
    id: int = None
    name: str
    surname: str
    email: str
    password_hash: str
    tel: str
    newletter: bool
    is_client: bool

class UserOptionnalFields(BaseModel):
    name: str = None
    surname: str = None
    email: str = None
    password_hash: str = None
    tel: str = None
    newsletter: bool = None
    is_client: bool = None