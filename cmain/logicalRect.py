from logicalPoint import *


class LogicalRect(LogicalPoint):

    def __init__(self, x, y, height, width, color):
        """
        :param x: point x rect
        :param y: point y rect
        :param height: height rect
        :param width: width rect
        :param color: color rect
        """
        super().__init__(x, y)
        self.__height = height
        self.__width = width
        self.__color = color

    def setHeight(self, height):
        """
        set height rect
        :param height: accept rect height
        """
        if height >= 0:
            self.__height = height

    def setWidth(self, width):
        """
        set width rect
        :param width: accepts rect width
        """
        if width >= 0:
            self.__width = width

    def getHeight(self):
        """
        :return: height rect
        """
        return self.__height

    def getWidth(self):
        """
        :return: width rect
        """
        return self.__width

    def setColor(self, color):
        """
        set color rect
        :param color: accepts rect color
        """
        self.__color = color

    def getColor(self):
        """
        :return: color rect
        """
        return self.__color

    def draw(self, p, w):
        """
        draw rect
        :param p: pygame
        :param w: window
        """
        p.draw.rect(w, self.getColor(), (self.getX(), self.getY(), self.getHeight(), self.getWidth()))
