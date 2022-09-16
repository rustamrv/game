from abc import ABC, abstractmethod
from menu import Menu
from player import Player 
from pygame import display, init
import pygame
from logicalRect import LogicalRect
from ballet import Ballet
from colorInterface import Color 

class PyInterface(ABC): 
    @abstractmethod
    def run(self):
        pass 
    @abstractmethod 
    def events(self):
        pass

class PygameService(PyInterface):

    def __init__(self, xWind, yWind, list):
        init();
        PyInterface.__init__(self)
        self.display = display.set_mode([xWind, yWind]);
        self.start = True
        self.menu = Menu(list)  
        self.basic = LogicalRect(53, 100, 100, 100, Color.WHITE.value)  
        self.player = Player(5, 525, 20, 10,  Color.GREEN.value, None);  
        self.enemy = Player(5, 50, 20, 10, Color.GREEN.value, 1)
        self.bPlayer = Ballet(self.player.getShape().getX(), self.player.getShape().getY(), self.player.getShape().getHeight(),
                      self.player.getShape().getWidth(), 5, Color.WHITE.value)
        self.bEnemy = Ballet(self.enemy.getShape().getX(), self.enemy.getShape().getY(), self.enemy.getShape().getHeight(),
                     self.enemy.getShape().getWidth(), 5, Color.WHITE.value)
    
    def run(self):
        self.start = self.menu.menu(self.display) 
 
        while self.start: 
            pygame.time.delay(10)
            self.display.fill(self.menu.background)  
  
            length = self.enemy.getShape().getX() - self.enemy.getShape().getWidth()
            if length >= self.display.get_width():
                self.enemy.setSide(2)
            elif length <= 0.0:
                self.enemy.setSide(1)
            if not self.player.isDead():
                self.player.draw(pygame, self.display)
                if not self.bPlayer.isDead():
                    self.bPlayer.getShape().shiftOYUp(10)
                    self.bPlayer.draw(pygame, self.display)
                    if self.enemy.getShape().getY() >= self.bPlayer.getShape().getY() and self.enemy.getShape().getX() <= self.bPlayer.getShape().getX() <= self.enemy.getShape().getX() + self.enemy.getShape().getHeight():
                        self.enemy.wound(1) 
            if not self.bEnemy.isDead():
                self.bEnemy.getShape().shiftOYDn(10)
                self.bEnemy.draw(pygame, self.display)
                if self.bEnemy.getShape().getY() >= self.player.getShape().getY() and self.player.getShape().getX() <= self.bEnemy.getShape().getX() <= self.player.getShape().getX() + self.player.getShape().getHeight():
                    self.player.wound(1)
                if self.bEnemy.getShape().getY() > self.display.get_height():
                    self.bEnemy.getShape().setPoints(self.enemy.getShape().getX(), self.enemy.getShape().getY())
                if not self.enemy.isDead():
                    self.enemy.draw(pygame, self.display)
                    if self.enemy.getSide() == 1:
                        self.enemy.getShape().shiftOXRight(1)
                    elif self.enemy.getSide() == 2:
                        self.enemy.getShape().shiftOXLeft(1)

            
            self.bPlayer.draw(pygame, self.display)
            self.bEnemy.draw(pygame, self.display)  
            rect = pygame.Rect([5, 5, 220, 25])
            if not self.player.isDead() and not self.enemy.isDead():
                self.display.blit( self.menu.font.render(
                    "Health enemy : " + format(self.enemy.getHealth()) + " health " +
                    ": " + format(
                        self.player.getHealth()), 1, (255, 255, 224)), rect.topleft)
            elif self.enemy.isDead():
                self.display.blit(self.menu.font.render("WIN!", 1, (255, 255, 244)), rect.topleft)
                self.bEnemy.setHealth(-1)
            elif self.enemy.isDead():
                self.display.blit(self.menu.font.render("Game over!", 1, (255, 255, 244)), rect.topleft)
            
            self.events() 
            pygame.display.update() 
            pygame.display.flip() 

    def events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.getShape().shiftOXLeft(2)
        elif keys[pygame.K_RIGHT]:
            self.player.getShape().shiftOXRight(2)
        elif keys[pygame.K_SPACE]:
            if not self.bPlayer.isDead():
                self.bPlayer.getShape().setPoints(self.player.getShape().getX(), self.player.getShape().getY())
        for event in pygame.event.get():   
            if event.type == pygame.QUIT: 
                self.start = False 
