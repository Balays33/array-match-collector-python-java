print('This is a pytone progarm')
print('array-match-collector-python')



from random import randrange
import random
import string
print(randrange(10))

     
# Randomly choose a letter from all the ascii_letters 
randomLetter = random.choice(string.ascii_letters) 
print(randomLetter)

# Randomly generate a ascii value 
# from 'a' to 'z' and 'A' to 'Z' 
randomLowerLetter = chr(random.randint(ord('a'), ord('z'))) 
randomUpperLetter = chr(random.randint(ord('A'), ord('Z'))) 
print(randomLowerLetter, randomUpperLetter)


myarray = []
inputNumber = input("Size of the array : ")
i = 0
# size of the array
if inputNumber<50:
    inputNumber =100
  
while i<inputNumber:
    #print(i)
    mystring =""
    for x in range(3):
        #print(x)
        randomCH = chr(random.randint(ord('a'), ord('z'))) 
        mystring += randomCH
    myarray.append(mystring)
    i+=1
    
print(myarray)


