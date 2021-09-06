def isPalindrome(stringInput):
    new_input = stringInput.replace(" ","")
    new_input = new_input.lower()
    for i in range(len(new_input)):
        if new_input[-(i+1)] != new_input[i]:
            return False
        if i == len(new_input)/2:
            return True

print(isPalindrome("kayak"))
