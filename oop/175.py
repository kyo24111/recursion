def howLongToReachFundGoal(capitalMoney,goalMoney,interest):
    return goalMoneyHelper(capitalMoney,goalMoney,interest,0)


def goalMoneyHelper(capitalMoney,goalMoney,interest,count):
    if (count >= 80):
        return 80

    if (goalMoney > capitalMoney) and ((count % 2)==0):
        return goalMoneyHelper(capitalMoney * (1 + (interest/100)),goalMoney*1.02,interest,count+1)
    elif (goalMoney > capitalMoney) and ((count % 2)!=0):
        return goalMoneyHelper(capitalMoney * (1 + (interest/100)),goalMoney*1.03,interest,count+1)
    elif (capitalMoney >= goalMoney):
        return count