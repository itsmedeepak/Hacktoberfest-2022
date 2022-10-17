# to search in mysql database using binary search, you have to import mysql connector to connect the database and python code
# MYSQL WORKBENCH is used for creating a database 
# you can use the given link to download mysql connector in your system
# https://www.youtube.com/watch?v=SYAqSyNDK0Y

import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="yourdatabasename"
    )

    sql = """INSERT INTO students (roll_no) 
            VALUES (2104220),(2104210),(2104221),(2104279),(2104215)"""
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "Record inserted successfully")
    mycursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

# database created and data inserted successfully
