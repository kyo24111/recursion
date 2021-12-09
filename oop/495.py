import math

# エラトステネスのふるいのアルゴリズム
def allNPrimesSieve(n):
    cache = [True] * n
    for currentPrime in range(2, math.ceil(math.sqrt(n))):
        if cache[currentPrime] == False: continue #trueのやつだけみる
        i = 2
        ip = i * currentPrime
        print("ip_1 = " +str(ip))
        while ip < n:
            cache[ip] = False
            print(cache)
            # i*pをアップデートします。
            i += 1
            ip = i * currentPrime
            print("ip_2 = " +str(ip))


    # キャッシュ内のすべてのtrueのインデックスは素数です。
    primeNumbers = []
    # enumerateは現在の位置のペアの値を返します．
    for index, predicate in enumerate(cache):
        if predicate: primeNumbers.append(index)

    return primeNumbers[2:]

print(allNPrimesSieve(10))
# print(len(allNPrimesSieve(20)))
# print(allNPrimesSieve(100))
# print(len(allNPrimesSieve(100)))