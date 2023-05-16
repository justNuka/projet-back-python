# System imports

# Libs imports
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy import Table, Column
# Local imports
from config.db import meta
from models.user import User

users: list[User] = [
    {
        "id_user": 1,
        "name": "Elias",
        "surname": "El",
        "email": "elboez@gmail.com",
        "password_hash": "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9",
        "tel": "0606060606",
    },
    {
        "id": 2,
        "name": "Mathieu",
        "surname": "Mat",
        "email": "mat@mathiel.fr",
        "password_hash": "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9",
        "tel": "0606060606",
    },
]