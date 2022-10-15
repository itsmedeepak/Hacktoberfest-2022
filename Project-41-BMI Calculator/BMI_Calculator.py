Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("your wight is too low")
	elif(BMI<=18.5):
		print("your weight is less")
	elif(BMI<=25):
		print("your weight is perfect")
	elif(BMI<=30):
		print("your weight is too high please do the exercise")
	else: print("you are severely overweight")
else:("please enter valid height and weight")
