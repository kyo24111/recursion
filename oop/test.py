def rotateByTimes(ids,n):
    tmp = ""
    ans_ids = ids
    for i in range(n):
        tmp = ans_ids[-1]
        ans_ids = ans_ids[:-1]
        ans_ids.insert(0,tmp)
        print("now, i is = " + str(i))
        print(ans_ids)
    return ans_ids

print(rotateByTimes([642,790,37,233,494,263,698,534,977,931,920,782,225,178,730],349))
[3,4,5,10,12]

arr = [3,4,2,6,1]
arr1 = arr[:-1]
arr1.insert(0,5)
print(arr1)


