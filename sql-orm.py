from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Assuming the database is "data"
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

# Create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# Opens an actual session by calling the Session() subclass defined above
session = Session()

# Creating the database using declarative_base subclass
base.metadata.create_all(db)