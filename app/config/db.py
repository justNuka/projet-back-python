# Libs imports
from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql + pymsql://root:root@localhost:3306/projet-back-python')
meta = MetaData()
conn = engine.connect()