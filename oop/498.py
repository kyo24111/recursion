# # Pythonで開発しましょう。
# def printDuplicates(inputList):
#     hashmap = {}

#     for i in range(len(inputList)):
#         hashmap[str(inputList[i])] = 1 if str(inputList[i]) not in hashmap else hashmap[str(inputList[i])] + 1
#     keys = list(hashmap.keys())
#     print(keys)
#     print(hashmap)

#     # dictionary.items()を利用して、キーと値の両方を手に入れます。items()の戻り値はtupleの配列です.[[key, value], [key, value], [key,value]......]
#     for (key, value) in hashmap.items():
#         print(key + " has " + str(value) + " duplicates.")

# printDuplicates([1,1,1,1,1,2,2,2,2,2,2,3,3,3,4,5,6,6,6,6,7,8,8,8,9,9,9])
# printDuplicates([7,7,6,6,3,5,3,9,2,5,5,4,6,4,1,4,1,7,2])

# # 例題1
# # アルファベットで構成される文字列が与えられるのでそれがパングラムかどうか判定する、isPangramという関数を作成してください。
# # パングラムとは、a-zまでの全てのアルファベットを含んだ文字列のことを指します。
# def isPangram(string):
#     hashmap = {}
#     for char in string.replace(" ", "").lower():
#         if char not in hashmap: hashmap[char] = 1
#         else: hashmap[char] += 1
#         return True if len(hashmap) == 26 else False

# # 例題2
# # 文字列stringが与えられるので、全ての文字が同じ数だけ含まれているかどうか判定するfindXTimesという関数を作成してください。
# def findXTimes(string):
#     hashmap = {}
#     for char in string:
#         if char not in hashmap:hashmap[char] = 1
#         else: hashmap[char] += 1
#     checkHashmap(hashmap)

# def checkHashmap(hashmap):
#     checker = set(list(hashmap.value))
#     return True if len(checker) == 1 else False

def findXTimes(string):
    hashmap = {}
    for char in string:
        if char not in hashmap: hashmap[char] = 1
        hashmap[char] += 1

    count = 0
    initial = hashmap[string[0]]

    for key, value in hashmap.items():
        if value == initial: count += 1
    print(hashmap)
    print(initial)
    print(count)
    return True if count == len(hashmap) else False

findXTimes("babacddc")