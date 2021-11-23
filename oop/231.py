def cubeRange(a, b):
    cubeList = []
    for i in range(a, b + 1):
        cubeList.append(i ** 3)
    return cubeList

def printList(arr):
    for i in range(len(arr)):
        print(arr[i])

printList(cubeRange(3, 10))

# 例題
# a,bが与えられるので、aからbまでの中で2の倍数を空の動的配列に追加する関数、evenRangeという関数を作成し、printListによって出力してください。
def evenRange(a,b):
    init_list = []
    for i in range(a,b):
        if i % 2 == 0:
            init_list.append = i

printList(init_list)