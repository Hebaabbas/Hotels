from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///data")
base = declarative_base()

Session = sessionmaker(db)
session = Session()

# Creating the database using declarative_base subclass
base.metadata.create_all(db)