# def fizzBuzz(x):
#     fizzBuzzList = []
#     for i in range(1,x):
#         if i % 3 == 0 and i % 5 == 0:
#             fizzBuzzList.append("fizzBuzz")
#         elif i % 3 == 0:
#             fizzBuzzList.append("fizz")
#         elif i % 5 == 0:
#             fizzBuzzList.append("buzz")
#         else:
#             fizzBuzzList.append("-" + str(i) + "-")
#     return fizzBuzzList

# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i])

# printList(fizzBuzz(45))

# 例題
# 自然数nが与えられるので、1からnまでに含まれる素数を空の動的配列に追加する、primeNumberを作成し、printListで出力してください。

prime_list = [1]
def prime_number(x):
    print("prime_check")
    for i in range(2,x+1):
        print(i)
        if isPrime(i): prime_list.append(i)
    return prime_list

def isPrime(y):
    for i in range(2, y):
        if y % i == 0: return False
        break


def print_list(arr):
    for i in range(0, len(arr)):
        print(prime_list[i])

print_list(prime_number(10))
