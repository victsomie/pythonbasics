my_list = [1, 2, 3 "victor", 4.5]

print my_list[0]  #prints the first item in the list
print append ("James") # This adds James to the end of the list
print len(my_list)   #Prints the length of the list
print my_list[0:4]  #Prints index 0 up to but excluding index 4
print my_list[0:len(my_list)] #Prints index 0 up to but excluding the last item
print my_list[0:]  #This prints from the first to the last item
my_list.insert(1, "dog") #This inserts content to the the specified index(in this case it insert dog to the index 1)


# For loop

list_2 = [ 1, 4, 5]
for number in list_2:
    print number

#Another for Loop
start_list = [5, 3, 1, 2, 4]
square_list = []


# Your code here!
for number in start_list:
    square_list.append(number**2)

square_list.sort()



animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]              # The fourth through sixth characters
frog = animals[6:]              # From the seventh character to the end


# DICTIONARIES
# Declare a new dictionary
my_dict ={"donkey":1, "cow": 5, "goat": 52}
empty_dict = {}  # Declares an empty dictionary
empty_dict["zebra"] = 100 #Adds a new key-pair value the empty array
dict_name[new_key] = new_value


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


