import pygame as p 
from Player import *
from CircleShape import *
from Menu import *
from WorkFile import *
from SQL import *
import logging
import sys

p.init()
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
window = p.display.set_mode([xWind, yWind])

basic = LogicalRect(5, 595, 790, -60, (255, 255, 255))
start = False

Play = Player(5, 525, 20, -10, (0, 128, 0), True, None)
logger.debug("Create player")
Enemy = Player(5, 50, 20, -10, (0, 128, 0), True, 1)
logger.debug("Create enemy")

Ballet = CircleShape(Play.getX(), Play.getY(), 5, (255, 255, 255), False)
BalletEnemy = CircleShape(Enemy.getX(), Enemy.getY(), 5, (255, 255, 255), True)

File = WorkFile("Menu.json")
startMenu = File.read()
File1 = WorkFile("settings1.json")
setMenu = File1.read()

database = 'DRIVER={SQL Server};SERVER=LAPTOP-JGQ8MSK8;DATABASE=DB;UID=Admin;PWD=qwerty12345'
Connect = Sql(database, logger)

stMenu = Menu(startMenu)

stMenu.menu(window)
name = "user"
if stMenu.point == 0:

    start = Connect.SearchName(name, Play, Enemy, basic)
elif stMenu.point == 1:
    name = stMenu.ask(window, "What is your name?")
    start = Connect.SearchName(name, Play, Enemy, basic)
elif stMenu.point == 2:
    name = stMenu.ask(window, "What is your name?")
    Connect.SaveGame(name, Play, Enemy)
elif stMenu.point == 3:
    Set = Menu(setMenu)
    Set.Setting(window, Play, Enemy, basic)
    if Set.point == 3:
        stMenu = Menu(startMenu)

        stMenu.menu(window)
        if stMenu.point == 0:
            start = Connect.SearchName(name, Play, Enemy, basic)
        elif stMenu.point == 1:
            name = stMenu.ask(window, "What is your name?")
            Connect.SearchName(name, Play, Enemy)
            start = Connect.SearchGame(name, Play, Enemy)

        elif stMenu.point == 2:
            Connect.SaveGame(name, Play, Enemy, basic)

if __name__ == "__main__":
    logger.debug("Start")
    while start:
        p.time.delay(10)
        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            Play.shiftOXLeft(2)
        elif keys[p.K_RIGHT]:
            Play.shiftOXRight(2)
        elif keys[p.K_ESCAPE]:
            ss = Menu(startMenu)
            ss.menu(window)

            if ss.point == 1:
                name = ss.ask(window, "What is your name?")
                Connect.SearchName(name, Play, Enemy, basic)
            elif ss.point == 1:
                start = True

            elif ss.point == 2:
                name = stMenu.ask(window, "What is your name?")
                Connect.SaveGame(name, Play, Enemy, basic)
            elif ss.point == 3:
                Set = Menu(setMenu)
                Set.Setting(window, Play, Enemy, basic)
                if Set.point == 3:
                    stMenu = Menu(startMenu)

                    stMenu.menu(window)
                    if stMenu.point == 0:
                        start = Connect.SearchName(name, Play, Enemy, basic)
                    elif stMenu.point == 1:
                        name = stMenu.ask(window, "What is your name?")
                        start = Connect.SearchName(name, Play, Enemy, basic)
                    elif stMenu.point == 2:
                        Connect.SaveGame(name, Play, Enemy, basic)
        elif keys[p.K_SPACE]:
            if Ballet.getIsBallet() == False:
                Ballet.setIsBallet(True)
                Ballet.setPoints(Play.getX(), Play.getY())

        for event in p.event.get():
            if event.type == p.QUIT:
                start = False

        leng = Enemy.getX() - Enemy.getWidth()
        if leng >= xWind:
            Enemy.setSide(2)
        elif leng <= 0.0:
            Enemy.setSide(1)
        if Play.getCreate():
            if Ballet.getIsBallet():
                Ballet.shiftOYUp(10)
                Ballet.draw(p, window)
                if Enemy.getY() >= Ballet.getY() and Enemy.getX() <= Ballet.getX() <= Enemy.getX() + Enemy.getHeight():
                    Enemy.wound(1)
                    logger.debug("Player hurt enemy")
                if Ballet.getY() < 0:
                    Ballet.setIsBallet(False)

        if Play.getCreate():
            Play.draw(p, window)
        if Enemy.getCreate():
            Enemy.draw(p, window)
            if Enemy.getSide() == 1:
                Enemy.shiftOXRight(1)
            elif Enemy.getSide() == 2:
                Enemy.shiftOXLeft(1)

        if BalletEnemy.getIsBallet():
            BalletEnemy.shiftOYDn(10)
            BalletEnemy.draw(p, window)
            if BalletEnemy.getY() >= Play.getY() and Play.getX() <= BalletEnemy.getX() <= Play.getX() + Play.getHeight():
                Play.wound(1)
                logger.debug("The enemy hurt the player")
            if BalletEnemy.getY() > yWind:
                BalletEnemy.setIsBallet(False)
                BalletEnemy.setPoints(Enemy.getX(), Enemy.getY())
                BalletEnemy.setIsBallet(True)

        if Play.getHealth() <= 0:
            Play.setCreate(False)
            BalletEnemy.setIsBallet(False)

        if Enemy.getHealth() <= 0:
            Enemy.setCreate(False)
            BalletEnemy.setIsBallet(False)

        basic.draw(p, window)
        font = p.font.Font('12172.ttf', 20)
        rect = p.Rect([5, 5, 220, 25])
        if Play.getCreate() and Enemy.getCreate():
            window.blit(font.render(
                "Hello, " + name + "! Health enemy : " + format(Enemy.getHealth()) + " health " + name + ": " + format(
                    Play.getHealth()), 1, (255, 255, 224)), rect.topleft)
        elif Enemy.getCreate() == False:
            window.blit(font.render("WIN!", 1, (255, 255, 244)), rect.topleft)
        elif Play.getCreate() == False:
            window.blit(font.render("Game over!", 1, (255, 255, 244)), rect.topleft)

        p.display.update()
        window.fill(stMenu.background)
