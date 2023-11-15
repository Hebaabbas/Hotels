from sqlalchemy import create_engine, Table, Column, Integer, String, Boolean, Text, Float, DateTime, MetaData, ForeignKey

# Assuming the database is "data"
db = create_engine("postgresql:///data")
meta = MetaData(db)

# Define the "users" table
users_table = Table(
    "users", meta,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), nullable=False),
    Column("email", String(100), nullable=False),
    Column("firstname", String(100)),
    Column("lastname", String(100)),
    Column("is_staff", Boolean, default=False),
    Column("is_supervisor", Boolean, default=False),
    Column("password", String(255))
)
# Define the "hotels" table
hotels_table = Table(
    "hotels", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    Column("country", String(100)),
    Column("city", String(100)),
    Column("average_rating", Float(precision=2, scale=1))
)
# Define the "reviews" table
reviews_table = Table(
    "reviews", meta,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("hotel_id", Integer, ForeignKey("hotels.id")),
    Column("review_date", DateTime, default="CURRENT_TIMESTAMP"),
    Column("content", Text),
    Column("room_type", String(100)),
    Column("duration", Integer),
    Column("spa", Boolean),
    Column("breakfast", Boolean)
)
# Define the "posts" table
posts_table = Table(
    "posts", meta,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("content", Text),
    Column("post_date", DateTime, default="CURRENT_TIMESTAMP"),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("hotel_id", Integer, ForeignKey("hotels.id"))
)
# Define the "comments" table
comments_table = Table(
    "comments", meta,
    Column("id", Integer, primary_key=True),
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("content", Text),
    Column("comment_date", DateTime, default="CURRENT_TIMESTAMP")
)
# Define the "reactions" table
reactions_table = Table(
    "reactions", meta,
    Column("id", Integer, primary_key=True),
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("is_thumb_up", Boolean)
)
# Making the connection
with db.connect() as connection:
    # Example Query - Select all users
    select_query = users_table.select()

    # Execute the query and print results
    results = connection.execute(select_query)
    for result in results:
        print(result)