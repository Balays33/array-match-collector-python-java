from random import randrange
import random
import string


class Progress:
    def __init__(self, sizeofarray,name):
        self.sizeofarray = sizeofarray
        self.name = name
        myarray = []


#name = str(input("What is your name : "))
#sizeofarray = input("Size of the array : ")

#print(name)
#p1 = Progress(sizeofarray,name)

value = input("Please enter a string:\n")
 
print(f'You entered {value} and its type is {type(value)}')
 
value = input("Please enter an integer:\n")
 
print(f'You entered {value} and its type is {type(value)}')