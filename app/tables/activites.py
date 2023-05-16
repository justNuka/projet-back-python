#System import

#Libs import
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String, DateTime

#Local import
from config.db import meta

activites = Table(
    "activites",meta,
    Column("id",Integer,primary_key=True),
    Column("title",String(255)),
    Column("entreprise",Integer),
    Column("user",String(255)),
    Column("created_by",Integer),
    Column("start_date",DateTime),
    Column("end_date",DateTime),
    Column("description",String(255)),
    Column("city",String(255)),
    Column("address",String(255)),
    Column("zipCode",String(255)),
    Column("country",String(255)),
)