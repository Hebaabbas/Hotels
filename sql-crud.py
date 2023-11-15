from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///data")
base = declarative_base()

# Class-based model for the "users" table
class User(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(100))
    firstname = Column(String(100))
    lastname = Column(String(100))
    is_staff = Column(Boolean)
    is_supervisor = Column(Boolean)
    password = Column(String(255))

Session = sessionmaker(db)
session = Session()

# Creating the database using declarative_base subclass
base.metadata.create_all(db)