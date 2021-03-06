"""
PRIME NUMBER
A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.

"""

def is_prime(x):
    if x<2:
        return False
    elif x>=2:
        for n in range(2, x):
            if x%n == 0:
                return False
    return True

print is_prime(int(raw_input("Enter any number")))
