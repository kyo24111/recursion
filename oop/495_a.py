import math

def allNPrimesSieve(n):
    cache = [True] * n
    for currentPrime in range(2,math.ceil(math.sqrt(n))):
        if not cache[currentPrime]: continue
        i = 2
        ip = i * currentPrime
        while ip < n:
            cache[ip] = False
            i += 1
            ip = i * currentPrime

    primeNumbers = []
    for index, predicate in enumerate(cache):
        if predicate:primeNumbers.append(index)
    return primeNumbers[2:]

allNPrimesSieve(30)
