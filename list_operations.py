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
letter = list_x + list_y

print "===Letters after adding content===="
print letter
print


#Nesting lists inside other lists
letter = [list_x, list_y]

print "===Letters as elements===="
print letter
print

print "===Back to print letters===="
print letters
print


#Slicing the list



print "===Letters after slicing from index 2 FORWARDS content===="
print "===Slices from index 2 FORWARDS including the index 2 item===="
print letters[2:]
print

print "===Letters after adding content===="
print "===Slices from index 2 BACKWARDS excluding the index 2 item===="
print letters[:2]
print

print "===Letters after adding content===="
print "===The COLON gives the whole list from first to last===="
print letters[:]
print

