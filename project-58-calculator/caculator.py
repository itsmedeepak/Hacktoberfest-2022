def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2
def mod(num1,num2):
    return num1 % num2
def xor(num1,num2):
    return num1^num2
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. Modulus\n" \
        "6. Xor\n")


select = int(input("Select operations form 1, 2, 3, 4, 5 6:"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
elif select == 5:
    print(number_1, " % ", number_2, "=", mod(number_1,number_2))
elif select ==6:
    print(number_1, " xor ", number_2, "=", xor(number_1,numer_2))
else:
    print("Invalid input")
