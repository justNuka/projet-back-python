#System imports

# Libs imports
from sqlalchemy import create_engine, MetaData
# Local imports

username = 'root'
password = 'root'
host = 'localhost'
port = '3306'
database = 'projet-back-python'

# Connexion à la base de données
db_url = f'mysql+pymsql://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(db_url)
meta = MetaData()
conn = engine.connect()