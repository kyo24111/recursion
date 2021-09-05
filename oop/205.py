def decimalToHexadecimal(decNumber):
    output = ""
    while decNumber >= 16:
        rem = decNumber % 16
        decNumber //= 16
        print("dec:" + str(decNumber))
        output += str(rem)
    output += str(decNumber)
    print(output)
    output_tmp = list(output)
    output_tmp.reverse()
    final_output = "".join(output_tmp)
    return final_output

decimalToHexadecimal(256)
