import math

def getShapeType(ax, ay, bx, by, cx, cy, dx, dy):
    #dot
    pointA = Point(ax, ay)
    pointB = Point(bx, by)
    pointC = Point(cx, cy)
    pointD = Point(dx, dy)

    #line
    lineAB = Line(pointA, pointB)
    lineBC = Line(pointB, pointC)
    lineCD = Line(pointC, pointD)
    lineDA = Line(pointD, pointA)

    #conection
    connectedABC = TwoConnectedLines(lineAB, lineBC)
    connectedBCD = TwoConnectedLines(lineBC, lineCD)
    connectedCDA = TwoConnectedLines(lineCD, lineDA)
    connectedDAB = TwoConnectedLines(lineDA, lineAB)

    errorMsg = "not a quadrilateral"

    #located same point → false
    if (pointA.x == pointB.x and pointA.y == pointB.y) or (pointA.x == pointC.x and pointA.y == pointC.y) or (pointA.x == pointD.x and pointA.y == pointD.y) or (pointB.x == pointC.x and pointB.y == pointC.y) or (pointB.x == pointD.x and pointB.y == pointD.y) or (pointC.x == pointD.x and pointC.y == pointD.y):
        return errorMsg

    #rhombus
    tmp_rhombus = lineAB.length()
    if tmp_rhombus == lineBC.length() and tmp_rhombus == lineCD.length() and tmp_rhombus == lineDA.length():
        return "rhombus"
    #parallelogram
    if lineAB.length() == lineCD.length() and lineBC.length() == lineDA.length():
        return "parallelogram"
    
    #trapezoid

    #kite

    #other

#class about point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#class aobut line
class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

    def vectorX(self):
        return self.endPoint.x - self.startPoint.x
    def vectorY(self):
        return self.endPoint.y - self.startPoint.y

    def length(self):
        return math.sqrt(self.vectorX() ** 2 + self.vectorY() ** 2)

#class about combined line
class TwoConnectedLines:
    def __init__(self, firstLine, secondLine):
        self.firstLine = firstLine
        self.secondLint = secondLine
    
    #innur product
    def innerProduct(self):
        return 
    
    #angle
    def degangle(self):




    
