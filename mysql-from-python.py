import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        rows = [("Bill", 33, "1987-03-04 23:04:56"),
                ("Bob", 32, "1986-03-04 23:04:56"),
                ("Thornton", 31, "1985-03-04 23:04:56")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s );", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()