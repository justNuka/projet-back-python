# System imports

# Libs imports
from pydantic import BaseModel

# Local imports


class User(BaseModel):
    id: int = None
    name: str
    surname: str
    email: str
    password_hash: str
    tel: str
    maintainer: bool