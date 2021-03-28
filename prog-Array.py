from random import randrange
import random
import string

myarray = []

class Progress:
    def __init__(self, sizeofarray,name,myarray):
        self.sizeofarray = sizeofarray
        self.name = name
        self.myarray = myarray
        caraterNumber = 3

    def createArray1(self):
        i=0
        #print(self.sizeofarray)
        
        if int(self.sizeofarray)<50:
            self.sizeofarray =50
            print(self.sizeofarray)
            
        while i<self.sizeofarray:
            #print(i)
            mystring =""
            for x in range(3):
                #print(x)
                randomCH = chr(random.randint(ord('a'), ord('z'))) 
                mystring += randomCH
            myarray.append(mystring)
            i+=1
               
          
        return(myarray)
        
    def welcome(self):
        print("Hello {}".format(name))
        
    


name = str(input("What is your name : "))
sizeofarray = input("Size of the array : ")


p1 = Progress(sizeofarray,name,myarray)

p1.welcome()
p1.createArray1()