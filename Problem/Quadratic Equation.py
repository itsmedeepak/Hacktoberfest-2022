import math 
import numpy as np
from matplotlib import pyplot as plt
  
def f(x):
   return a*x*x + b*x + c 
def solve( a, b, c): 
    D = (b * b) - (4 * a * c) 
    if D > 0: 
        print(" Real and Unequal Roots! ")
        SD = math.sqrt(D) 
        print((-b + SD)/(2 * a)) 
        print((-b - SD)/(2 * a)) 
      
    elif D == 0: 
        print(" Real and Equal Roots!") 
        print(-b / (2 * a)) 
      
    
    else:
        print("Complex Roots!")
        SD = math.sqrt(abs(D)) 
        print(- b / (2 * a), " + i", SD) 
        print(- b / (2 * a), " - i", SD) 
  


print("Your Equation should be in the form ax^2 + bx + c = 0") 
a = float(input("Enter Coeff of x^2 : "))
b = float(input("Enter Coeff of x : "))
c = float(input("Enter rest of the constant terms : "))
  
print("Equation is :")
print("({}x^2) + ({}x) + ({}) = 0".format(a,b,c))
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True



x = np.linspace(-20 , 20)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.ylim(-10, 10)
plt.plot(x,f(x), 'r')
plt.show()

if a == 0: 
        print("This is a linear equation")
        sol = (-1)*c/b;
        print(sol); 
  
else:
    solve(a, b, c)
