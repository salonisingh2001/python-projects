#Q1 Display user entered name followed by good afternoon .
greet="Good afternooon "
name=input("enter name : ")
print(greet+name)
print("***************************************************")

# Q2 wap to fill letter
#     letter ='dear <Name>
#                you are selected,
#                <date>'
               
date=input("enter date")
print("'Dear",name,"\n \t you are selected,\n\t",date,"'")

print("***************************************************")

#Q3Wap to detect double spaces
x="Hello  I am   Saloni   Rajput!"
print(x.count("  "))

print("***************************************************")

#Q4 Wap to replace double spaces with single

print(x.replace("  "," "))

print("***************************************************")

# Q5 Wap for escape sequence

print("Hello\nI am\t Saloni '\'Rajput\\Sallu!")

#Q2 Alternative method
letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''
name = input("Enter Your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

# Q3 alternative
st = "This is a string with double  spaces"

doubleSpaces = st.find("  ")
print(doubleSpaces)

##Q5 Alternative
letter = "Dear Harry, This Python course is nice! Thanks!"
print(letter)

formatted_letter = "Dear Harry,\n\tThis Python course is nice!\nThanks!"
print(formatted_letter)

