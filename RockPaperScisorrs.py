# Rock Paper Scissors ASCII Art
from ast import Assign
import numbers
import random
from tokenize import Number

from cupshelpers import Printer

l=["""
     _______
---'    ____)____
           ______)
          _______)  
         _______)
---.__________)
""",
"""
    _______
---'   ____)
      (_____)
      (_____)       
      (____)
---.__(___)
""",
"""
    _______
---'   ____)____
          ______)
       __________)   
      (____)
---.__(___)
"""
]

# print(l[0])

print("You can select between  0 for Rock, 1 for Paper, 2 for Scissors")
a=int(input("Enter your choice : "))

# example of Assigning value to the string and further we can apply function with them 
# f={0:"rock",1:"paper",2:"scissors"}

number=random.randint(0,2)
# print(number)

# handling all of the Condition 
if(a==number):
    print(f"You Choose : \n {l[a]}")
    print(f"Computer Choose : \n {l[number]}")
    print("A Draw !!")
elif((a==0 and number==1) or (a==1 and number==2) or (a==2 and number==0)):
    print(f"You Choose : \n {l[a]}")
    print(f"Computer Choose : \n {l[number]}")
    print("You Won !!")
else:
    print(f"You Choose : \n {l[a]}")
    print(f"Computer Choose : \n {l[number]}")
    print("Computer Won !!")
 