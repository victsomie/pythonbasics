my_list = [1, 2, 3 "victor", 4.5]

print my_list[0]  #prints the first item in the list
print append ("James") # This adds James to the end of the list
print len(my_list)   #Prints the length of the list
print my_list[0:4]  #Prints index 0 up to but excluding index 4
print my_list[0:len(my_list)] #Prints index 0 up to but excluding the last item
print my_list[0:]  #This prints from the first to the last item
my_list.insert(1, "dog") #This inserts content to the the specified index(in this case it insert dog to the index 1)



animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]              # The fourth through sixth characters
frog = animals[6:]              # From the seventh character to the end
