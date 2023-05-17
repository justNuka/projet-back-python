# System imports

# Libs imports
from pydantic import BaseModel

# Local imports


class User(BaseModel):
    id: int = None
    name: str
    surname: str
    email: str
    password: str
    tel: str
    maintainer: bool

class UserChangeableFields(BaseModel):
    name: str = None
    surname: str = None
    email: str = None
    password: str = None
    tel: str = None
    maintainer: bool = None