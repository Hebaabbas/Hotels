from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, DateTime, ForeignKey, Text
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

# Class-based model for the "reactions" table
class Reaction(base):
    __tablename__ = "reactions"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    is_thumb_up = Column(Boolean)

# Create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# Opens an actual session by calling the Session() subclass defined above
session = Session()

# Creating the database using declarative_base subclass
base.metadata.create_all(db)

# Query 1 - Select all records from the "users" table
# users = session.query(User)
# for user in users:
    print(user.id, user.username, user.email, sep=" | ")

# Query 2 - Select only the "username" and "email" columns from the "users" table
# users = session.query(User.username, User.email)
#  for user in users:
#    print(user.username, user.email)

# Query 3 - Select a specific user by username
# user = session.query(User).filter_by(username="specific_username").first()
# if user:
#     print(user.id, user.username, user.email, sep=" | ")

# Query 4 - Select all hotels in a specific city
# hotels = session.query(Hotel).filter_by(city="specific_city")
# for hotel in hotels:
#     print(hotel.id, hotel.name, hotel.country, hotel.city, hotel.average_rating, sep=" | ")

# Query 5 - Select all reviews for a specific hotel
# reviews = session.query(Review).filter_by(hotel_id=specific_hotel_id)
# for review in reviews:
#     print(review.id, review.user_id, review.hotel_id, review.content, sep=" | ")

# Query 6 - Select all posts made by a specific user
# posts = session.query(Post).filter_by(user_id=specific_user_id)
# for post in posts:
#     print(post.id, post.title, post.content, post.user_id, post.hotel_id, sep=" | ")
