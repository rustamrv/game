from circleShape import *


class Ballet:

    def __init__(self, x, y, height, width, r, color):
        self.__height = height
        self.__width = width
        self.__health = 100
        self.__shape = CircleShape(x, y, r, color)

    def draw(self, p, w):
        self.__shape.draw(p, w)

    def getShape(self):
        return self.__shape

    def setHealth(self, health):
        self.__health = health

    def isDead(self):
        return self.__health < 0
