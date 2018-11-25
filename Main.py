import pygame
from Player import *
from Menu import *
from WorkFile import *
from SQL import *
from LogicalRect import *
from Ballet import *
import logging
import sys

pygame.init()
logging.basicConfig(filename="errors.log", level=logging.DEBUG)
logger = logging.getLogger("exampleApp")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh = logging.FileHandler(filename="errors.log", encoding='utf-8')
fh.setFormatter(formatter)
logger.addHandler(fh)

sh = logging.StreamHandler(stream=sys.stdout)
sh.setFormatter(formatter)
logger.addHandler(sh)

xWind = 800
yWind = 600
window = pygame.display.set_mode([xWind, yWind])

basic = LogicalRect(5, 595, 790, -60, (255, 255, 255))
start = False

Play = Player(5, 525, 20, -10, (0, 128, 0), None)
print(Play.__doc__)

logger.debug("Create player")
Enemy = Player(5, 50, 20, -10, (0, 128, 0), 1)
logger.debug("Create enemy")

BalletPlayer = Ballet(Play.getShape().getX(), Play.getShape().getY(), Play.getShape().getHeight(), Play.getShape().getWidth(), 5, (255, 255, 255))
BalletEnemy = Ballet(Enemy.getShape().getX(), Enemy.getShape().getY(), Enemy.getShape().getHeight(), Enemy.getShape().getWidth(), 5, (255, 255, 255))

File = WorkFile("Menu.json")
startMenu = File.read()
File1 = WorkFile("settings.json")
setMenu = File1.read()

database = 'DRIVER={SQL Server};SERVER=LAPTOP-JGQ8MSK8;DATABASE=DB;UID=Admin;PWD=qwerty12345'
Connect = Sql(database, logger)

stMenu = Menu(startMenu)

stMenu.menu(window)
name = "user"
start = stMenu.position(Connect, window, Play, Enemy, basic, setMenu)

if __name__ == "__main__":
    logger.debug("Start")
    while start:
        pygame.time.delay(10)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            Play.getShape().shiftOXLeft(2)
        elif keys[pygame.K_RIGHT]:
            Play.getShape().shiftOXRight(2)
        elif keys[pygame.K_ESCAPE]:
            stMenu.setList(startMenu)
            stMenu.menu(window)
            stMenu.position(Connect, window, Play, Enemy, basic, setMenu)

        elif keys[pygame.K_SPACE]:
            if not BalletPlayer.isDead():
                BalletPlayer.getShape().setPoints(Play.getShape().getX(), Play.getShape().getY())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False

        length = Enemy.getShape().getX() - Enemy.getShape().getWidth()
        if length >= xWind:
            Enemy.setSide(2)
        elif length <= 0.0:
            Enemy.setSide(1)
        if not Play.isDead():
            if not BalletPlayer.isDead():
                BalletPlayer.getShape().shiftOYUp(10)
                BalletPlayer.draw(pygame, window)
                if Enemy.getShape().getY() >= BalletPlayer.getShape().getY() and Enemy.getShape().getX() <= BalletPlayer.getShape().getX() <= Enemy.getShape().getX() + Enemy.getShape().getHeight():
                    Enemy.wound(1)
                    logger.debug("Player hurt enemy")

        if not Play.isDead():
            Play.draw(pygame, window)
        if not Enemy.isDead():
            Enemy.draw(pygame, window)
            if Enemy.getSide() == 1:
                Enemy.getShape().shiftOXRight(1)
            elif Enemy.getSide() == 2:
                Enemy.getShape().shiftOXLeft(1)

        if not BalletEnemy.isDead():
            BalletEnemy.getShape().shiftOYDn(10)
            BalletEnemy.draw(pygame, window)
            if BalletEnemy.getShape().getY() >= Play.getShape().getY() and Play.getShape().getX() <= BalletEnemy.getShape().getX() <= Play.getShape().getX() + Play.getShape().getHeight():
                Play.wound(1)
                logger.debug("The enemy hurt the player")
            if BalletEnemy.getShape().getY() > yWind:
                BalletEnemy.getShape().setPoints(Enemy.getShape().getX(), Enemy.getShape().getY())

        basic.draw(pygame, window)
        font = pygame.font.Font('12172.ttf', 20)
        rect = pygame.Rect([5, 5, 220, 25])
        if not Play.isDead() and not Enemy.isDead():
            window.blit(font.render(
                "Hello, " + name + "! Health enemy : " + format(Enemy.getHealth()) + " health " + name + ": " + format(
                    Play.getHealth()), 1, (255, 255, 224)), rect.topleft)
        elif Enemy.isDead():
            window.blit(font.render("WIN!", 1, (255, 255, 244)), rect.topleft)
            BalletEnemy.setHealth(-1)
        elif Play.isDead():
            window.blit(font.render("Game over!", 1, (255, 255, 244)), rect.topleft)

        pygame.display.update()
        window.fill(stMenu.background)
