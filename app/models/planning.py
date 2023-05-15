# System imports
from enum import Enum
# Libs imports
from pydantic import BaseModel

class Planing(BaseModel):
    id_planning: int
    title: str
    entreprise: int
    user: list[int]
    creation_at: str
    created_by: int
    start_date: str
    end_date: str
    description: str = None
    city: str = None
    adresse: str = None
    zipCode: str = None
    country: str = None

class PlaningOptionnalFields(BaseModel):
    title: str = None
    entreprise: int = None
    user: list[int] = None
    creation_at: str = None
    created_by: int = None
    start_date: str = None
    end_date: str = None
    description: str = None
    city: str = None
    adresse: str = None
    zipCode: str = None
    country: str = None