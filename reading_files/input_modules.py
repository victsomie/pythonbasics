#!/usr/bin/python
"""


To run the program you must pass three command line arguments):
"""

from sys import argv

"""
first = raw_input("First entry: ")
second = raw_input("Second entry: ")
third = raw_input("Third entry: ")
"""

script, first, second, third = argv #Take whatever is in argv, unpack it, and assign it to all these variables on the left in order.


prompt users response
first = raw_input("First entry: ")
second = raw_input("Second entry: ")
third = raw_input("Third entry: ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
