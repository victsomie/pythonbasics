#!/usr/bin/python

#Create a dictionary
my_dict = {"name": "Victor",
           "institution": "moringa school",
           "cohort":"5"
          }

#Print the dictionary before manipulatinng it
print "******Dictionary at first******* "
print my_dict
print

#iterate through the dictionary looking
for i in my_dict:
    if my_dict[i] == "moringa school":
        my_dict[i] = "school"


#Print the dictionary after manipulating it
print "******Dictionary after manipulation******* "
print my_dict

#A function that allows to take in extra arguments
def data(a,b,c,*x):
    print "First item is: " +a
    print "Second item is: " +b
    print "Third item is: " +c
    print x
    print
    count = 0

    #Iterate all the extra elements printing them
    for i in x:
        count+= 1
        print "Item ",
        print count,
        print " in the extra is: "+i

#Call the function with extra arguments
data("John", "Jack",  "Germain", "The first extra!!!!", "Another extra element!!!", "Even more elements!!")
