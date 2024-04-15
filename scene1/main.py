import pygame
import math
from sys import exit
from random import randint, choice
from enum import Enum

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, worker_group, is_inverted=False):
        super().__init__()
        
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.speed = 15  # Adjust speed as needed
        
        self.walk_away = []
        self.walk_towards = []
        self.stand = None
        self.shout = []
        self.frame = 0
        self.shout_frames = 0
        self.is_inverted = is_inverted
        self.worker_group = worker_group
        
        for i in range(0, 13):
            path = f"../Assets/sprites/scene1/s{i}.png"
            img = pygame.image.load(path).convert_alpha()
            if self.is_inverted == False:
                sprite = img
            else:
                sprite = pygame.transform.flip(img, True, False)
            if i in range(0, 4):
                self.walk_away.append(sprite)
            elif i in range(4, 10):
                self.walk_towards.append(sprite)
            elif i == 10:
                self.stand = sprite
            elif i in range(11, 13):
                self.shout.append(sprite)
        
        # Set initial sprite to standing
        self.image = self.stand
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
                
        self.prev_state = -1
        self.curr_state = 2
    
    def update(self):
        if self.curr_state != self.prev_state:
            self.frame = 0
        if self.curr_state == 0:
            self.move_away()
        elif self.curr_state == 1:
            self.move_towards()
        elif self.prev_state == 3 and self.curr_state == 2:
            for worker in self.worker_group:
                if abs(worker.rect.centery -90 - self.rect.centery) <= 20:
                    print("touch")
                    worker.curr_state = 0
                else:
                    print("no touch")
                    print(f"Soldier rect: {self.rect.centerx}, {self.rect.centery}")
                    print(f"Worker rect: {worker.rect.centerx}, {worker.rect.centery}")


        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.walk_away[int(self.frame)]
        elif self.curr_state == 1:
            self.image = self.walk_towards[int(self.frame)]
        elif self.curr_state == 2:
            self.image = self.stand
        elif self.curr_state == 3:
            self.image = self.shout[int(self.frame)]
        
        # Update previous state
        self.prev_state = self.curr_state

        # Move to the next frame
        if self.curr_state == 0:
            if self.frame < 3:
                self.frame += 0.5
            else: self.frame = 0
            # print("curr_state: "+ str(self.curr_state))
            # print("frame: "+str(self.frame))
        if self.curr_state == 1:  
            if self.frame < 5:
                self.frame += 0.5
            else: self.frame = 0
            # print("curr_state: "+ str(self.curr_state))
            # print("frame: "+str(self.frame))
        if self.curr_state == 3:  
            if self.shout_frames < 8:
                if self.frame < 1:
                    self.frame += 0.5
                else: self.frame = 0
                self.shout_frames +=1
                # print("shout frames : "+str(self.shout_frames))
                # print("curr_state: "+ str(self.curr_state))
                # print("frame: "+str(self.frame))
            else:
                self.curr_state = 2
                self.shout_frames = 0
                # print("curr_state: "+ str(self.curr_state))
                # print("frame: "+str(self.frame))

    def move_away(self):
        if self.rect.centery > self.target_y:
            self.rect.centery -= self.speed
        else:
            self.curr_state = 3
            self.frame = 0
            # print("curr_state: "+ str(self.curr_state))
            # print("frame: "+str(self.frame))
                    
    def move_towards(self):
        if self.rect.centery < self.target_y:
            self.rect.centery += self.speed
        else:
            self.curr_state = 3
            self.frame = 0
            # print("curr_state: "+ str(self.curr_state))
            # print("frame: "+str(self.frame))
                
    def set_target(self, target_x, target_y):
        self.target_x = target_x
        self.target_y = target_y
        if target_y < self.rect.centery:
            self.curr_state = 0
        else:
            self.curr_state = 1

