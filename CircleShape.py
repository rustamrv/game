from LogicalPoint import *

class CircleShape(LogicalPoint):

    def __init__(self, x, y, r, color):
        super().__init__(x, y)
        self.radius = r
        self.color = color

    def draw(self, p, window):
        p.draw.circle(window, self.color, (self.getX(), self.getY()), self.radius)
