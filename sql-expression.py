from sqlalchemy import create_engine, Table, Column, Integer, String, Boolean, Text, Float, DateTime, MetaData, ForeignKey

# Assuming the database is "data"
db = create_engine("postgresql:///data")
meta = MetaData(db)

# Making the connection
with db.connect() as connection:
    # Example Query - Select all users
    select_query = users_table.select()

    # Execute the query and print results
    results = connection.execute(select_query)
    for result in results:
        print(result)