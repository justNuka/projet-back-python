# System imports

# Libs imports
from pydantic import BaseModel

# Local imports


class Entreprise(BaseModel):
    id: int = None
    nameFirm: str
    location: str