def winnerBlackjack(playerCards,houseCards):
    # ここから書きましょう
    sum = 0
    print("player" + str(inverter(playerCards)))
    print("house:" + str(inverter(houseCards)))
    if inverter(playerCards) > 21:
        return False
    elif inverter(houseCards) < 22 and inverter(playerCards) < inverter(houseCards):
        return False
    elif inverter(playerCards) == inverter(houseCards):
        return False
    else:
        return True

    

def inverter(arr):
    count = 0
    number = 0
    for i in arr[::1]:
        if i[1] == "A":
            number = 1
        elif i[1] == "J":
            number = 11
        elif i[1] == "Q":
            number = 12
        elif i [1] == "K":
            number = 13
        elif len(i) == 3:
            number = 10
        else:
            number = int(i[1])
        count += number
    return count



winnerBlackjack(["♥10","♥6","♣K"],["♠Q","♦2","♥K"])
