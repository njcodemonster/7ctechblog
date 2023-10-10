from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 


from app.database import sessionmaker
from sqlalchemy.orm import Session 
SQLALCHEMY_DATABASE_URL = 'mysql://nctech6_master:Timbot1986.@205.134.238.117/nctech6_newBlog'
engine= create_engine(SQLALCHEMY_DATABASE_URL)
sessionmaker = sessionmaker( autoflush=True , bind = engine)

Base = declarative_base() 
