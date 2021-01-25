# Perform addition
def add(x,y):
    return x+y
# Perform subtraction
def subtract(x,y):
    if x<y:
        return Error
    return x-y
# Perform multiplication
def multiply(x,y):
    return x*y
    
# Perform division
def divide(x,y):
    if y==0:
        return Divide_By_0_Error
    return x/y
def square(x):
    return x*x
