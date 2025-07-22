#first day code after setting up python and vs code in my pc printing hello word and using strings and comments#

print("hello word")

#day2 of learning python modules and variables 

import pyjokes
print(pyjokes.get_joke())

# variables
a = 2
b = 4
print(a + b)

#building bmi calculator with the help of the learning the new and exciting things in python
 
a = int(input("enter bodyweight: ",  ))
b = float(input("enter height: ",   ))
b2= float(input("confirm height: ", ))
c = b * b2

print("the formula of calculating BMI is bodyweight/height*height: ", c)
bmi = a / c
print("bmi is: ", round(bmi,2))
