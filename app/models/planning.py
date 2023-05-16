# System imports

# Libs imports
from pydantic import BaseModel

# Local imports


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