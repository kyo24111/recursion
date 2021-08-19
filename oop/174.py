def divisor(number):
    #ここから書きましょう
    return helper(number, number, "")

def helper(n, count, str):
    if count == 1 return str
    


#必要な情報を先に整理しましょう。約数を求めるということは、28を例に上げると、28/28, .... 28/14, ... 28/7,... 28/4 .... 28/2, 28/1 
# のように計算していかなければいけません。つまり、この場合28は固定で分母に違う数字を入れていく必要があります。これをcountとしましょう。次に
# 計算した値を文字列として保存して行く必要があるため、文字列も必要になります。これをstringとします。


function divisor(number) {
  return divisorHelper(number, number+1, "-")
}

function divisorHelper(number, count, string) {
  if (number /1 <1) {
    return count;
  }  else {
    return divisorHelper(count, string+count, number/number);
  }
}
console.log(divisor(28))