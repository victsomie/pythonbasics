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
print ("=" *4) + "print counties abbereviation" + ("=" *4 )
for c in counties:
    print counties[c]
print


