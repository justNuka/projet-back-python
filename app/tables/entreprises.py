#System import

#Libs import
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String

#Local import
from config.db import meta

entreprises = Table(
    "entreprise",meta,
    Column("id",Integer,primary_key=True),
    Column("nameFirm",String(255)),
    Column("location",String(255)),
)