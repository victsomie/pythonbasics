#!/usr/bin/python

"""
Remember to add a parameter when you are going to run this program
"""

from sys import argv

script, filename = argv
txt = open(filename) #Declares a variable that opens the file and the parameterized file name

print "Here's your file %r:" % filename #This gets the file name and print its out
print txt.read() #This prints out the txt variable, which was the file given
txt.close()


print "Type the filename again:"
file_again = raw_input("> ") #Prompts the user for any file name

txt_again = open(file_again) #Creates a variable that open that file given as a parameter
txt_again.close()  #This closes the file that has been opened

print txt_again.read() #Prints  the filename that has been requested through parameter



print "******** %r" % filename
