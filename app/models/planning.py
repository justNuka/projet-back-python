# System imports

# Libs imports
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy import Table, Column
# Local imports
from config.db import meta
from models.entreprise import Entreprise

plannings = Table(
    "planning",meta,
    Column("id",Integer,primary_key=True),
    Column("title",String(255)),
    Column("entreprise",Integer),
    Column("user",String(255)),
    Column("creation_at",String(255)),
    Column("created_by",Integer),
    Column("start_date",String(255)),
    Column("end_date",String(255)),
    Column("description",String(255)),
    Column("city",String(255)),
    Column("address",String(255)),
    Column("zipCode",String(255)),
    Column("country",String(255)),
)

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