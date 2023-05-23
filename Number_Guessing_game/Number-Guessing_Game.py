           # using Random Module
import random
computer=random.randrange(1,101)
userinput=int(input("Enter Your Guess Number:--"))
if userinput>computer:
    print("computer Guess Number:--",computer)
    print("You are win😊😍🤩")
elif computer>userinput:
    print("computer Number:--", computer)
    print("You are lost😥😪😭")
else:
    print("computer Guess Number", computer)
    print("Your Guess Number is Same🤪")