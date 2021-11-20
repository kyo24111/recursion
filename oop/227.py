def sumArrayElement(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

def maxValue(second_list):
    max = 0
    for i in range(len(second_list)):
        if second_list[i] > max:
            max = second_list[i]
    return max

def countChar(arr):
    count = 0
    for i in range(len(arr)):
        current_S = arr[i]
        for j in range(len(current_S)):
            count += 1
    return count



list_1 = [3,43,5,4,2,100,6]
# print(sumArrayElement(list_1))

list_2 = [3,43,5,4,2,100,6]
# print(maxValue(list_2))

list_3 = ["The wood", "Pecked peckers", "At the inn", "Tomorrowland"]
print(countChar(list_3))
