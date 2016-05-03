def digit_sum(n):
    x = str(n)
    sum=0
    for c in range(0, len(x)):
        sum = sum+int(x[c])
    return sum
print digit_sum(1234)
