#Author: Swapnil Srivastava
# A game all about shooting monsters but not getting touched by them.
# Bigger monsters are worth more points.
# Beware, you only have 25 bullets. Use all and it's Game Over
import pygame
from pygame.locals import *
import random
import sys
import time

pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE  = (0, 0, 255)
LRED   = (255, 204, 203)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
sky_blue = (135,206,235)

#This is the view surface
shooting_range = pygame.display.set_mode((1000,1000))
shooting_range.fill(sky_blue)
pygame.display.set_caption("Shooting Monsters")

#Our gun object that is controlled by mouse position and has 25 bullets
class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rem_bullets = 25
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
        if(self.rem_bullets<=0):
            pygame.event.post(pygame.event.Event(GAMEOVER))

#Our bullet object created upon mouse click 
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.color = BLACK
        #self.position = pos
        self.velocity = 5
        self.size = 5,5
        self.rect = pygame.Rect(pos,self.size)
    
    def update(self):
        self.rect.move_ip(10,0)
    
    def draw(self,surface):
        pygame.draw.rect(surface, BLACK, self.rect)

#Three types of monsters with different kill score and health values. 
# Once the monster rect collides with bullet then the health of monster goes down
# If monster health reaches 0 then the appropriate points are added to score.
# If any monster collides with gun then it's Game Over!
class Monster(pygame.sprite.Sprite):
    def __init__(self, lvl, pos):
        super().__init__()
        self.lvl = lvl
        if(lvl == 1):
            self.image = pygame.image.load("lvl_1.png")
            #self.pos = 500,250
            self.image = pygame.transform.scale(self.image, (50,50))
        elif(lvl == 2):
            self.image = pygame.image.load("lvl_2.png")
            #self.pos = 500,250
            self.image = pygame.transform.scale(self.image, (80,80))
            self.health = 2
        elif(lvl == 3):
            self.image = pygame.image.load("lvl_3.png")
            #self.pos = 500,250
            self.image = pygame.transform.scale(self.image, (150,150))
            self.health = 3
        self.rect = self.image.get_rect()
        self.rect.center = pos
    
    def update(self):
        if(self.lvl == 1):
            self.rect.center =  (self.rect.center[0]-5,self.rect.center[1])
        elif(self.lvl == 2):
            self.rect.center =  (self.rect.center[0]-3,self.rect.center[1])
        elif(self.lvl == 3):
            self.rect.center =  (self.rect.center[0]-1,self.rect.center[1])

    
    def draw(self,surface):
        surface.blit(self.image, self.rect)
    
    def get_center(self):
        x = self.rect.center
        return x 
    
    # def shot(self, bullets):
    #     for bullet in bullets:
    #         if(self.rect.colliderect(bullet.rect)):
    #             return True
    #         else:
    #             return False
    #     return False
        
class Score():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(str(self.score), True, GREEN, sky_blue)
        self.rect = self.text.get_rect()
        self.rect.center = 500,50
    
    def draw(self, surface):
        surface.blit(self.text, self.rect)
    
    def update(self, score):
        self.score = score
        self.text = self.font.render("Score: " + str(self.score), True, BLACK, sky_blue)
        self.rect = self.text.get_rect()
        self.rect.center = 500,50
    
    def get_score(self):
        return self.score
    
#Initialize gun, bullets,score, monsters, and events
gun = Gun()
fired = False
bullets = []
monsters = []
monsters.append(Monster(1, (1000,250))) 
GAMEOVER = pygame.USEREVENT + 0
CREATEMONSTER_lvl1 = pygame.USEREVENT + 1
pygame.time.set_timer(CREATEMONSTER_lvl1, 800)
CREATEMONSTER_lvl2 = pygame.USEREVENT + 2
pygame.time.set_timer(CREATEMONSTER_lvl2, 1000)
CREATEMONSTER_lvl3 = pygame.USEREVENT + 3
pygame.time.set_timer(CREATEMONSTER_lvl3, 1500)
pygame.mouse.set_pos(50,250)

score = Score()

alive = True # False if gun collides with monster
# Game loop

while alive:
    for event in pygame.event.get():
        if event.type == GAMEOVER:
            alive = False
            # score.draw(shooting_range)
            # font = pygame.font.Font('freesansbold.ttf', 32)
            # text = font.render("Game Over!", True, WHITE)
            # rect = text.get_rect()
            # rect.center = 500,500
            # shooting_range.blit(text, rect)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == CREATEMONSTER_lvl1:
            monsters.append(Monster(1, (1000,random.randint(0,900))))
        if event.type == CREATEMONSTER_lvl2:
            monsters.append(Monster(2, (1000,random.randint(0,900)))) 
        if event.type == CREATEMONSTER_lvl3:
            monsters.append(Monster(3, (1000,random.randint(0,900)))) 
        if event.type == MOUSEMOTION:
            gun.update()
        if event.type == MOUSEBUTTONDOWN:
            if(len(bullets)<10):
                bullets.append(Bullet(pygame.mouse.get_pos()))
                gun.shoot()
            else:
                pygame.event.post(pygame.event.Event(GAMEOVER))

        

    shooting_range.fill(sky_blue)
    
    gun.draw(shooting_range)
    
    for monster in monsters:
        
        if(monster.get_center()[0]<0):
            monsters.remove(monster)
        elif(gun.rect.colliderect(monster.rect)):
            # shooting_range.fill(RED)
            # gun.draw(shooting_range)
            pygame.event.post(pygame.event.Event(GAMEOVER))
        else:
            monster.update()
        monster.draw(shooting_range)
    for bullet in bullets:
        bullet.draw(shooting_range)
        bullet.update()
        for monster in monsters:
            if(bullet.rect.colliderect(monster.rect)):
                bullets.remove(bullet)
                if(monster.lvl == 1):
                    monsters.remove(monster)
                    score.update(score.get_score() + 50)
                else:
                    if(monster.health==1):
                        monsters.remove(monster)
                        score.update(score.get_score() + (monster.lvl * 80))
                    else:
                        monster.health -= 1
    
    score.draw(shooting_range)

        
    pygame.display.update()
    
    FramePerSec.tick(FPS)

pygame.display.update()
shooting_range.fill(LRED)
score.draw(shooting_range)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("Game Over!", True, WHITE)
rect = text.get_rect()
rect.center = 500,500
shooting_range.blit(text, rect)
pygame.display.update()
time.sleep(5)
pygame.quit()
sys.exit()