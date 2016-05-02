def add(num):
    while num<20:
        print num
        num+=1
        if num==17:
            break
    else:  #This doesnt execute if the break statement is reached
        print "Numbers fro here are greater the one given in the condition"

add(10)
