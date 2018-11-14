from LogicalPoint import *

class Player(LogicalPoint):

    def __init__(self, x, y, height, width, color, isCreate, side):
        super().__init__(x, y)
        self.__height = height
        self.__width = width
        self.__health = 100
        self.__color = color
        self.__isCreate = isCreate
        self.__side = side

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

    def getCreate(self):
        return self.__isCreate

    def setCreate(self, isCreate):
        self.__isCreate = isCreate

    def setSide(self, side):
        if side is not None:
            self.__side = side

    def getSide(self):
        return self.__side

    def draw(self, p, w):
        p.draw.rect(w, self.getColor(), (self.getX(), self.getY(), self.getHeight(), self.getWidth()))


