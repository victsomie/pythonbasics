#!/usr/bin/python

"""
Remember to add a parameter when you are going to run this program

open(filename)
open(filename, 'w') #Opens for writting
open(filename, 'r') #opens for reading
open(filename, 'a') #opens for appending

"""

from sys import argv

script, filename = argv
txt = open(filename) #Declares a variable that opens the file and the parameterized file name

print "Here's your file %r:" % filename #This gets the file name and print its out
print txt.read() #This prints out the txt variable, which was the file given
txt.close()


print "Type the filename again:"
file_again = raw_input("> ") #Prompts the user for any file name

txt_again = open(file_again, 'a') #Creates a variable that open that file given as a parameter it declares the file writeable too

#print txt_again.read() #Prints  the filename that has been requested through parameter

print "Write three things to write to file here: "
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "I'm going to write these to the file."
txt_again.write(line1)# this write to the file
txt_again.write("\n")#This will help skip to the next line
txt_again.write(line2)
txt_again.write("\n")
txt_again.write(line3)
txt_again.write("\n")

txt_again = open(file_again, 'r')
print txt_again.read()

txt_again.close()  #This closes the file that has been opened

print "******** %r" % filename
