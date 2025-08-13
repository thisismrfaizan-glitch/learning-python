#chapter3_practice_set.py

#problem 1
# a python program to display a user enteredname followed by good afternoon using input() function
name = input("enter the name : ")
print(f"Good Afternoon {name}" )

#problem 2
# write a program to fill in a letter template given below with name and date 

letter = '''Dear<|Name|>, 
You are selected!
<|Date|> '''
            
name = input("enter the name: ")
date = str(input("enter the date: "))
a1 = (letter.replace("Name",name))
a2 = (a1.replace("<|Date|>",str(date)))
print(a2)

# problem 3
# write a program to detect double space in a string
string = "faizan is very genuine and real person he loves to do  self improvement rather than correcting others"
print(string.find("  "))
#if double space is found than its output would be its index otherwise it would be -1
#in above string its index is 53. means its occurance is at 53rd index
# if we want to replace double space with single space to correct it 
print(string.replace("  ", " " ))

#problem 4
# replace the double space from problem 3 with single space
string = "faizan is very genuine and real person he loves to do  self improvement rather than correcting others"
print(string.replace("  ", " "))
# this will correct the double space issue in the string

#problem 5
# write a program to format the following letter using escape sequence characters
letter = "Dear Faizan, this python practice is going great. keep it up!"
proper_letter =  "Dear Faizan:\n \t This \"Python\" practice is going great.\n\t Keep it up!"
print(proper_letter)
# this will print the letter with proper formatting using escape sequence characters
