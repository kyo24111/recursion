def makeHashmap(x):
    hashmap = {}
    for i in range(x):
        hashmap[i] = "Num" + str(i)
    return hashmap

print(makeHashmap(3))