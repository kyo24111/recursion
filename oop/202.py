def isPalindromeInteger(n):
    n_a = str(n)
    for i in range (len(n_a)//2):
        if n_a[i] != n_a[-i+1]:
            print("false")
            return False
    print("true")
    print(len(n_a))
    return True

isPalindromeInteger(11411)x
