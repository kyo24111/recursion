def fizzBuzz(x):
    fizzBuzzList = []
    for i in range(1,x):
        if i % 3 == 0 and i % 5 == 0:
            fizzBuzzList.append("fizzBuzz")
        elif i % 3 == 0:
            fizzBuzzList.append("fizz")
        elif i % 5 == 0:
            fizzBuzzList.append("buzz")
        else:
            fizzBuzzList.append("-" + str(i) + "-")
    return fizzBuzzList

def printList(arr):
    for i in range(len(arr)):
        print(arr[i])

printList(fizzBuzz(45))

# 例題
# 自然数nが与えられるので、1からnまでに含まれる素数を空の動的配列に追加する、primeNumberを作成し、printListで出力してください。