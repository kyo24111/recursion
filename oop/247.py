def websitePagination(urls,pageSize,page):
    # 関数を完成させてください
    pageIndex = pageSize*(page-1)
    outputArr = []
    for i in range(pageSize):
        print("i = " + str(i))
        outputArr.append(urls[pageIndex+i])
        if pageIndex+i == len(urls)-1:break
    return outputArr



print(websitePagination(["url1","url2","url3","url4","url5","url6"],4,1))
# [url1,url2,url3,url4]

print(websitePagination(["url1","url2","url3","url4","url5","url6","url7","url8","url9"],3,2))
# [url4,url5,url6]

print(websitePagination(["url1","url2","url3","url4","url5","url6","url7","url8","url9"],4,3))