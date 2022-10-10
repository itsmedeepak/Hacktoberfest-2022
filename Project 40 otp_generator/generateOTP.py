import random
def otp(num):
    result=""
    if(len(str(num))==10):
        for i in range(6):
            digit=str(random.randint(0,9))
            result=result+digit
        return "Your OTP is: "+result
    else:
        s="Enter a valid mobile number!"
        return s
number=int(input("Enter mobile number: "))
print(otp(number))