def bubble_sort(items):
    """ Implementation of bubble sort """

    for i in range(len(items)):
        for j in range(len(items)-1-i):
            print items[i]
            print items[j]
        
        """
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j] # Swap!
                print "Awesome"
        """
"""

print bubble_sort(x)
print x
print len(x)
print len(x)-1

"""
x = [21, 3, 45, 2]
print "Let me try from scratch"
print x

def sorting(items):
    for y in range(len(items)):
        for z in range(len(items)-1-y):
            print items[z]
            print "This is the item that I want to print %s" %items[z]

sorting(x)
