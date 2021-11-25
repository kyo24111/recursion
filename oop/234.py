def charInBagOfWordsCount(bagOfWords,keyCharacter):
    # ここから書きましょう
    sum = 0
    for i in bagOfWords[::1]:
        for j in i[::1]:
            if j == keyCharacter: sum += 1
    return sum

charInBagOfWordsCount(["abgd","dgd","egd"], "a")