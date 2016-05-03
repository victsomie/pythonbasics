
#This iterates five times printing athe string on each iteration
for x in range(5):
    print "am learning the for loops"


"""
enumerate function
==================
"""
l = ["james", "john", "cate", "dan"] #declare a variable list

for index, item in enumerate(l):
    print index+1 + " " + item  #Loops and prints index number from 1 and item in the list
