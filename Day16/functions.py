a = 1
b =2
def multiplication(a,b):
    print("Multiplication of a * b = ", a*b)
def sub(a,b):
    print("Subtraction of a and b = ", a - b)

x = 5
y = 2
def multiplication(x,y):
    print("Multiplication of x * y = ", x*y)
def sub(x,y):
    print("Subtraction of x and y = ", x - y)
def addition():
    pass #pass means i will get back to it later, for now move on to next line. 

# note: since i am using the same function name so it overwrites the print function, but the parameter is  used from a, b. so we should avoid using same function names. 
multiplication(a,b)
sub(x,y)
sub (a,b)