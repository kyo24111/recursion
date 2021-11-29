def subscriberListCheck(emailList):
    arr = []
    for email in emailList:
        if isValidEmail(email): arr.append(email) 
    return arr

def isValidEmail(email):
    firstAtIndex = email.find("@")
    addressAfterAt = email[firstAtIndex + 1:len(email)]
    return True if email.find(" ") == -1 and addressAfterAt.find("@") == -1 and addressAfterAt.find(".") != -1 else False