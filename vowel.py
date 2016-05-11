#!usr/bin/python
"""
A function that takes a string and removes 
all vowels including the capitalized one
"""
def anti_vowel(text):
    s = ""
    for x in text:
        if x == "a"  or x =="e" or x == "i" or x == "o" or x=="u":
            continue
        else:
            s =s + x
    print s

anti_vowel("Hey look Words!") #Call to function

"""

def anti_vowel(text):
    v = "AEIOUaeiou"
    newStr = ""
    for c in text:
        for ch in v:
            if ch == c:
                continue
            else:
                newStr =newStr + c
    print newStr

"""
