def missingItems(listA,listB):
    # 関数を完成させてください
    hashmap = {}
    for b in range(len(listB)):
        hashmap[b] = listB[b] # make a hashmap
    print(hashmap)
    output = []
    for a in listA:
        if a not in hashmap.values(): output.append(a)
    return output if not len(output) == 0 else listA


print(missingItems([7,65,9,8,650,482,5],[482,6]))





