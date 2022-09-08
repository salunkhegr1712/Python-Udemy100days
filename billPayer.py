import random


a=input("input names comma seperated : ")
c=a.split(",")
n=random.randint(0,len(c)-1)
# print(c)
print(f"{c[n]} will pay the bill")
# print(n)
