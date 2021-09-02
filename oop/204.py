def decimalToBinary(decNumber):
    output = ""
    rem = 0
    while decNumber > 1:
        rem = decNumber % 2
        # print("rem:"+str(rem))
        output += str(rem)
        decNumber //= 2
        # print("new_dec:"+str(decNumber))
        # print("output:"+str(output))
    output += "1"
    # print("final_output:"+str(output))
    new_output = list(output)
    new_output.reverse()
    str_output = "".join(new_output)
    # print(type(str_output))
    # print(str_output)
    return new_output

decimalToBinary(1)