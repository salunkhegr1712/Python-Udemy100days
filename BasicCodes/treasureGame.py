import time

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")

#Write your code below this line 👇

print("In this game you have options and you have make choices and win treasure at last")

print("select one Left or Right : ")

a=input("")

if(a.lower()=="left"):
    print("You go to left side")
    time.sleep(2)
    print("You found a group on Wild animals")
    time.sleep(2)
    print("They followed you")
    time.sleep(2)
    print("You died!!")
    time.sleep(2)
    print("You loose!")
    exit(0)
else:
    print("You go to right side")
    time.sleep(2)
    print("You see a lake!")
    time.sleep(2)
    print("You see a Rhino at 200m and running towards you")
    time.sleep(2)
    print("You have two options Swim or Wait : ")
    a=input("")

if(a.lower()=="swim"):
    print("You started to swim")
    time.sleep(2)
    print("You are being followed by Shark")
    time.sleep(2)
    print("In middle you see a boat but it looks weak")
    time.sleep(2)
    print("Want to take boat yes or no : ")
    a=input("")
else:
    print("Rhino nearing distance")
    time.sleep(2)
    print("He came and killed you")
    time.sleep(2)
    print("you Loose!!")
    exit(0)


if a.lower()=="no":
    print("you swim fast")
    time.sleep(2)
    print("You reached island")
    time.sleep(2)
    print("You found a house on island")
    time.sleep(2)
    print("You go inside the house")
    time.sleep(2)
    print("You see 3 doors inside the house")
    time.sleep(2)
    print("Select one door from Blue Red Yellow \nselect one : " )
    a=input("")


else:
    print("You take boat")
    time.sleep(2)
    print("You tried to make it move")
    time.sleep(2)
    print("You created some distance from shark")
    time.sleep(2)
    print("Boat is broken due to your wait")
    time.sleep(2)
    print("You Fell in water and you died")
    print("you loose!")
    exit(0)

if a.lower()=="red":
    print("You Loose")
elif a.lower()=="blue":
    print("you loose")
else:
    print("You Win !!")