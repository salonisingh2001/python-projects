# #wap to print 1 to 50 using while loop
# i=0
# while(i<=50):
#     print(i)
#     i=i+1

# # wap to print contents of the list using while loop
# myFriendstList = ["devraj","akshat","bhavesh","simmi","deepesh","dishu","himanshu"]
# print(myFriendstList) 
# i=0
# while(i<=6):
#     print(myFriendstList[i])
#     i=i+1

# for item in myFriendstList:
#     print(item)

# # wap to print multiplication table of a given no entered  using while loop
# table=int(input("enter the no whoose table you want : "))
# i=1
# while(i<=10):
#     print(table,"*",i,"=",i*table)
#     i=i+1
# print("done")

# #wap to greet all the person names stored in a list whoose name starts with s
# #l1=["harry","sallu","simmi","jayu","sonu"]
# l1=["harry","sallu","simmi","jayu","sonu"]

# for name in l1:
#     if name.startswith("s"):
#         print("Hello " + name)

# # #wap to find whether a given no is prime or not
# from pickle import TRUE
# from stringprep import in_table_c11_c12


# x=int(input("enter a no "))
# prime=True

# if(x== 0 or x== 1):
#    prime=False

# for i in range(2,x):
#     if(x%i == 0):
#         prime = False
#         break
# if prime:
#     print("This number is Prime")
# else:
#     print("This number is not Prime")

# #wap to find sum of 1st n natural no
# num=int(input("enter a no "))
# i=num
# num=((num+1)*num)/2
# print("sum of the nos are ",num)
# #alternative
# n=int(input("enter a no "))
# n=i
# while(i>0):
#     i=i-1
#     n=n+i
   
# print("sum of the nos are ",n)

#wap to calculate factorial of a no
# z=int(input("enter a no "))
# x=z
# i=1
# while(i<x):     
#    z=z*(x-i)    
#    i=i+1        
# print("factorial is ",z)

#print star pattern
n=3
for i in range(3):
   print("*"*(i+1),end="\n")

n=3
for i in range(3):
   print(" "*(n-i-1),end="")   
   print("*"*(2*i+1),end="")   
   print(" "*(n-i-1),) 
print("\n")
print("*"*3,end="\n")
print("* *",end="\n")
print("*"*3,end="")

#wap to print multiplication table of n using for loop in reversed order
# num=int(input("enter the table no"))
# for i in range (10):
#    print(num*(10-i))