def generateAlphabet(firstAlphabet,secondAlphabet):
    char_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # lowercase
    n_first = str(firstAlphabet).lower()
    n_second = str(secondAlphabet).lower()
    print("n_first = " + n_first + " , n_second = " + n_second )
    print(ord(n_first))
    start_point = 0
    end_point = 0
    if ord(n_first) <= ord(n_second):
        start_point = char_list.index(n_first)
        end_point = char_list.index(n_second)
        print("start = " + str(start_point))
        print("end = " + str(end_point))
    else:
        start_point = char_list.index(n_second)
        end_point = char_list.index(n_first)
    return char_list[start_point:end_point+1]

print(generateAlphabet("A","D"))
