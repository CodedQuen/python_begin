def geometricSeriesSum(x,n):
    sum = 0
    i = 0
    while i <= n:
        prod = 1
        j = 0
        while j< i:
            prod *= x
            j += 1
        sum += prod
        i += 1
    return sum

print(geometricSeriesSum(4,10))
