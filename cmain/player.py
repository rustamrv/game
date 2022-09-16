from logicalRect import *


class Player:
    """
    class Player
    """
    def __init__(self, x, y, height, width, color, side):
        """
        :param x: point x
        :param y: point y
        :param height: player height
        :param width: player width
        :param color: player color
        :param side:
        """
        self.__height = height
        self.__width = width
        self.__health = 100
        self.__color = color
        self.__side = side
        self.__shape = LogicalRect(x, y, height, width, color)

    def setColor(self, color):
        """
        set color
        :param color: accepts player color
        """
        self.__color = color

    def getColor(self):
        """ :return: color  """
        return self.__color

    def getHealth(self):
        """ :return: health """
        return self.__health

    def setHealth(self, health):
        """
        set health
        :param health: accepts player health
        """
        self.__health = health

    def wound(self, wound):
        """
        wounded player
        :param wound: number of wounds
        """
        self.__health -= wound

    def isDead(self):
        """
        check is dead
        :return: true if player dead
        """
        return self.getHealth() < 0

    def setSide(self, side):
        if side is not None:
            self.__side = side

    def getSide(self):
        return self.__side

    def getShape(self):
        """
        :return: shape
        """
        return self.__shape

    def draw(self, p, w):
        """
        draw player
        :param p: pygame
        :param w: window
        """
        self.__shape.draw(p, w)
