# System imports

# Libs imports
from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy import Table, Column
# Local imports
from config.db import meta
from models.entreprise import Entreprise


entreprises: list[Entreprise] = [
    {
        "id_entreprise": 1,
        "nameFirm": "PyLancer",
        "location": "Paris, France",
    },
    {
        "id": 2,
        "nameFirm": "KindleCestGénial",
        "location": "Etats-Unis, New-York",
    },
]