import math
def sumPrimeUpToN(n):
    cache = [True] * n
    for p in range(2,math.ceil(math.sqrt(n))):
        if not cache[p] : continue
        i = 2
        ip = i * p
        while ip < n:
            cache[ip] = False
            i += 1
            ip = i * p
    
    count = 0
    for index, predicate in enumerate(cache):
        if predicate: count += index
    return count-1

# 53 -> 381
# 89 -> 963
# 97 -> 1060
print(sumPrimeUpToN(53))
print(sumPrimeUpToN(89))
print(sumPrimeUpToN(97))
