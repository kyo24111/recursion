import math
import random

class BankAccount:
    maxWidthdrawRate = 0.2

    def __init__(self, bankName, ownerName, savings, interestPerDay):
        self.bankName = bankName
        self.ownerName = ownerName
        self.savings = savings
        self.interestPerDay = interestPerDay
    

    # ユーザーの情報を表示します。
    def showInfo(self):
        return "bank: " + self.bankName + "\nowner name: " + self.ownerName + "\nbank account number: " + str(HelperFunction.getRandomInteger(1, math.pow(10,8)))
    
    # depositAmountによって貯蓄額を増やし、その金額をint型で返します。もし預金前の貯蓄額が$20,000以下の場合は、$100の手数料がかかります。
    def depositMoney(self, depositAmount):
        self.savings += depositAmount - 100 if self.savings <= 20000 else depositAmount
        return int(self.savings)

    # withdrawAmountによって貯蓄額を減らし、withdrawAmountを整数として返します。最大で貯蓄額の20%を引き出すことができます。
    def withdrawMoney(self, withdrawAmount):
        moneyYouCanTake = self.maxWidthdrawRate * self.savings if withdrawAmount > self.maxWidthdrawRate * self.savings else withdrawAmount
        self.savings -= moneyYouCanTake
        return int(moneyYouCanTake)   

    # 毎日interestPerDayによって貯蓄額を増加し、その金額をdouble型で返します。
    def pastime(self, day):
        return self.savings * (1 + self.interestPerDay) ** day

# 計算を行うクラス
class HelperFunction:
    # min-max間のランダムな整数を返します。
    @staticmethod
    def getRandomInteger(min, max):
        return math.floor(random.random() * (max - min)) + min

user1 = BankAccount("Chase", "Claire Simmmons", 30000, 0.010001)

print(user1.showInfo())
print(user1.withdrawMoney(1000))
print(user1.depositMoney(10000))
print(user1.pastime(200))

print("\n")

user2 = BankAccount("Bank Of America", "Remy Clay", 10000, 0.010001)

print(user2.showInfo())
print(user2.withdrawMoney(5000))
print(user2.depositMoney(12000))
print(user2.pastime(500))