# def twosComplement(bits):

def twosComplement(bits):
    str_num = list(oneComplement(bits))
    for i in range (len(str_num)-1, -1, -1):
        print(i)
        if str_num[i] == "0":
            str_num[i] = "1"
            break
        else:
            str_num[i] = "0"

        if i == 0 and str_num[0] == "0":
            reach_final = True
        else:
            reach_final = False
        if reach_final == True:
            str_num.insert(0,'1')
    answer = "".join(str_num)
    return answer

def oneComplement(num):
    bits_list = list(str(num))
    for i in range(0,len(bits_list)):
        if bits_list[i] == "0":
            bits_list[i] = "1"
        else:
            bits_list[i] = "0"
    final_output = "".join(bits_list)
    print(final_output)
    return final_output

twosComplement(111)
