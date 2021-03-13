print("Welcome to the function")
def function1(a,b,c):    #defining the variables in function
    """This is used to calculate for three numbers only"""
    print("Thanks for use the function")
    mul = a + b + c
    return mul    #return value of mul to v after doing operaation
v = function1(4, 9, 10)
print(v)
print(function1.__doc__)    #this line is used to print the docstring

