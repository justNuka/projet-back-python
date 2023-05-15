# Local imports
from models.user import User

users: list[User] = [
    {
        "id": 1,
        "name": "Elias",
        "surname": "El",
        "email": "julessorens@gmail.com",
        "password_hash": "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9",
        "tel": "0606060606",
        "newletter": True,
        "is_client": True
    },
    {
        "id": 2,
        "name": "Mathieu",
        "surname": "Mat",
        "email": "yan@yan-officiel.fr",
        "password_hash": "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9",
        "tel": "0606060606",
        "newletter": False,
        "is_client": False
    },
    {
        "id": 3,
        "name": "Adam",
        "surname": "Adamou",
        "email": "adam@adam.fr",
        "password_hash": "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9",
        "tel": "0606060606",
        "newletter": True,
        "is_client": True
    },
    {
        "id": 4,
        "name": "Yanis",
        "surname": "Yanisou",
        "email": "yanis@yanis.fr",
        "password_hash": "f2d81a260dea8a100dd517984e53c56a7523d96942a834b9cdc249bd4e8c7aa9",
        "tel": "0606060606",
        "newletter": True,
        "is_client": True
    }
]