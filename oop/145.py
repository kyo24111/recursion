# 自然数digitsが与えられるので、桁数を分解して足し合わせる、splitAndAddという関数を末尾再帰を使って作成

import math

def splitAndAdd(digits):
    return splitAndAddHelper(digits, 0)

def splitAndAddHelper(digits, total):
    if digits < 10:
        return digits + total

    return splitAndAddHelper(math.floor(digits / 10), total + digits % 10)

# 10
print(splitAndAdd(19))

# 23
print(splitAndAdd(23387))

# 23
print(splitAndAdd(546125))