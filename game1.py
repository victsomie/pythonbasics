#!/usr/bin/python

#A simple game to combine different function


from random import randint #Imports the randint
print randint(0,5)


def jump():
    times = []
    count = 0
    for i in range(0,5):
        ran  = randint(0,5)
        j = int(raw_input("Enter a number 0 - 4 here: "))
        if ran == j:
            times.append("YAY!")
        else:
            times.append("OOPS")
    print times

jump()

