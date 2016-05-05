"""A function to reverse a string"""
def  reverse(text):
    s = ""
    #Loop over the list writting characters inside
    for x in range(0, len(text)):
        s = text[x] + s #Add to the character behind the string
    return s #Returns the string created
