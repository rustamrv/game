import pygame as p
from LogicalRectShape import *
from Player import * 
from CircleShape import *
from Menu import *
from WorkFile import *
from SQL import *

p.init()

xWind = 800
yWind = 600
window = p.display.set_mode([xWind, yWind])

basic = LogicalRect(5, 595, 790, -60, (255,255,255))
start = False
isBalletEnemy = True
isEnemy = True
isPlayer = False
isBalletPlayer = False

Play = Player(5, 525, 20, -10, (0, 128, 0))
Enemy = Player(5, 50, 20, -10, (0, 128, 0))

Ballet = CircleShape(Play.getX(), Play.getY(), 5, (255,255,255))
BalletEnemy = CircleShape(Enemy.getX(), Enemy.getY(), 5, (255,255,255))

side = 1
File = WorkFile("Menu.json")
startMenu = File.read()
File1 = WorkFile("settings1.json")
setMenu = File1.read()

database = 'DRIVER={SQL Server};SERVER=LAPTOP-JGQ8MSK8;DATABASE=DB;UID=Admin;PWD=qwerty12345'
Connect = Sql(database)

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
            start = Connect.SearchName(name, Play, Enemy)
        elif stMenu.point == 1:
            name = stMenu.ask(window, "What is your name?")
            Connect.SearchName(name, Play, Enemy)
            start = Connect.SearchGame(name, Play, Enemy, basic)

        elif stMenu.point == 2:
            Connect.SaveGame(name, Play, Enemy, basic)

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
        if isBalletPlayer == False:
            isBalletPlayer = True
            Ballet.setPoints(Play.getX(), Play.getY())

    for event in p.event.get():
        if event.type == p.QUIT:
            start = False

    if side == 1:
        Enemy.shiftOXRight(1)
    elif side == 2:
        Enemy.shiftOXLeft(1)

    leng = Enemy.getX() - Enemy.getWidth()
    if leng >= xWind:
        side = 2
    elif leng <= 0.0:
        side = 1
    if isPlayer:
        if isBalletPlayer:
            Ballet.shiftOYUp(10)
            Ballet.draw(p, window)
            if Enemy.getY() >= Ballet.getY() and Enemy.getX() <= Ballet.getX() <= Enemy.getX() + Enemy.getHeight():
                Enemy.wound(1)

            if Ballet.getY() < 0:
                isBalletPlayer = False

    Play.draw(p,window)
    isPlayer = True
    Enemy.draw(p,window)
    if isBalletEnemy:
        BalletEnemy.shiftOYDn(10)
        BalletEnemy.draw(p,window)
        if BalletEnemy.getY() >= Play.getY() and Play.getX() <= BalletEnemy.getX() <= Play.getX() + Play.getHeight():
            Play.wound(1)
        if BalletEnemy.getY() > yWind:
            isBalletEnemy = False
            BalletEnemy.setPoints(Enemy.getX(), Enemy.getY())
            isBalletEnemy = True
    basic.draw(p, window)
    font = p.font.Font('12172.ttf', 20)
    rect = p.Rect([5, 5, 220, 25])
    window.blit(font.render("Hello, " + name + "! Health enemy : " + format(Enemy.getHealth()) + " health " + name + ": " + format(
        Play.getHealth()), 1, (255, 255, 224)), rect.topleft)
    p.display.update()
    window.fill(stMenu.background)






