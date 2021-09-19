import math

def getShapeType(ax,ay,bx,by,cx,cy,dx,dy):
    #ここから書きましょう
    #点A, B, C, D
    pointA = Point(ax, ay)
    pointB = Point(bx, by)
    pointC = Point(cx, cy)
    pointD = Point(dx, dy)

    #線分AB, BC, CD, DA
    lineAB = Line(pointA, pointB)
    lineBC = Line(pointB, pointC)
    lineCD = Line(pointC, pointD)
    lineDA = Line(pointD, pointA)

    #折れ線ABC, BCD, CDA, DAB
    connectedABC = TwoConnectedLines(lineAB, lineBC)
    connectedBCD = TwoConnectedLines(lineBC, lineCD)
    connectedCDA = TwoConnectedLines(lineCD, lineDA)
    connectedDAB = TwoConnectedLines(lineDA, lineAB)

    errMsg = "not a quadrilateral"

    #同じ座標に位置する点があれば、not a quadrilateralを返す
    if pointA.x == pointB.x and pointA.y == pointB.y: return errMsg
    elif pointA.x == pointC.x and pointA.y == pointC.y: return errMsg
    elif pointA.x == pointD.x and pointA.y == pointD.y: return errMsg
    elif pointB.x == pointC.x and pointB.y == pointC.y: return errMsg
    elif pointB.x == pointD.x and pointB.y == pointD.y: return errMsg
    elif pointC.x == pointD.x and pointC.y == pointD.y: return errMsg

    #3点が一直線上に並ぶ場合：内積の絶対値が2つのベクトルの長さの積と一致 なら、not a quadrilateralを返す
    if math.fabs(connectedABC.innerProduct()) == lineAB.length() * lineBC.length(): return errMsg
    elif math.fabs(connectedBCD.innerProduct()) == lineBC.length() * lineCD.length(): return errMsg
    elif math.fabs(connectedCDA.innerProduct()) == lineCD.length() * lineDA.length(): return errMsg
    elif math.fabs(connectedDAB.innerProduct()) == lineDA.length() * lineAB.length(): return errMsg

    # すべての角度が90度（隣り合う2辺のベクトルの内積が0）かつすべての辺の長さが等しい場合は正方形
    if connectedABC.innerProduct() == 0 and connectedBCD.innerProduct() == 0 and connectedCDA.innerProduct() == 0 and connectedDAB.innerProduct() == 0:
        if lineAB.length() == lineBC.length() and lineBC.length() == lineCD.length() and lineCD.length() == lineDA.length():
            return "square（正方形）"
        #辺の長さが等しくなければ長方形
        else: return "rectangle（長方形）"
    
    #すべての辺の長さが等しければひし形
    if lineAB.length() == lineBC.length() and lineBC.length() == lineCD.length() and lineCD.length() == lineDA.length():
        return "rhombus（ひし形）"
    
    #向かい合う2組の辺の長さがそれぞれ等しければ、平行四辺形
    if lineAB.length() == lineCD.length() and lineBC.length() == lineDA.length():
        return "parallelogram（平行四辺形）"
    
    #1組の向かい合う辺が平行（内積の絶対値が1）であれば台形
    if math.fabs(lineAB.vectorX() * lineCD.vectorX() + lineAB.vectorY() * lineCD.vectorY()) == 1: return "trapezoid（台形）"
    elif math.fabs(lineBC.vectorX() * lineDA.vectorX() + lineBC.vectorY() * lineDA.vectorY()) == 1: return "trapezoid（台形）"
    
    #隣り合う2辺の長さが等しい組が向かい合っている四角形であれば、凧
    if lineAB.length() == lineBC.length() and lineCD.length() == lineDA.length(): return "kite（凧）"
    elif lineDA.length() == lineAB.length() and lineBC.length() == lineCD.length(): return "kite（凧）"

    return "other（その他）"
    


    

#点を表すクラス
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#線分を表すクラス
class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
    
    #ベクトルのX成分
    def vectorX(self):
        return self.endPoint.x - self.startPoint.x

    #ベクトルのY成分    
    def vectorY(self):
        return self.endPoint.y - self.startPoint.y
    
    def length(self):
        return math.sqrt(self.vectorX() ** 2 + self.vectorY() ** 2)

#折れ線を表すクラス
class TwoConnectedLines:
    def __init__(self, firstLine, secondLine):
        self.firstLine = firstLine
        self.secondLine = secondLine

    #内積
    def innerProduct(self):
        return self.firstLine.vectorX() * self.secondLine.vectorX() + self.firstLine.vectorY() * self.secondLine.vectorY()

    #折れ線の角度
    def degAngle(self):
        #ベクトルの内積の式よりcosを算出
        cosAngle = self.innerProduct() / self.firstLine.length() / self.secondLine.length()
        return math.acos(cosAngle) * 180 / math.pi