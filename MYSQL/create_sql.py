# USE THE GIVEN LINK TO DOWNLOAD MYSQL CONNECTOR IN YOUR SYSTEM
# https://www.youtube.com/watch?v=SYAqSyNDK0Y
# CREATE DATABSE IN MYSQL USING PYTHON AND THE CONNECTOR

import mysql.connector

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="yourdatabase"
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
