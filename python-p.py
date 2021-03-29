from random import randrange
import random
import string

myarray = []
myarray2 = []
myarray3 = []

class Progress:
    def __init__(self, sizeofarray,name,myarray,myarray2,myarray3):
        self.sizeofarray = sizeofarray
        self.name = name
        self.myarray = myarray
        self.myarray2 = myarray2
        self.myarray3 = myarray3
        caraterNumber = 3

    def createArray1(self):
        i=0
        #print(self.sizeofarray)
        
        if int(self.sizeofarray)<50:
            self.sizeofarray =50
            #print(self.sizeofarray)
        elif int(self.sizeofarray)>100:
            self.sizeofarray =1000
        else:
            print("OK progress")
        
        
        while i<int(self.sizeofarray):
            #print(i)
            mystring =""
            for x in range(3):
                #print(x)
                randomCH = chr(random.randint(ord('a'), ord('z'))) 
                mystring += randomCH
            myarray.append(mystring)
            i+=1
        i=0
        while i<int(self.sizeofarray):
            #print(i)
            mystring =""
            for x in range(3):
                #print(x)
                randomCH = chr(random.randint(ord('a'), ord('z'))) 
                mystring += randomCH
            myarray2.append(mystring)
            i+=1
        i=0
        while i<int(self.sizeofarray):
            #print(i)
            mystring =""
            for x in range(3):
                #print(x)
                randomCH = chr(random.randint(ord('a'), ord('z'))) 
                mystring += randomCH
            myarray3.append(mystring)
            i+=1
        return(myarray,myarray2,myarray3)
        
    def welcome(self):
        print("Hello {}".format(name))
        
    def sortoutArray(self,myarray):
        #print(myarray)
        myarray.sort()
        #print(myarray)
        return myarray
        
    def findmatch(self,myarray,myarray2,myarray3):
        howmanyMatch =0
        #print (len(myarray))
        for x in range(len(myarray)-1):
            for y in range(len(myarray)):
                if myarray[x]==myarray2[y]:
                    for z in range(len(myarray)):
                        if myarray2[y]==myarray3[z]:
                            howmanyMatch += 1
                            print("this is the position first array {} and this is the code {} ".format(x,myarray[x]))
                            print("this is the position second array {} and this is the code {} ".format(y,myarray2[y]))
                            print("this is the position third array {} and this is the code {} ".format(z,myarray3[z]))
                                   
        return howmanyMatch
        


name = str(input("What is your name : "))
sizeofarray = input("Size of the array : ")


p1 = Progress(sizeofarray,name,myarray,myarray2,myarray3)

p1.welcome()
p1.createArray1()
#print("This is the first before sort array{}".format(myarray))
#print("This is the second before sort array{}".format(myarray2))
p1.sortoutArray(myarray)
p1.sortoutArray(myarray2)
p1.sortoutArray(myarray3)
#print("This is the first array{}".format(myarray))
#print("This is the second array{}".format(myarray2))
#print("This is the third array{}".format(myarray3))
p1.findmatch(myarray,myarray2,myarray3)
