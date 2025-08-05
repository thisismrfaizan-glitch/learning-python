#string slicing 
#string slicing is used to access a part of the string
#it is done by using the square brackets [] and specifying the start and end index of the string
#start index is counted and end index is excluded 
#in python or other programming languages, the index starts from 0

name = "shaikh faizan"
slicing = name[1:8]  
print(slicing)
#output would be "haikh f" 
#slicing can also be done with negative indices
negative_slicing = name[-10 : -2]
print(negative_slicing)

# special slicing types 
name2 = "hello shaikh faizan"
a = name2[:8] #when there is only end index is given it means it will start from the begginingrespectivly when end index isn't given this means it will go till the end of the string( mean length of the string).
b = name2[8:]
print(a)
print(b)