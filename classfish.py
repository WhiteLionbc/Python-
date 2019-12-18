import pygame
import random
class Player(pygame.sprite.Sprite):
    
    def __init__(self,lis):
        redy = "images/player_{}.png"
        
        self.fishs=[]
        for i in range(1,5):
            fish = pygame.image.load(redy.format(i))
            self.fishs.append(fish)
            
        self.speed = 5
        self.rect = self.fishs[lis].get_rect()
        self.alive = True
        self.rect.topleft = (500,450)
        
    
    def moveUp(self):
        if self.rect.top >= 0:
            self.rect.top = self.rect.top - self.speed
        
    def moveDown(self):
        if self.rect.bottom < 700:
            self.rect.top = self.rect.top + self.speed
        
    def moveLeft(self):
        if self.rect.left >= 0 :
            self.rect.left = self.rect.left - self.speed
        
    def moveRight(self):
        if self.rect.right < 1000:
            self.rect.left = self.rect.left + self.speed
            
class Shrimp(pygame.sprite.Sprite):
    def __init__(self,init_pos):
        self.image = pygame.image.load('images/shrimp.png')
        self.Enemy2 = pygame.image.load('images/fish_2.png')
        self.Enemy3 = pygame.image.load('images/fish_3.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 1
        self.alive = True
        self.id = 0
    def move(self):
        self.rect.right = self.rect.right + self.speed

class Fish2(pygame.sprite.Sprite):
    def __init__(self,init_pos):
        self.image = pygame.image.load('images/fish_2.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 1.5
        self.alive = True
        self.id = 1
        
    def move(self):
        self.rect.right = self.rect.right + self.speed        
        
class Fish3(pygame.sprite.Sprite):
    def __init__(self,init_pos):
        self.image =  pygame.image.load('images/fish_3.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 1.5
        self.alive = True
        self.id = 2
        
    def move(self):
        self.rect.right = self.rect.right + self.speed
        