class Worker(pygame.sprite.Sprite):
    def __init__(self, x, y, is_inverted=False):
        super().__init__()
        
        self.working = []
        self.tired = []
        self.is_inverted = is_inverted
        self.curr_state = 0
        self.prev_state = -1
        
        for i in range(0, 4):
            path = f"../Assets/sprites/scene1/w{i}.png"
            img = pygame.image.load(path).convert_alpha()
            if self.is_inverted == False:
                sprite = img
            else:
                sprite = pygame.transform.flip(img, True, False)
            self.working.append(sprite)
        for i in range(2,-1,-1):
            self.working.append(self.working[i])        
        
        for i in range(0,3):
            path = f"../Assets/sprites/scene1/t{i}.png"
            img = pygame.image.load(path).convert_alpha()
            if self.is_inverted == True:
                sprite = img
            else:
                sprite = pygame.transform.flip(img, True, False)
            self.tired.append(sprite)   
        for i in range(1,-1,-1):
            self.tired.append(self.tired[i])
        
        # Set initial sprite to be randomly working
        self.frame = randint(0,3)
        self.image = self.working[self.frame]
        self.rect = self.image.get_rect()
        if self.is_inverted == False:
            self.rect.bottomright = (x,y)
        else:
            self.rect.bottomleft = (x,y)

    def update(self):
        self.prev_state = self.curr_state
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.working[int(self.frame)]
        if self.curr_state == 1:
            # print("out of bound frame: " + str(int(self.frame)))
            self.image = self.tired[int(self.frame)]        
        
        if self.is_inverted == False:
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
        else:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        
        # Move to the next frame
        if self.curr_state == 0:
            if self.frame < 6:
                self.frame += 0.2
            else: self.frame = 0

            # print("curr_state: "+ str(self.curr_state))
            # print("frame: "+str(self.frame))
        if self.curr_state == 1:
            if self.frame < 4:
                self.frame += 0.2
            else: self.frame = 0
            # print("frame: " + str(int(self.frame)))
            # print("curr_state: "+ str(self.curr_state))
            # print("frame: "+str(self.frame))
        
        # Random logic for worker to get tired.
        # Suggest better logic
        if randint(1,500) == 1:
            self.curr_state = 1
            if self.curr_state != self.prev_state:
                self.frame = 0

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((1600, 1200))
background = pygame.image.load("../Assets/sprites/scene1/bg.png")
pygame.display.set_caption('Congo')
clock = pygame.time.Clock()

# Groups

worker_group_left = pygame.sprite.Group()
worker_group_right = pygame.sprite.Group()

workers_left = [Worker(750,1000),Worker(750,800),Worker(750,600),Worker(750,400),Worker(750,200)]
workers_right = [Worker(850,1000,is_inverted=True),Worker(850,800,is_inverted=True),Worker(850,600,is_inverted=True),Worker(850,400,is_inverted=True),Worker(850,200,is_inverted=True)]

for worker in workers_left:
    worker_group_left.add(worker)
for worker in workers_right:
    worker_group_right.add(worker)

soldier_group = pygame.sprite.Group()
soldier_left = Soldier(400,1000,worker_group_left,is_inverted=True)
soldier_right = Soldier(1200,1000,worker_group_right)
soldier_group.add(soldier_left)
soldier_group.add(soldier_right)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            target_x, target_y = pygame.mouse.get_pos()
            if target_x < 800:
                for worker in worker_group_left:
                    if worker.rect.collidepoint(target_x, target_y):
                        soldier_left.set_target(worker.rect.centerx , worker.rect.centery-90)
            else:
                for worker in worker_group_right:
                    if worker.rect.collidepoint(target_x, target_y):
                        soldier_right.set_target(worker.rect.centerx, worker.rect.centery-90)
    
    # screen.fill((255, 255, 255))
    screen.blit(background,(0,0))
    soldier_group.draw(screen)    
    soldier_group.update()

    worker_group_left.draw(screen)
    worker_group_left.update()
    
    worker_group_right.draw(screen)
    worker_group_right.update()
    
    pygame.display.update()
    clock.tick(25)


