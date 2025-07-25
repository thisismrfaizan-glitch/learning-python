#practice of basics that learned in previous days

#print hello word

print("hello world")

#adding two variables

a = 25
b = 30
print(a+b)

#finding remainer of the numbers

a = 52
b = 30

print("the remainder of the given numbers are :  ", a % b)

# finding types of the variables

a = ("faizan")
b = ("14.85")
c = (12)
d = (12.45)
e = ("shaikh") 
f = 45 + 18

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(f)

#finding out the graeter number with the help of comparission operator

a = 34
b = 80
print(a>b)

#finding average of two numbers entered by the user

a = float(input("Enter the first number: ", ))
b = float(input("Enter the second number: ", ))

print("The average of two number given is: ", (a+b)/2)

#finding the percentage of the numbers entered by user

a = float(input("Enter the marks you got: ", ))
b = float(input("Enter the total marks: ", ))

print("The percentage you got is: ", ((((a)/(b))*100)) , ("%"))

#Improved version of finding percentage with the help of AI


print("Finding the percentage of the numbers entered by user")


marks_obtained = float(input("Enter the marks you got: "))
total_marks = float(input("Enter the total marks: "))
percentage = (marks_obtained / total_marks) * 100
print(f"The percentage you got is: {percentage:.2f}%")
