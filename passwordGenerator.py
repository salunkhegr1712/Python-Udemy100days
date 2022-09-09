
import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(letters))
numbers = "0123456789"
symbols = "!#$%&()*+"


def easyPass(a,b,c):
    # a count of alphabets
    # b count of special character
    # c count of number
    size=a+b+c
    passwd=""
    for i in range(size):
        if i<=a:
            passwd+=letters[random.randint(0,51)]
        elif i<=a+b and i>a:
            passwd+=symbols[random.randint(0,8)]
        else:
            passwd+=numbers[random.randint(0,9)]

    return passwd

def hardPass(a,b,c):
    l=[str(letters),str(symbols),str(numbers)]
    print(l)
    size=a+b+c
    aa=0;bb=0;cc=0
    n=random.randint(0,2)
    g=random.randint(0,len(l[n])-1)
    paswd=""
    while len(paswd)!=size:
        n=random.randint(0,2)
        g=random.randint(0,len(l[n])-1)
        if(n==0 and aa<a):
            aa+=1
            paswd+=(l[0])[g]
        elif(n==1 and bb<b):
            bb+=1
            paswd+=(l[1])[g]
        elif (n==2 and cc<c):
            cc+=1
            paswd+=(l[2])[g]
    return paswd


a=hardPass(10,1,4)
print(a)
print(len(a))