# #wap to find greatest of 3 nos using functions

# def greatest(l1,l2,l3):
#     if(l1>l2 and l1>l3):
#        return(l1)
#     elif(l2>l1 and l2>l3):
#       return(l2)
#     else:
#       return(l3)  
     
# w1=greatest(2,3,1)
# print("greatest no is ",w1)
# w2=greatest(29,4,786)
# print("greatest no is ",w2)
# w3=greatest(29,89,78)
# print("greatest no is ",w3)
 
# #wap to convert celcius to farenheit
# def farh(cel):
#   return (cel *(9/5)) + 32

# c = int(input("enter temp in celcius"))
# f = farh(c)
# print("Fahreheit Temperature is " + str(f))

# #write a recursive function to calculate the sum of n natural nos
# n=int(input("enter no"))
# def sum(n): 
#   if (n == 0): 
#     return 0
#   else: 
#     return n + sum(n - 1)
# print("sum is",sum(n))    

# #wap to print 1st n lines of the following pattern
# x=int(input("enter the no"))
# for i in range (x):
#   print("*"*x,end="\n")
#   x=x-1
  
# #wap to convert inches into cm
# def cm(inches):
#    return(inches*2.54)
# c= int(input("enter the no in cm "))
# i=cm(c)
# print("inches is " + str(i))

#wap to remove a given word from list strip it at the same time
def remove_and_split(string, word):
    newStr = string.replace(word,"")
    return newStr.strip()

this = "      Harry is a good      "
n = remove_and_split(this, "Harry")
x=remove_and_split("hello aisha!","hello")
print(x)
print(n)
print(this)
print(this.strip())

     