def twosComplement(bits):
    twosComplement = onesComplement(bits)
    carryOut = False

    for i in reversed(range(0, len(twosComplement))):
        if twosComplement[i] == '0':
            twosComplement = twosComplement[:i] + '1' + twosComplement[i + 1:]
            carryOut = False
            break

        elif twosComplement[i] == '1':
            twosComplement = twosComplement[:i] + '0' + twosComplement[i + 1:]
            carryOut = True

    return '1' + twosComplement if carryOut else twosComplement

def onesComplement(bits):
    onesComplement = ''
    for bit in bits:
        if bit == '1':
            onesComplement += '0'
        else:
            onesComplement += '1'
    return onesComplement

print(twosComplement("00011100"))
print(twosComplement("10010"))
print(twosComplement("001001"))
print(twosComplement("0111010"))
print(twosComplement("1"))