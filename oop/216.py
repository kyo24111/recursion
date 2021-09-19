class Point:
    def __init__(self, x, y):
            self.x = x
            self.y = y

class Line:
    def __init__(self, startPoint, endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint

# Lineオブジェクト例
line1 = Line(Point(3,1), Point(3,6))
print(line1.startPoint.x)