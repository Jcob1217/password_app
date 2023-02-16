import mysql.connector
from datetime import datetime
import password_generator as pg

# Creatin connection to existing database connection
db = mysql.connector.connect(
    host="localhost",
    user="",  # connection user
    passwd="",  # connection password
    database = "" # database name
    )

# Creating database cursor
cursor = db.cursor()

# Creating database
'''
cursor.execute("""CREATE TABLE passwords (
                                    password_id INT PRIMARY KEY AUTO_INCREMENT,
                                    service varchar(50) NOT NULL,
                                    password varchar(50) NOT NULL
)""")
'''

cursor.execute("SELECT * FROM passwords")

# Printing existing passwords
for x in cursor:
    print(f"Service: {x[1]}")
    print(f"Password: {x[2]}")
    print("")

add_password = input("Do you want to add new password? (y/n):  ").lower()

if add_password == "y":
    service = input("What service is password for? ")
    auto_generated = input("Do you want your password to be automatically generated? (y/n): ") 
    if auto_generated == "y":
        password_criteria = pg.criteria_input()
        password = pg.generate_password(*password_criteria)
    else:
        password = input("New password: ")

    cursor.execute("INSERT INTO passwords (service, password) VALUES (%s, %s)", (service, password))
    db.commit()
