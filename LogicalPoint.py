
class LogicalPoint:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "({0},{1})".format(self.__x, self.__y)

    def setPoints(self,x, y):
        self.__x = x
        self.__y = y

    def setX(self, x):
        self.__x = x



    def shiftOXRight(self, shift):
        self.__x += shift

    def shiftOXLeft(self, shift):
        self.__x -= shift

    def shiftOYUp(self, shift):
        self.__y -= shift

    def shiftOYDn(self, shift):
        self.__y += shift

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
