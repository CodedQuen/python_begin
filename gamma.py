import math
def gamma():
    result = 0
    i = 1
    while i <= 500000:
        result += 1/i - math.log((i + 1)/i)
        i += 1
    return result

print(gamma())
