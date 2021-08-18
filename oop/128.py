def g(i):
    return i
 
def summationOfi(a, b):
    if b < a:
        return 1

    return g(b) * summationOfi(a, b-1)

print(summationOfi(3,5))