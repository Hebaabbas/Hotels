import psycopg2

connection = psycopg2.connect(database="data")

# build a cursor object of the database
    cursor = connection.cursor()

# Query 1 - Select all users
#cursor.execute('SELECT * FROM user')

# Query 2 - Select a specific user by username
#cursor.execute('SELECT * FROM user WHERE username = %s', ["exampleUsername"])

# Query 3 - Select all hotels
#cursor.execute('SELECT * FROM hotels')

# Query 4 - Select a specific hotel by name
#cursor.execute('SELECT * FROM hotels WHERE name = %s', ["HotelName"])

# Query 5 - Select all reviews for a specific hotel
#cursor.execute('SELECT * FROM review WHERE hotel = %s', [hotelId])  # assuming hotelId is an integer

# Query 6 - Select all reviews by a specific user
#cursor.execute('SELECT * FROM review WHERE user = %s', [userId])  # assuming userId is an integer

# Query 7 - Select all posts
#cursor.execute('SELECT * FROM post')

# Query 8 - Select a specific post by title
#cursor.execute('SELECT * FROM post WHERE title = %s', ["PostTitle"])

# Query 9 - Select posts related to a specific hotel
#cursor.execute('SELECT * FROM post WHERE hotel = %s', [hotelId])  # assuming hotelId is an integer

# Query 10 - Select posts made by a specific user
#cursor.execute('SELECT * FROM post WHERE user = %s', [userId])  # assuming userId is an integer

# fetch the results (multiple)
results = cursor.fetchall()

    # Print results
    for result in results:
        print(result)

except psycopg2.Error as e:
    print("Database error: ", e)

finally:
    cursor.close()
    connection.close()
