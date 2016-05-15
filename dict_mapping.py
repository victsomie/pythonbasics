#!/usr/bin/python
# program to map elements/items in two dictionaries


#create two dictionaries
counties = {"nairobi": "nrb", 
            "mombasa": "msa", 
            "embu": "emb", 
            "meru":"mru"
           }

towns = {"nrb": "cbd", 
         "msa": "likoni", 
         "emb": "siakago", 
         "mru": "nkubu"
        }

#do queries repectively here
#Prints key in a dictionary (COUNTY'S NAMES)
print ("=" *4) + "print counties" + ("=" *4 )
for c in counties:
    print c
print

#prints items in the key (COUNTIES ABBREVIATION)
print ("=" *4) + "print counties abbreviation" + ("=" *4 )
for c in counties:
    print counties[c]  #Uses key to access element of that key
print


#Print keys in a dict(COUNTY ABBREVIATION- Keys in a towns dictionary)
print ("=" *4) + "print counties abbreviation [KEYS IN TOWN DICT]" + ("=" *4 )
for key in towns:
    print key
print

#Use items in a dictionary using their key
print ("=" *4) + "print names of towns in each city [KEYS IN TOWN DICT]" + ("=" *4 )
for key in towns:
    print towns[key]
print

#map items in keys of one dict as keys of another
#"key values" in counties is "key" in to
print ("=" *4) + "NB: TOWNS AGAIN using key values from counties" + ("=" *4 )
for key in counties:
    print towns[counties[key]] + " is town in "  + key
print

#simplify the for loop
print ("=" *4) + "NEW WAY TO DO FOR LOOP: for x, y in dictionary " + ("=" *4 )
for key, item in counties.items():
    print key + " abbreviates as " +  item
print

#Try to get items from a dict in a new way
print ("=" *4) + "a different way to access key values" + ("=" *4 )
county = counties.get("mer")
if not county:
    print "Sorry: doesn't exist"
elif county == "mru":
    print "You are in MERU"    
else:
    print county
    
x = counties.get(raw_input("Enter a search: "))
if not x:
    print "pUUUF not found"
else:
    print x

    
    