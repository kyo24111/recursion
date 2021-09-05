def decimalToHexadecimal(decNumber):
    output = ""
    while decNumber >= 16:
        rem = decNumber % 16
        rem = str(rem)
        convert_16(rem)
        decNumber //= 16
        print("dec:" + str(decNumber))
        output += rem
    convert_16(decNumber)
    output += str(decNumber)
    print(output)
    output_tmp = list(output)
    output_tmp.reverse()
    final_output = "".join(output_tmp)
    return final_output

def convert_16(n):
    if n == "10":
        n = "A"
    elif n == "11":
        n = "B"
    elif n == "12":
        n = "C"
    elif n == "13":
        n = "D"
    elif n == "14":
        n = "E"
    elif n == "15":
        n = "F"
    return n

decimalToHexadecimal(255)
