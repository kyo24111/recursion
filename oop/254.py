def isPangram(string):
    # 関数を完成させてください
    cache = [True] * 26
    for i in string.lower():
        print(ord(i))
        if i == " ":continue
        if not cache[ord(i)-97] :continue
        cache[ord(i)-97] = False
    if set(cache) == {False}:return True
    else: return False

print(isPangram("the Japanese yen for commerce is still well-known"))


