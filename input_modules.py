#!/usr/bin/python
"""
Take whatever is in argv, unpack it, and assign it to all these variables on the left in order.
"""

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
