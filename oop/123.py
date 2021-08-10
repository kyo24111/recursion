from random import randrange

# 文字の文字コードが奇数か偶数かチェックする1つのタスク
def isCharCodeEven(stringChar):
    isEven = False
    if ord(stringChar[0]) % 2 == 0:
        isEven = True
    return isEven

# 文字のインデックスを把握するための文字列1つのタスク
def chosenCharacter(index, string):
    return "The char [" + string[index] + "] at index " + str(index)

# もっとシンプルで簡潔にまとめることができます。
def randomCharEvenOrOddDecomposed(string1):
    randomIndex = randrange(len(string1))
    message = chosenCharacter(randomIndex,string1)
    return message + " is Even" if isCharCodeEven(string1[randomIndex]) else  message + " is Odd"

print(randomCharEvenOrOddDecomposed("Don't tell me lies."))


# 例題1
# 小文字で構成される文字列を1つ受け取り、文字列内のランダムな文字が母音ならTrue、子音ならFalseを返す、isRandomCharVowelという関数を作成してください。


# 例題2
# 2つの文字列が与えられるので、文字列のランダムな文字の文字コードの合計が偶数ならTrue、奇数ならFalseを返す、isRandomEncodeEvenという関数を作成してください。