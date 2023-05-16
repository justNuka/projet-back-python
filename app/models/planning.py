# System imports
from enum import Enum
# Libs imports
from pydantic import BaseModel

class Planning(BaseModel):
    id: int = None
    title: str
    entreprise: int
    user: list[int]
    creation_at: str
    created_by: int
    start_date: str
    end_date: str
    description: str = None
    city: str = None
    address: str = None
    zipCode: str = None
    country: str = None

class PlanningOptionnalFields(BaseModel):
    title: str = None
    entreprise: int = None
    user: list[int] = None
    creation_at: str = None
    created_by: int = None
    start_date: str = None
    end_date: str = None
    description: str = None
    city: str = None
    address: str = None
    zipCode: str = None
    country: str = None