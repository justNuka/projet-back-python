#System import

#Libs import
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String

#Local import
from config.db import meta

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