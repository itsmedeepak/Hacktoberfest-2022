import random 
import mysql.connector as sqls
mycon=sqls.connect(host="localhost",user="root",passwd="root",database="bank")
cursor = mycon.cursor()
if mycon.is_connected():
    print("connected")


def deposit():
    x=int(input("Enter amount to be deposited:"))
    y=int(input("Enter your account no:"))
    st="update clients set accbalance=accbalance+{} where accno={}".format(x,y)
    cursor.execute(st)
    mycon.commit()
    print('transaction complete!')

def withdraw():
    x=int(input("enter amount to be withdrawn:"))
    y=int(input("enter your account no:"))
    st="update clients set accbalance=accbalance-{} where accno={}".format(x,y)
    cursor.execute(st)
    mycon.commit()
    print('transaction complete!')

def transfer():
    x=int(input("enter amount to be transfered"))
    y=int(input("enter your account no"))
    z=int(input("enter the account no of the payee"))
    st="update clients set accbalance=accbalance-{} where accno={}".format(x,y)
    cursor.execute(st)
    mycon.commit()
    st="update clients set accbalance=accbalance+{} where accno={}".format(x,z)
    cursor.execute(st)
    mycon.commit()
    print("Transaction complete!")
    
def balance():
    x=int(input("enter your account number"))
    st="select * from clients where accno={}".format(x)
    cursor.execute(st)
    data=cursor.fetchall()
    for row in data:
        print(row)

def loan():
     print("1","interest rate (1year)=15%")
     print("2","interest rate(2 year)=9%")
     print("3","interest rate(3 year)=7%")
     print("5","interest rate(more than 3 years)=5%")
     time=int(input("enter the time to repay the loan(in years):"))
     if time==1 or time==2 or time==3 or time>3:    
         if time==1:
                 amount=int(input("enter the amount of loan:"))
                 interest=int((amount*1*15)/100)    
         elif time==2:
                 amount=int(input("enter the amount of loan:"))
                 interest=int((amount*2*9)/100)
         elif time==3:
                 amount=int(input("enter the amount of loan:"))
                 interest=int((amount*3*7)/100)         
         elif time>3:
                 amount=int(input("enter the amount of loan:"))
                 interest=int((amount*10*4)/100)
         print( "interest amount=",interest)
         print("Do you want the loan?")
         print("1.Yes")
         print("2.No")
         ch=int(input("enter your choice number:"))
         if ch==1:
                 y=int(input("enter your accountno:"))
                 st="update clients set accbalance=accbalance+{} where accno={}".format(interest,y)
                 cursor.execute(st)
                 mycon.commit()
                 print('loan granted!')

         else:
                print("unvalid choice")                  


def delete():
    x=int(input("enter your account number:"))
    st="delete from clients where accno={}".format(x)
    cursor.execute(st)
    mycon.commit()
    print("Account deleted!")        
    
logic=input("do you have an existing account(y/n)")
if logic=="y":
   ch=1
   while ch!=7:
       print("MAIN MENU")
       print("1) Withdraw money from your account")
       print("2) Deposit money in your account")
       print("3) View the balance")
       print("4) Take a loan")
       print("5) Transfer money")
       print("6) Delete account")
       print("7) Exit")
       ch=int(input("enter your choice(1-7):"))

       if ch==1:
           withdraw()
       elif ch==2:
           deposit()
       elif ch==3:
           balance()
       elif ch==4:
           loan()    
       elif ch==5:
           transfer()
       elif ch==6:
           delete()    
else:
    x=input("enter your name:")
    y=int(input("enter your starting balance:"))
    z=random.randrange(1000000,9999999)
    print("your account number is",z)
    st="insert into clients values('{}',{},{})".format(x,z,y)
    cursor.execute(st)
    mycon.commit()
    print("Account succcessfully created!")           
mycon.close() 
