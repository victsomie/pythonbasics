#print "Test factorial"
"""
To calculate the factorial of a non-negative integer x, just multiply all the integers from 1 through x. For example:

factorial(4) would equal 4 * 3 * 2 * 1, which is 24.
factorial(1) would equal 1.
factorial(3) would equal 3 * 2 * 1, which is 6.
"""



def factorial(x):
    fact = 1 #Declares a memory location to store the product of the factorial

    while x>0:
        fact = fact * x
        x = x-1 #Decreaments by one on each iteration
    return fact


print factorial(3)
