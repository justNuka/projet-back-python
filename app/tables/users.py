#System import

#Libs import
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String, Boolean, LargeBinary

#Local import
from config.db import meta

users = Table(
    "user",meta,
    Column("id",Integer,primary_key=True),
    Column("name",LargeBinary),
    Column("surname",LargeBinary),
    Column("email",LargeBinary),
    Column("password_hash",String(255)),
    Column("tel",LargeBinary),
    Column("maintainer",Boolean),
)