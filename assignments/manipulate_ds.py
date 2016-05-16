#!/usr/bin/python

#Create a dictionary
my_dict = {"name": "Victor",
           "institution": "moringa school",
           "cohort":"5"
          }
#iterate through the dictionary looking
print "******Dictionary at first******* "
print my_dict
print

for i in my_dict:
    if my_dict[i] == "moringa school":
        my_dict[i] = "school"


print "******Dictionary after manipulation******* "
print my_dict

"""
name = raw_input("Who are you ?")
age = int(raw_input("How old are you"))
elizabeth = {
    "name" : "moringa",
    "age": 20,
    "height": 57,
    "weight": "181lbs"

}
"""

def data(a,b,c,*x):
    print "First item is: " +a
    print "Second item is: " +b
    print "Third item is: " +c
    print x
    print
    count = 0
    for i in x:
        count+= 1
        print "Item ",
        print count,
        print " in the extra is: "+i


data("John", "Jack",  "Germain", "The extra this!!!!", "another", )
