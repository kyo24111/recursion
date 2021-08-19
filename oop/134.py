def reduceByFive(number):
    return reduceByFiveHelper(number, number, False)

def reduceByFiveHelper(number, curr, flag):
    if number == curr and flag:
        print(curr)
        return ""

    if curr < 0 or flag:
        print(curr)
        return reduceByFiveHelper(number, curr + 5, True)
    
    print(curr)
    return reduceByFiveHelper(number, curr - 5, flag)