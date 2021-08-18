def wholeNumberSubstraction(x,y):
    if y == 0:
        return x
    return wholeNumberSubstraction(x-1,y-1)

print(wholeNumberSubstraction(5,4))
print(wholeNumberSubstraction(10,3))