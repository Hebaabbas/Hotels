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

# Making the connection
with db.connect() as connection:
    # Example Query - Select all users
    select_query = users_table.select()

    # Execute the query and print results
    results = connection.execute(select_query)
    for result in results:
        print(result)