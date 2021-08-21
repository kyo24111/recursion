def divisor(number):
    #ここから書きましょう
    d_list = []
    return helper(number, number, d_list)

#def helper(28, 27, [28]):
def helper(n, count, d_list):
    if count == 1: return count
    for i in range(count,0,-1): # decrement
        if n % i == 0: break
    #for文で割れるところまで回す
    
    return helper(n, i-1, d_list.append(i))



#必要な情報を先に整理しましょう。約数を求めるということは、28を例に上げると、28/28, .... 28/14, ... 28/7,... 28/4 .... 28/2, 28/1 
# のように計算していかなければいけません。つまり、この場合28は固定で分母に違う数字を入れていく必要があります。これをcountとしましょう。次に
# 計算した値を文字列として保存して行く必要があるため、文字列も必要になります。これをstringとします。


# function divisor(number) {
#   return divisorHelper(number, number+1, "-")
# }

# function divisorHelper(number, count, string) {
#   if (number /1 <1) {
#     return count;
#   }  else {
#     return divisorHelper(count, string+count, number/number);
#   }
# }
# console.log(divisor(28))