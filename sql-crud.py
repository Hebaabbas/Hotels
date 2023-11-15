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

# Class-based model for the "hotels" table
class Hotel(base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    country = Column(String(100))
    city = Column(String(100))
    average_rating = Column(Float)

# Class-based model for the "reviews" table
class Review(base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    review_date = Column(DateTime)
    content = Column(Text)
    room_type = Column(String(100))
    duration = Column(Integer)
    spa = Column(Boolean)
    breakfast = Column(Boolean)

# Class-based model for the "posts" table
class Post(base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(Text)
    post_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    hotel_id = Column(Integer, ForeignKey('hotels.id'))

# Class-based model for the "comments" table
class Comment(base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    content = Column(Text)
    comment_date = Column(DateTime)
    
                
Session = sessionmaker(db)
session = Session()

# Creating the database using declarative_base subclass
base.metadata.create_all(db)