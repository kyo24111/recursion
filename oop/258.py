import math
def shuffleSuccessRate(arr,shuffledArr):
    # 関数を完成させてください
    matchCount = 0
    for i in range(len(arr)):
        if arrCheck(arr,shuffledArr)[i] == arrInvert(arr)[i]: matchCount += 1
    return math.floor((len(arr) - matchCount)/len(arr)*100)


def arrCheck(arr,shuffledArr):
    output = []
    for i in arr:
        for j in shuffledArr:
            if not i == j:continue
            if i == j:
                output.append(shuffledArr.index(j))
            break
    return output

def arrInvert(arr):

    return list(range(len(arr)))

print(shuffleSuccessRate([1,2,3],[3,2,1]))