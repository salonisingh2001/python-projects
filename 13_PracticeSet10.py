#Q1 create a class programmer for storing information of few programmers working at microsoft.
class Programmer:
    company= "Microsoft"

    def __init__(self,name1):
        self.name=name1

    def getInfo(self):
        print(f"The company name of {self.name} is {self.company} ")

s=Programmer("saloni")
s.getInfo()

#Q2 write a class calculator , capable of calculating square, cube nd square root of a no.
import math
class Calculator:
    def __init__(self,a):
        self.no=a

    def square(self):
        print(f"Square of {self.no} is {self.no*self.no} or {self.no**2}")

    def cube(self):
        print(f"cube of {self.no} is {self.no*self.no*self.no} or {self.no**3}")
    
    def squareRoot(self):
        print(f"SquareRoot of {self.no} is { math. sqrt(self.no) } or {self.no**0.5}")
b=int(input("enter the no for square "))
x=int(input("enter the no for cube"))
y=int(input("enter the no for square root"))
s=Calculator(b)
c=Calculator(x)
sr=Calculator(y)
s. square() 
c.cube()  
sr.squareRoot()    

# #Q3 Create a class with a class attribute a; create an object from it and set a directly using object.a=0. does this change the class attributes?
class Check:
    a=10

obj=Check()
obj.a=0 
print(obj.a)

#Q4 write a static method to greet hello

@staticmethod
def greet():
        print("*******Hello *******")

#Q5 write a class train which has methods to book a ticket,get status (no. of seats)& get fare info of train running under Indian railways

class train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print(f"The name of train is {self.name}\nfare cost={self.fare}\n no. of seats left={self.seats}")
               
    def booking(self):
        if(self.seats>0):
           print(f"Booking successfull!!!! \n your seat no is {self.seats}")
           self.seats=self.seats-1
        else:
            print("SORRY!!! seats are full......\n Better luck next time")

Humsuffer=train("HumsafarExpress",110,2)
Humsuffer.getStatus()
Humsuffer.booking()
Humsuffer.booking()
Humsuffer.booking()
Humsuffer.getStatus()


#Can you change self parameter inside a class to something else (like "CS"). try changing self to "CS" & see effects
class change:
    def __init__(CS,name):
        CS.name=name
c1=change("CodinationStudy")       
print(c1.name)





