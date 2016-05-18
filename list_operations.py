#!/usr/bin/python

letters =["a", "b", "c", "d"]
print "===Letters before any operation===="
print letters
print

#Get the length the list
length = len(letters)
print "===Lee=ngth of the list===="
print length
print

#Nesting lists inside lists
list_x = ["x", "y", "z"]
list_y = ["p", "q", "r"]
letters = list_x + list_y

print "===Letters after adding content===="
print letters
print


#Nesting lists inside other lists
letters = [list_x, list_y]

print "===Letters as elements===="
print letters
print
