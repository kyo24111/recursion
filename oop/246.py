# def rotateByTimes(ids,n):
#     # 関数を完成させてください
#     amountOfRooms = len(ids) #5
#     final_arr = []
#     for i in ids: #10,12,3,4,5
#         originIndex = ids.index(i) #0,1,2,3,4,
#         if originIndex + n < amountOfRooms: #繰り上がりなし
            
def rotateByTimes(ids,n):
    tmp = ""
    ans_ids = ids
    for i in range(n-1):
        tmp = ids[-1]
        ans_ids = ans_ids[:-1]
        ans_ids.insert(0,tmp)
        
# rotateByTimes([10,12,3,4,5],3) --> [3,4,5,10,12]



