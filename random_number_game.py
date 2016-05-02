#A game to gues three numbers and compete with computer
from random import randint

x  = randint(0, 5)
y = int(raw_input("Enter a number (0 - 5)")) #Note that you have to convert the string input

print x
print y
print
print

if y==x:
    print "Won"
else:
    print "try again"

#x = int(randint(0,5))

