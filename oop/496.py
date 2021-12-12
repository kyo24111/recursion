# TODO: リストと値を受け取り、リスト内にある値のインデックスを返す、searchListという関数をハッシュマップを使って作成してください。
# 値がリスト内に複数ある場合は先に出てきたインデックスを返してください。もし発見されない場合は-1を返してください。

# def searchList(list, n):
#     hashmap = {}
#     for i in range(len(list)):
#         hashmap[i] = list[i]
#         if list[i] == n:
#             return i
#     return -1

# print(searchList([1,4,3,5,7,3,6], 8))



def searchList(givenList, value):
    hashMap = {}

    for i in range(len(givenList)):
        if hashMap.get(givenList[i]) is not None: continue
        hashMap[givenList[i]] = i
    print(hashMap)

    return -1 if hashMap.get(value) == None else hashMap.get(value)

sampleList = [3,10,23,3,4,50,2,3,4,18,6,1,-2]

# 2
print(searchList(sampleList,23))

# 12
# print(searchList(sampleList,-2))

# # -1
# print(searchList(sampleList,100))