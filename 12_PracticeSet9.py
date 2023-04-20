#Q1 wap to read the text from a given file poem.txt and find whether it contains the word "twinkle"
f = open('poem.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()

#Q2 wap to update hi score whenever game() breaks the hi-score 
def game():
    return 44677

score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()
    
if hiScoreStr=='':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score :
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

#Q3 wap to write table from 2 to 20 in a folder and different different file
for i in range(2, 21):
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}")
            if j!=10:
                f.write('\n')

#Q4 wap to replace donkey with $%^@$^# in hiscore.txt file
with open("hiscore.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#")

with open("hiscore.txt", "w") as f:
    f.write(content)

#Q5 repeat program 4 for list for such words to be censsored    
words = ["donkey", "kaddu", "mote"]

with open("sample.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%^@$^#")
    with open("sample.txt", "w") as f:
        f.write(content)

#Q6 wap to find if python is presemt or not
with open("hiscore.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes python is present")
else:
    print("No python is not present")

#Q7 wap to find the line of python present in file 
content = True
i = 1
with open("hiscore.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}") 
        i+=1
      
#Q8 wap to make copy of text file
with open("hiscore.txt") as f:
    content = f.read()

with open("copy.txt", 'w') as f:
    f.write(content)

#Q9 wap to find whetehr the file is identical or has some match with othefile1 = "log.txt"
file1 = "hiscore.txt"
file2 = "copy.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2= f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")

#Q10 wap to wipe out contents of file using 
filename = "copy.txt"
with open(filename, "w") as f:
    f.write("")

#Q11 wap to rename a file
import os

oldname = "copy.txt"
newname = "renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)