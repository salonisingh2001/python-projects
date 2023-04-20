import random
def gameWin(comp,you):
   if comp==you:
    return None
   elif comp=='s':
      if you =='p':
        return False
      elif you=='sc':
        return True
   elif comp=='p':
      if you =='sc':
        return False
      elif you=='s':
        return True
   elif comp=='sc':
      if you =='s':
        return False
      elif you=='p':
        return True     


print(" comp choosed: scissor(s) Paper(p) or stone(sc)")
randNo=random.randint(1,3)

if randNo==1:
    comp='s'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='sc'    
you=input("Players Turn : scissor(s) Paper(p) or stone(sc)")

print(f"comp choose {comp}")
print(f"you choose {you}")

a=gameWin(comp,you)
if a==None:
    print("tie")
elif a:
    print("you win")
else:
    print("comp wins")        