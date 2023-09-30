import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'grapes'
)

# prepare a cursor object
cursor_object = database.cursor()

# Create database
cursor_object.execute("CREATE DATABASE BraisonTechnologies")

print("Database created!")