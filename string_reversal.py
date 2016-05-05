"""A function to reverse a string"""
def  reverse(text):
    s = ""
    for x in range(0, len(text)):
        s = text[x] + s
    return s
