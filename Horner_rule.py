def Horner(a, n, x):
    result = a[n]
    i = n - 1
    while i >= 0:
        result = result * x + a[i]
        i-= 1
    return result
