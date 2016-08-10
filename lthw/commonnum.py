l = [1, 2, 3, 4, 5]
l2 = [2, 4, 6]

finallist = []

for x in l:
    for y in l2:
        if x == y:
            finallist.append(x)

print finallist


