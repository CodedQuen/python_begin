def findMaximum(a, n):
    result = a[0]
    i = 1
    while i < n:
        if a[i] > result:
            result = a[i]
        i += 1
    return result
