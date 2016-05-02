"""
Program fto create a dictionary and how to access the key and
key value separately
=================================
"""
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print "%s %s" %(key, d[key]) #Prints the key and the key value on each iteration

"""
============================
"""


#Complex dictionary

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'],
    'pocket': ["seashell","strange berry", "lint"]
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']=550


print inventory
