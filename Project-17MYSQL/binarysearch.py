import mysql.connector 
import functools

# connection with the database and implementing binary search in it
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Nerachanan123#",
database="college"
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