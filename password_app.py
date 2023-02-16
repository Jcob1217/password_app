import mysql.connector
from datetime import datetime
import password_generator as pg

db = mysql.connector.connect(
    host="localhost",
    user="jacob",
    passwd="1217",
    database = "password_database"
    )

cursor = db.cursor()


'''
cursor.execute("""CREATE TABLE passwords (
                                    password_id INT PRIMARY KEY AUTO_INCREMENT,
                                    service varchar(50) NOT NULL,
                                    password varchar(50) NOT NULL
)""")
'''


# cursor.execute("INSERT INTO passwords (service, password) VALUES (%s, %s)", ("facebook", "dd6^7t&^G^@h"))
# db.commit()


cursor.execute("SELECT * FROM passwords")

for x in cursor:
    print(f"Service: {x[1]}")
    print(f"Password: {x[2]}")
    print("")

# data = pg.criteria_input()

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
