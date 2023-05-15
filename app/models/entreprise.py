# System imports
from enum import Enum
# Libs imports
from pydantic import BaseModel

class Entreprise(BaseModel):
    id_entreprise: int = None
    nameFirm: str
    location: str

class EntrepriseOptionnalFields(BaseModel):
    nameFirm: str
    location: str