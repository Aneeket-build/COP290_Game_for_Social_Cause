import pygame
import math
from sys import exit
from random import randint

class Fireman(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.x = x
        self.y = y

        self.idle = []
        self.working = []

        self.prev_state = -1
        self.curr_state = 0

        self.working_frames = 0

        for i in range(1, 12):
            path = f"../Assets/sprites/scene4/fireman/idle{i}.png"
            sprite = pygame.image.load(path).convert_alpha()
            self.idle.append(sprite)

        for i in range(1,12):
            path = f"../Assets/sprites/scene4/fireman/w{i}.png"
            sprite = pygame.image.load(path).convert_alpha()
            self.working.append(sprite)

        self.frame = 0
        self.image = self.idle[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    def update(self):
        # Update prev_state
        self.prev_state = self.curr_state
        
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.idle[int(self.frame)]
        if self.curr_state == 1:
            # print("out of bound frame: " + str(int(self.frame)))
            self.image = self.working[int(self.frame)]
        
        # Move to the next frame
        if self.curr_state == 0:
            if self.frame < 10:
                self.frame += 0.2
            else: self.frame = 0

            # print("curr_state: "+ str(self.curr_state))
            # print("frame: "+str(self.frame))
        if self.curr_state == 1:
            if self.working_frames < 25:
                if self.frame < 10:
                   self.frame += 0.4
                else: self.frame = 0
                self.working_frames += 1
            else:
                self.working_frames = 0
                self.curr_state = 0
                self.frame = 0
            # print("frame: " + str(int(self.frame)))
            # print("curr_state: "+ str(self.curr_state))
            # print("frame: "+str(self.frame))

class SiliconWoman(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.x = x
        self.y = y

        self.idle = None
        self.working = []

        self.prev_state = -1
        self.curr_state = 0

        self.working_frames = 0

        for i in range(1, 12):
            path = f"../Assets/sprites/scene4/sili_wom/sw{i}.png"
            sprite = pygame.image.load(path).convert_alpha()
            if i==1:
                self.idle = sprite
            else:
                self.working.append(sprite)

        self.frame = 0
        self.image = self.idle
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    def update(self):
        # Update prev_state
        self.prev_state = self.curr_state
        
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.idle
        if self.curr_state == 1:
            # print("out of bound frame: " + str(int(self.frame)))
            self.image = self.working[int(self.frame)]
        
        if self.curr_state == 1:
            if self.working_frames < 25:
                if self.frame < 9:
                    self.frame += 0.4
                else: self.frame = 0
                self.working_frames += 1
            else:
                self.working_frames = 0
                self.curr_state = 0
                self.frame = 0

class Watergirl(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.x = x
        self.y = y

        self.idle = None
        self.working = []

        self.prev_state = -1
        self.curr_state = 0

        self.working_frames = 0

        for i in range(1, 7):
            path = f"../Assets/sprites/scene4/watergirl/wg{i}.png"
            sprite = pygame.image.load(path).convert_alpha()
            if i==1:
                self.idle = sprite
            else:
                self.working.append(sprite)

        self.frame = 0
        self.image = self.idle
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    def update(self):
        # Update prev_state
        self.prev_state = self.curr_state
        
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.idle
        if self.curr_state == 1:
            # print("out of bound frame: " + str(int(self.frame)))
            self.image = self.working[int(self.frame)]
        
        if self.curr_state == 1:
            if self.working_frames < 25:
                if self.frame < 4:
                    self.frame += 0.4
                else: self.frame = 0
                self.working_frames += 1
            else:
                self.working_frames = 0
                self.curr_state = 0
                self.frame = 0
                

class Fireboy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.x = x
        self.y = y

        self.idle = []
        self.working = []

        self.prev_state = -1
        self.curr_state = 0

        self.working_frames = 0

        for i in range(1, 15):
            path = f"../Assets/sprites/scene4/fireboy/b{i}.png"
            sprite = pygame.image.load(path).convert_alpha()
            if i < 6:
                self.idle.append(sprite)
            else:
                self.working.append(sprite)

        self.frame = 0
        self.image = self.idle[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    def update(self):
        # Update prev_state
        self.prev_state = self.curr_state
        
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.idle[int(self.frame)]
        if self.curr_state == 1:
            # print("out of bound frame: " + str(int(self.frame)))
            self.image = self.working[int(self.frame)]
        
        # Move to the next frame
        if self.curr_state == 0:
            if self.frame < 4:
                self.frame += 0.2
            else: self.frame = 0

            # print("curr_state: "+ str(self.curr_state))
            # print("frame: "+str(self.frame))
        if self.curr_state == 1:
            if self.working_frames < 25:
                if self.frame < 8:
                    self.frame += 0.4
                else: self.frame = 0
                self.working_frames += 1
            else:
                self.working_frames = 0
                self.curr_state = 0
                self.frame = 0
            # print("frame: " + str(int(self.frame)))
            # print("curr_state: "+ str(self.curr_state))
            # print("frame: "+str(self.frame))

class BrokenPhone(pygame.sprite.Sprite):
    def __init__(self,x,y,worker_goup):
        super().__init__()
        self.x = x
        self.y = y

        self.motion_x = x
        self.motion_y = y

        self. speed = 10
        self.worker_group = worker_goup

        sprite = pygame.image.load("../Assets/sprites/scene4/junk/broken_phone.png").convert_alpha()
        
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.dragging = False

    def update(self):
        if self.dragging:
            self.rect.center = pygame.mouse.get_pos()
        else:
            for worker in self.worker_group:
                if self.rect.colliderect(worker.rect):
                    if self.dragging == False:
                        self.kill()
                        worker.curr_state = 1
                else:
                    self.motion_y += self.speed
                    self.rect.center = (self.motion_x, self.motion_y)

class Flask(pygame.sprite.Sprite):
    def __init__(self,x,y,worker_goup):
        super().__init__()
        self.x = x
        self.y = y

        self.motion_x = x
        self.motion_y = y

        self. speed = 10
        self.worker_group = worker_goup

        sprite = pygame.image.load("../Assets/sprites/scene4/junk/flask.png").convert_alpha()
        
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.dragging = False

    def update(self):
        if self.dragging:
            self.rect.center = pygame.mouse.get_pos()
        else:
            for worker in self.worker_group:
                if self.rect.colliderect(worker.rect):
                    if self.dragging == False:
                        self.kill()
                        worker.curr_state = 1
                else:
                    self.motion_y += self.speed
                    self.rect.center = (self.motion_x, self.motion_y)

class Motherboard(pygame.sprite.Sprite):
    def __init__(self,x,y,worker_goup):
        super().__init__()
        self.x = x
        self.y = y

        self.motion_x = x
        self.motion_y = y

        self. speed = 10
        self.worker_group = worker_goup

        sprite = pygame.image.load("../Assets/sprites/scene4/junk/motherboard.png").convert_alpha()
        
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.dragging = False

    def update(self):
        if self.dragging:
            self.rect.center = pygame.mouse.get_pos()
        else:
            for worker in self.worker_group:
                if self.rect.colliderect(worker.rect):
                    if self.dragging == False:
                        self.kill()
                        worker.curr_state = 1
                else:
                    self.motion_y += self.speed
                    self.rect.center = (self.motion_x, self.motion_y)

class Chemical(pygame.sprite.Sprite):
    def __init__(self,x,y,worker_goup):
        super().__init__()
        self.x = x
        self.y = y

        self.motion_x = x
        self.motion_y = y

        self. speed = 10
        self.worker_group = worker_goup

        sprite = pygame.image.load("../Assets/sprites/scene4/junk/yellow_chem.png").convert_alpha()
        
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.dragging = False

    def update(self):
        if self.dragging:
            self.rect.center = pygame.mouse.get_pos()
        else:
            for worker in self.worker_group:
                if self.rect.colliderect(worker.rect):
                    if self.dragging == False:
                        self.kill()
                        worker.curr_state = 1
                else:
                    self.motion_y += self.speed
                    self.rect.center = (self.motion_x, self.motion_y)
    
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((1600, 1200))
background = pygame.image.load("../Assets/sprites/scene4/pink.png")
pygame.display.set_caption('E-Waste')
clock = pygame.time.Clock()

fireman_group = pygame.sprite.GroupSingle()
fireman_group.add(Fireman(300,300))

sili_woman_group = pygame.sprite.GroupSingle()
sili_woman_group.add(SiliconWoman(1100,300))

watergirl_group = pygame.sprite.GroupSingle()
watergirl_group.add(Watergirl(300,700))

fireboy_group = pygame.sprite.GroupSingle()
fireboy_group.add(Fireboy(1100,700))

# Timer 
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer,1000)

broken_phone_group = pygame.sprite.Group()

flask_group = pygame.sprite.Group()

motherboard_group = pygame.sprite.Group()

chemical_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == timer:
            # Choose a random object type to add
            choice = randint(1, 4)
            if choice == 1:
                broken_phone_group.add(BrokenPhone(randint(700,900), -100, fireboy_group))
            elif choice == 2:
                flask_group.add(Flask(randint(700,900), -100, watergirl_group))
            elif choice == 3:
                motherboard_group.add(Motherboard(randint(700,900), -100, sili_woman_group))
            elif choice == 4:
                chemical_group.add(Chemical(randint(700,900), -100, fireman_group))

        for broken_phone in broken_phone_group:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if broken_phone.rect.collidepoint(event.pos):
                    broken_phone.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if broken_phone.dragging:
                    broken_phone.dragging = False
        for flask in flask_group:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if flask.rect.collidepoint(event.pos):
                    flask.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if flask.dragging:
                    flask.dragging = False
        for motherboard in motherboard_group:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if motherboard.rect.collidepoint(event.pos):
                    motherboard.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if motherboard.dragging:
                    motherboard.dragging = False
        for chemical in chemical_group:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if chemical.rect.collidepoint(event.pos):
                    chemical.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if chemical.dragging:
                    chemical.dragging = False

    screen.blit(background,(0,0))

    fireman_group.draw(screen)    
    fireman_group.update()

    sili_woman_group.draw(screen)
    sili_woman_group.update()

    watergirl_group.draw(screen)
    watergirl_group.update()

    fireboy_group.draw(screen)    
    fireboy_group.update()

    broken_phone_group.draw(screen)
    broken_phone_group.update()

    flask_group.draw(screen)
    flask_group.update()

    motherboard_group.draw(screen)
    motherboard_group.update()

    chemical_group.draw(screen)
    chemical_group.update()

    pygame.display.update()
    clock.tick(25)

