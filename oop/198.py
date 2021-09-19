import math

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
        


    
