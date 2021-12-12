def shuffledPositions(arr,shuffledArr):
    # 関数を完成させてください
    output = []
    for i in arr:
        # print("now i = " + str(i))
        for j in shuffledArr: #45,32,2
            # print("now j = " + str(j))
            if not i == j: continue
            if i == j:
                output.append(shuffledArr.index(j)) #iのあるindexを配列に格納
            break
    return output





print(shuffledPositions([1350,181,1714,375,1331,943,735],[1714,1331,735,375,1350,181,943]))
#[4,5,0,3,1,6,2]