def num(x):
    if x%3 == 0 and x%5 ==0:
        print "FIZZBUZZ!"
    elif x%3 ==0 and x%5!=0:
        print "FIZZ"
    elif x%3!=0 and x%5==0:
        print "BUZZ"



num(int(raw_input("Enter number: ")))
