
def check_perfect(x):
    s = 0
    for i in range(1,x):
        if x % i == 0:
            s += i
    if s == x:
        return True
    else:
        return False

def question(x):
    l = ""
    for k in range(1,x+1):
        if check_perfect(k) == True:
            l = l + str(k) + "-"
    print(l[:-1])
# def f(x):
#     for i in range(1,x+1):
#         print(i)

question(500)
