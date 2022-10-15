import math
a=int(input("Enter a number to check : "))
temp=a
ans=0
while a!=0:
    res = a % 10
    ans += math.pow(res,3)
    a //=10
if(temp==ans):
    print("This number is armmstrong")
else:
    print("This is not armstrong")