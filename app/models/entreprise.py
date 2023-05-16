# System imports

# Libs imports
from pydantic import BaseModel

# Local imports
from models.user import User
from models.activite import Activite


class Entreprise(BaseModel):
    id: int = None
    nameFirm: str
    location: str
    users: list[User] = []
    plannings: list[Activite] = []