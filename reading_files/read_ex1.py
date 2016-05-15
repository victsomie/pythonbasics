#!/usr/bin/python

"""
Remember to add a parameter when you are going to run this program
"""

from sys import argv

script, filename = argv
txt = open(filename) #Declares a variable that opens the file and the parameterized file name

print "Here's your file %r:" % filename #This gets the file name and print its out
print txt.read() #This prints out the txt variable, which was the file given
