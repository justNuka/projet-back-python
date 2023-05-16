# System imports

# Libs imports
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy import Table, Column
# Local imports
from config.db import meta
from models.entreprise import Entreprise

entreprises = Table(
    "entreprise",meta,
    Column("id",Integer,primary_key=True),
    Column("nameFirm",String(255)),
    Column("location",String(255)),
)

class Entreprise(BaseModel):
    id: int = None
    nameFirm: str
    location: str

class EntrepriseOptionnalFields(BaseModel):
    nameFirm: str
    location: str