
#This iterates five times printing athe string on each iteration
for x in range(5):
    print "am learning the for loops"


"""
==================
enumerate function
==================
It works by supplying a corresponding index to each element in the element that you pass it

"""

l = ["james", "john", "cate", "dan"] #declare a variable list

for index, item in enumerate(l):
    print index+1 + " " + item  #Loops and prints index number from 1 and item in the list

"""
==================
zip function
==================
zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.

"""

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

#for loop that uses zip function to print he greater element
#It helps compare two elements in both lists
#The loop stops at smallest list
print "Zip function to compare two lists: \ prints the greater item and stops at the smaller list's last index"
for a, b in zip(list_a, list_b):
    # Add your code here!
    #you may also try using print max(a,b)
    if a > b:
        print a
    else:
        print b
