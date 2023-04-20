 #Q1
# x1 = int(input("Enter no 1: "))
# x2 = int(input("Enter no 2: "))

# a={x1,x2}
# if(x1>x2):
#     print(x1,"is greatest")
# else:
#     print(x2,"is greatest")
# #alternative
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# num4 = int(input("Enter number 4: "))

# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4

# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3

# if(f1>f2):
#     print(str(f1) + " is greatest")
# else:
#     print(str(f2) + " is greatest")

#Q2
# b1 = int(input("Enter Marks of subject 1: "))
# b2 = int(input("Enter Marks of subject 2: "))
# b3 = int(input("Enter Marks of subject 3: "))
# per=((b1+b2+b3)*100)/300
# print(per)
# if(60>per>=40):
#   print("just passed with c grade")
# elif(80>per>=60):
#    print("b grade")
# elif(100>per>=80):
#    print("A grade") 
# else:
#    print("fail")    
     
#Q3
# text = input("Enter the text\n")

# if("make a lot of money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This text is spam")
# else:
#     print("This text is not spam")

# #Q4
# username=input("enter username : ")
# x=len(username)
# if(x<10):
#     print("it contains less than 10 characters")
# else:
#     print("it contains more than equals to 10 characters")  

#Q5
# names=["akshat","bhanu","bhuppi","diya","kiran","simmi","jayuuu","deepesh"]
# name=input("enter your name if you are in sallu's close friend list or not : ")
# if name in names:
#     print(name,"is sallu's close friend")
# else:
#     print(name,"is not sallu's close friend")  

#multiple if statemets
# a=int(input("enter a no "))
# if(a>3):
#     print("greater than 3")
# if(a>13):
#     print("greater than 13")
# if(a>10):
#     print("greater than 10")
# if(a>7):
#     print("greater than 7") 
# in statement work
# a=[12,13,14,15,16,17,18]
# for item in a:
#     print(item)

# if(12 in a):
#     print("yes ")
# else:
#     print("no")        

# #is statement 
b=None
if(b is not None):
    print("yes")
else:
    print("no ")

if(b is None):
    print("y")
else:
    print("n ")    
