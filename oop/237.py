# Sanchez はメルマガを定期的に配信しています。会員のメールアドレスリスト emailList が与えられるので、正しく利用できるメールアドレスだけを配列として返す validEmailList という関数を定義してください。正しいメールアドレスの条件は以下の通りです。
# - スペースがないこと
# - 「@」を 1 つのみ含んでいること
# - 「@」の後に「.」があること

def validEmailList(emailList):
    arr = []
    for email in emailList:
        print("now I'm checking this email : " + email)
        if count_alfa(email) == 1 and check_dot(email) == True and no_space(email) == True: arr.append(email)
        arr_str = '-'.join(arr)
        print("now arr is : " + arr_str)
    print(arr)

def count_alfa(string):
    alfa_count = 0
    for letter in string:
        if letter == "@": alfa_count += 1
    print(string + "'s alfa_count is : " + str(alfa_count))
    return alfa_count

def check_dot(string):
    alfa_index = 0
    dummy_count = 0
    for index in range(len(string)):
        print(index)
        if string[index] == "@": alfa_index = index
        else: dummy_count = 0 #これどうすれば
    print("where is @ :" + str(alfa_index))
    back_str = string[alfa_index+1:]
    print("back_str is : " + back_str)
    for j in back_str:
        print("checking dot:" + j)
        if j == ".": return True
    return False

def no_space(string):
    space_count = 0
    for letter in string:
        if letter == " ": space_count += 1
    if space_count == 0:return True
    else: return False


validEmailList(["abc@gmail.com", "kyo24111@gmail.com", "dog@gdl@fl.", "degko@gefw.ef fe"])


