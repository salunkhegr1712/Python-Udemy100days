
def addition(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    # rounding up the floating value upto 2 digits after point 
    return round(a/b,2)

# we are able to perforn the functional programming inside the py 

def calcalution(op,a,b):
    # here we are using the parameter as the function name 
    return op(a,b)
    

pi=3.145
