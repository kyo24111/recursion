def oneComplement(bits):
    bits_list = list(bits)
    # print(type(bits_list))
    # print(bits_list)
    # print(len(bits_list))
    for i in range(0,len(bits_list)):
        # print("i =" + bits_list[i])
        if bits_list[i] == "0":
            bits_list[i] = "1"
        else:
            bits_list[i] = "0"
    final_output = "".join(bits_list)
    print(final_output)
    return final_output

oneComplement("01001101011")