# to search in mysql database using binary search, you have to import mysql connectorto connect database and python code
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

import functools

# establish connection with database to search in it 
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="yourpassword",
database="yourdatabasename"
)

db = mydb.cursor()

db.execute("SELECT roll_no from students")
data = db.fetchall()
rollno = []

for x in data:
    rollno.append(functools.reduce(lambda sub, ele: sub*10+ele, x))

print("List of Roll No. : ")
rollno.sort()
print(rollno)

roll = input("Enter roll no: ")

# use binary search to search for a particular roll no
def binary_search(arr, low, high, number):
    if high >= low:
        mid = (high + low) // 2
        if (arr[mid] == number):
            return mid
        elif (arr[mid] > number):
            return binary_search(arr, low, mid-1, number)
        else:
            return binary_search(arr, mid+1, high, number)
    else:
        return -1

r = binary_search(rollno, 0, len(rollno), roll)
if r != -1:
    print("Element found at index", str(r))
else:
    print("Element is not present in database")