def sumOfAllPrimes(n):
    sum = 0
    for k in range(n+1):
        if prime_judge(k) == True:
            sum += k
    print(sum)
    return sum

def prime_judge(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True

sumOfAllPrimes(100)