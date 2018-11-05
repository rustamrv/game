from LogicalPoint import *

class Player(LogicalPoint):

    def __init__(self, x, y, height, width, color):
        super().__init__(x, y)
        self.__height = height
        self.__width = width
        self.__health = 100
        self.__color = color

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def getHealth(self):
        return self.__health

    def setHealth(self, health):
        self.__health = health

    def wound(self, wound):
        self.__health -= wound


    def draw(self, p, w):
        p.draw.rect(w, self.getColor(), (self.getX(), self.getY(), self.getHeight(), self.getWidth()))


