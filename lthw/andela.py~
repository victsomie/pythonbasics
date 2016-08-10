l = [2, 3, 4, 5, 64444]


#create a list to contain all the individual numbers
mylist = []
for i in l:
    mylist = mylist + list(str(i))

#check of the numbers are duplicates and remove them
newlist = [] #New List with removed duplicate

for j in mylist:
    j = int(j)
    if j in newlist:
        newlist.remove(j)
    elif j not in newlist:
        newlist.append(j)


"""
for k in newlist:
    if k no:
            del newlist[k] #newlist.remove(k)
"""


print mylist
print newlist

product = 1;

for i in newlist:
    product = product * i

print product
