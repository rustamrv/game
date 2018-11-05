from LogicalPoint import *

class LogicalRect(LogicalPoint):

    __height = 0
    __width = 0

    def __init__(self, x, y, height, width, color):
        super().__init__(x,y)
        self.__height = height
        self.__width = width
        self.__color = color


    def setHeight(self, height):
        if height>=0:
           self.__height = height

    def setWidht(self, width):
        if width >= 0:
           self.__width = width

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def getHeight(self):
        return self.__height

    def getColor(self):
        return self.__color

    def getWidth(self):
        return self.__width

    def draw(self,p,w):
        p.draw.rect(w, self.getColor(), (self.getX(), self.getY(), self.getHeight(), self.getWidth()))

