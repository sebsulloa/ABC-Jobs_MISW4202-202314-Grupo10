from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///aplicacion.sqlite', pool_size=10)
Session = sessionmaker(bind=engine)

Base = declarative_base()
session=Session()