# Sanchez はメルマガを定期的に配信しています。会員のメールアドレスリスト emailList が与えられるので、正しく利用できるメールアドレスだけを配列として返す validEmailList という関数を定義してください。正しいメールアドレスの条件は以下の通りです。

# - スペースがないこと

# 　
# - 「@」を 1 つのみ含んでいること

# 　
# - 「@」の後に「.」があること

def validEmailList(emailList):
    
    correct_email = []
    for i in emailList[::1]: #各メール
        if email_check == True: correct_email.append(i)
    return corrct_email

def email_check(email):
    count_@ = 0
    for i in range(0,len(email)):
        letter_i = email[i]
        letter_next = email[i+1]
        if letter_i == " ": return False #space
        elif letter_i = "@": count_@ += 1
        


