class BankAccount:
    def __init__(self, bankName, ownerName, savings, interestPerDay):
        self.bankName = bankName
        self.ownerName = ownerName
        self.savings = savings
        self.interestPerDay = interestPerDay
    
    def showInfo(self):
        return "bank: " + self.bankName + "\nowner name: " + self.ownerName + "\nbank account number: " + str(数)

    def depositMoney(self, depositAmount):
        if self.savings <= 20000:
            self.savings += depositAmount - 100
        else:
            self.savings += depositAmount
        return int(self.savings)
    
    def withdrawMoney(self, withdrawAmount):
        if self.savings <= 


