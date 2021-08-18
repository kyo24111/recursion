#-*- coding: utf-8 -*-
# # 複雑な処理が必要な場合は、やるべき処理を分解してそれぞれ関数を作ります。
# カラオケの料金を計算する関数、学校があるか判定する関数、閏年か判定する関数の3つをつくり、最終的なカラオケ料金を計算する関数getKaraokeFee:の中から呼び出します。

def getKaraokeFee(day, isHoliday, lastDigits, num):
    # カラオケの料金を計算する関数を呼び、その結果を変数priceに代入します。
    price = calculateFee(num)
    # 学校があるか判定する関数を呼びます。falseの時priceは4倍になります。
    if isThereSchool(day, isHoliday) is False: price *= 4
    # 閏年か判定する関数を呼びます。trueなら半額になります。
    if isLeapYear(lastDigits): price //= 2

    print(price)

#　カラオケの料金を計算する関数
def calculateFee(people):
    perPerson = 0

    if people <= 3: perPerson = 8
    elif people < 10: perPerson = 6
    else: perPerson = 5

    return perPerson * people

# 学校があるか判定する関数
def isThereSchool(day, isHoliday):
    if day == "Sunday" or day == "Saturday" or isHoliday: return False
    else: return True

# 閏年かどうか判定する関数
def isLeapYear(year):
    if year % 400 == 0: return True
    elif year % 100 == 0: return False
    elif year % 4 == 0: return True
    return False