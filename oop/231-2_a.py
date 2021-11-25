# 例題
# 自然数nが与えられるので、1からnまでに含まれる素数を空の動的配列に追加する、primeNumberを作成し、printListで出力
def primeNumber(number):
    primeList = []
    for i in range(2, number+1):
        if isPrime(i): primeList.append(i)
    return primeList

def isPrime(n):
    for i in range(2, n):
        if n % i == 0: return False
    return n > 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i])

printList(primeNumber(97))