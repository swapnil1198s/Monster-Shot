import pygame
from pygame.locals import *
import random
import sys

pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
sky_blue = (135,206,235)


shooting_range = pygame.display.set_mode((500,500))
shooting_range.fill(sky_blue)
pygame.display.set_caption("Shooting Range")

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.gun =  Gun()


class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rem_bullets = 10
        self.mode = 1
        self.image = pygame.image.load("gun.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (50,250)
    
    def update(self):
        #get mouse position for aim and then use clicks for bullets
        self.rect.center = pygame.mouse.get_pos() #get_pos() -> (x, y)

    def draw(self,surface):
        surface.blit(self.image, self.rect)

    def shoot(self):
        self.rem_bullets -= 1

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        print("here")
        self.color = BLACK
        #self.position = pos
        self.velocity = 5
        self.size = 5,5
        self.rect = pygame.Rect(pos,self.size)
    
    def update(self):
        self.rect.move_ip(10,0)
    
    def draw(self,surface):
        pygame.draw.rect(surface, BLACK, self.rect)

class Monster(pygame.sprite.Sprite):
    def __init__(self, lvl):
        super().__init__()
        self.image = pygame.image.load("lvl_1.png")
        #self.pos = 500,250
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = 500,250
    
    def updated(self):
        self.rect.center =  (self.rect.center[0]-10,self.rect.center[1] - 0)
    
    def draw(self,surface):
        surface.blit(self.image, self.rect)
        

    
#Game loop
gun = Gun()
fired = False
bullets = []
monsters = []
monsters.append(Monster(1))
pygame.mouse.set_pos(50,250)
CREATEMONSTER = pygame.USEREVENT + 1
pygame.time.set_timer(CREATEMONSTER, 120)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            gun.update()
        if event.type == MOUSEBUTTONDOWN:
            if(len(bullets)<10):
                bullets.append(Bullet(pygame.mouse.get_pos()))
                gun.shoot()
        # if event.type == CREATEMONSTER:
        #     monsters.append(Monster(1))
    shooting_range.fill(WHITE)
    gun.draw(shooting_range)
    
    for bullet in bullets:
        bullet.draw(shooting_range)
        bullet.update()
    
    for monster in monsters:
        monster.draw(shooting_range)
        monster.update()
    pygame.display.update()
    
    FramePerSec.tick(FPS)