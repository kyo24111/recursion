import math

def recursiveDigitsAdded(digits):
    return Helper(digits, 0)

def Helper(digits,lastNumber):
    x = splitAndAdd(digits,0)
    lastNumber += x
    if x < 10:
        return lastNumber
    else:
        return splitAndAdd(x,lastNumber)

def splitAndAdd(digits, total):
    if digits < 10:
        total += digits
        return total
    else:
        return splitAndAdd(math.floor(digits/10), total + digits%10 )