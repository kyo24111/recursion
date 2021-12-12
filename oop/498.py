# Pythonで開発しましょう。
def printDuplicates(inputList):
    hashmap = {}

    for i in range(len(inputList)):
        hashmap[str(inputList[i])] = 1 if str(inputList[i]) not in hashmap else hashmap[str(inputList[i])] + 1
    keys = list(hashmap.keys())
    print(keys)
    print(hashmap)

    # dictionary.items()を利用して、キーと値の両方を手に入れます。items()の戻り値はtupleの配列です.[[key, value], [key, value], [key,value]......]
    for (key, value) in hashmap.items():
        print(key + " has " + str(value) + " duplicates.")

printDuplicates([1,1,1,1,1,2,2,2,2,2,2,3,3,3,4,5,6,6,6,6,7,8,8,8,9,9,9])
printDuplicates([7,7,6,6,3,5,3,9,2,5,5,4,6,4,1,4,1,7,2])