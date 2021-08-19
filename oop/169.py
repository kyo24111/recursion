def x(count):
    return y(count,"")
def y(count,string):
    if <= 0:return string
    return y(count-1, str(count) + "sheep ~" + string)