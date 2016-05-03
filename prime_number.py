"""
PRIME NUMBER
A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.

"""

def is_prime(x):
    y = x
    while x >1:
        for n in range(x-1):
            if x%n == 0:
                return False
            else:
                return True


print is_prime(9)
