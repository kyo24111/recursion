# def twosComplement(bits):

def output(number):
    str_num = list(str(number))
    for i in range (len(str_num)):
        if str_num[i] == "0":
            str_num[i] = "1"
            break
        else:
            str_num[i] = "0"

        if i == len(str_num) -1 and str_num[i] == 0:
            reach_final = True
        else:
            reach_final = False
    if reach_final == True:
        str_num.append('1')

    print(str_num)
    print(reach_final)

output(1111)