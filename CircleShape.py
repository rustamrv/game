from LogicalPoint import *

class CircleShape(LogicalPoint):

    def __init__(self, x, y, r, color, isBallet):
        super().__init__(x, y)
        self.radius = r
        self.color = color
        self.__isBallet = isBallet

    def draw(self, p, window):
        p.draw.circle(window, self.color, (self.getX(), self.getY()), self.radius)

    def getIsBallet(self):
        return self.__isBallet

    def setIsBallet(self, isBallet):
        self.__isBallet = isBallet
