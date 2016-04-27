#BUILT IN FUNCTIONS

def is_numeric(num):
    return type(num) == int or type(num) == float:

max(2, 3, 4) # 4
min(2, 3, 4) # 2

abs(2) # 2
abs(-2) # 2


"""
First, def a function called distance_from_zero, with one argument (choose any argument name you like).
If the type of the argument is either int or float, the function should return the absolute value of the function input.
Otherwise, the function should return "Nope"

"""

# Sample code
def distance_from_zero(s):
    if type(s)==int or type(s) ==float:
        return abs(s)
    else:
        return "Nope"
