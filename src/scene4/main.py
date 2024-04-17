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

        self.flame_sound = pygame.mixer.Sound('../../Assets/audio/scene4/flames2.wav')
        self.flame_sound.set_volume(0.5)

        for i in range(1, 12):
            path = f"../../Assets/sprites/scene4/fireman/idle{i}.png"
            img = pygame.image.load(path).convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            self.idle.append(scaled_img)

        for i in range(1,12):
            path = f"../../Assets/sprites/scene4/fireman/w{i}.png"
            img = pygame.image.load(path).convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            self.working.append(scaled_img)

        self.frame = 0
        self.image = self.idle[self.frame]
        self.rect = self.image.get_rect()
        self.rect.bottomright = (self.x, self.y)
    
    def update(self):
        # Update prev_state
        self.prev_state = self.curr_state
        
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.idle[int(self.frame)]
        if self.curr_state == 1:
            # print("out of bound frame: " + str(int(self.frame)))
            self.flame_sound.play()
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

        self.spark_sound = pygame.mixer.Sound('../../Assets/audio/scene4/sparks2.wav')
        self.spark_sound.set_volume(0.5)

        for i in range(1, 12):
            path = f"../../Assets/sprites/scene4/sili_wom/sw{i}.png"
            img = pygame.image.load(path).convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            if i==1:
                self.idle = scaled_img
            else:
                self.working.append(scaled_img)

        self.frame = 0
        self.image = self.idle
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.x, self.y)
    
    def update(self):
        # Update prev_state
        self.prev_state = self.curr_state
        
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.idle
        if self.curr_state == 1:
            # print("out of bound frame: " + str(int(self.frame)))
            self.image = self.working[int(self.frame)]
            self.spark_sound.play()
        
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

        self.wash_sound = pygame.mixer.Sound('../../Assets/audio/scene4/wash2.wav')
        self.wash_sound.set_volume(0.5)

        for i in range(1, 7):
            path = f"../../Assets/sprites/scene4/watergirl/wg{i}.png"
            img = pygame.image.load(path).convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            if i==1:
                self.idle = scaled_img
            else:
                self.working.append(scaled_img)

        self.frame = 0
        self.image = self.idle
        self.rect = self.image.get_rect()
        self.rect.bottomright = (self.x, self.y)
    
    def update(self):
        # Update prev_state
        self.prev_state = self.curr_state
        
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.idle
        if self.curr_state == 1:
            # print("out of bound frame: " + str(int(self.frame)))
            self.image = self.working[int(self.frame)]
            self.wash_sound.play()
        
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

        self.cough_sound = pygame.mixer.Sound('../../Assets/audio/scene4/cough31.mp3')
        self.cough_sound.set_volume(0.5)

        for i in range(1, 15):
            path = f"../../Assets/sprites/scene4/fireboy/b{i}.png"
            img = pygame.image.load(path).convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            if i < 6:
                self.idle.append(scaled_img)
            else:
                self.working.append(scaled_img)

        self.frame = 0
        self.image = self.idle[self.frame]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.x, self.y)
    
    def update(self):
        # Update prev_state
        self.prev_state = self.curr_state
        
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.idle[int(self.frame)]
        if self.curr_state == 1:
            # print("out of bound frame: " + str(int(self.frame)))
            self.image = self.working[int(self.frame)]
            self.cough_sound.play()
        
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

        self. speed = 5
        self.worker_group = worker_goup

        img = pygame.image.load("../../Assets/sprites/scene4/junk/broken_phone.png").convert_alpha()
        scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
        self.image = scaled_img
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.fall_sound = pygame.mixer.Sound('../../Assets/audio/scene4/fall.mp3')
        self.fall_sound.set_volume(0.5)

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
        if self.rect.centery > 620:
            self.fall_sound.play()
            self.kill()

class Flask(pygame.sprite.Sprite):
    def __init__(self,x,y,worker_goup):
        super().__init__()
        self.x = x
        self.y = y

        self.motion_x = x
        self.motion_y = y

        self. speed = 5
        self.worker_group = worker_goup

        img = pygame.image.load("../../Assets/sprites/scene4/junk/flask.png").convert_alpha()
        scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
        self.image = scaled_img
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.fall_sound = pygame.mixer.Sound('../../Assets/audio/scene4/fall.mp3')
        self.fall_sound.set_volume(0.5)

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
        if self.rect.centery > 620:
            self.fall_sound.play()
            self.kill()

class Motherboard(pygame.sprite.Sprite):
    def __init__(self,x,y,worker_goup):
        super().__init__()
        self.x = x
        self.y = y

        self.motion_x = x
        self.motion_y = y

        self. speed = 5
        self.worker_group = worker_goup

        img = pygame.image.load("../../Assets/sprites/scene4/junk/motherboard.png").convert_alpha()
        scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
        self.image = scaled_img
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.fall_sound = pygame.mixer.Sound('../../Assets/audio/scene4/fall.mp3')
        self.fall_sound.set_volume(0.5)

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
        if self.rect.centery > 620:
            self.fall_sound.play()
            self.kill()

class Chemical(pygame.sprite.Sprite):
    def __init__(self,x,y,worker_goup):
        super().__init__()
        self.x = x
        self.y = y

        self.motion_x = x
        self.motion_y = y

        self. speed = 5
        self.worker_group = worker_goup

        img = pygame.image.load("../../Assets/sprites/scene4/junk/yellow_chem.png").convert_alpha()
        scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
        self.image = scaled_img
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.fall_sound = pygame.mixer.Sound('../../Assets/audio/scene4/fall.mp3')
        self.fall_sound.set_volume(0.5)

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
        if self.rect.centery > 620:
            self.fall_sound.play()
            self.kill()

class Line(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = 5

        img = pygame.image.load("../../Assets/sprites/scene4/line.png").convert_alpha()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.rect.centery < 540:
            self.rect.centery += self.speed
        else:
            self.kill()

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("../../Assets/sprites/scene4/bg.png")
pygame.display.set_caption('E-Waste')
clock = pygame.time.Clock()

fireman_group = pygame.sprite.GroupSingle()
fireman_group.add(Fireman(240,240))

sili_woman_group = pygame.sprite.GroupSingle()
sili_woman_group.add(SiliconWoman(560,240))

watergirl_group = pygame.sprite.GroupSingle()
watergirl_group.add(Watergirl(240,500))

fireboy_group = pygame.sprite.GroupSingle()
fireboy_group.add(Fireboy(560,500))

line_group = pygame.sprite.Group()
for j in range(1,30):
    line_group.add(Line(401,540-j*20))

# Timer 
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer,1000)

broken_phone_group = pygame.sprite.Group()

flask_group = pygame.sprite.Group()

motherboard_group = pygame.sprite.Group()

chemical_group = pygame.sprite.Group()

story_msg = pygame.mixer.Sound('../../Assets/audio/scene4/scene4_audio.wav')
story_msg.play()
# bg_music = pygame.mixer.Sound('../../Assets/audio/scene4/happy1.wav')
# bg_music.set_volume(0.2)
# bg_music.play()

# Define the color
BLACK = (0, 0, 0)

count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == timer:
            # Choose a random object type to add
            choice = randint(1, 4)
            if choice == 1:
                broken_phone_group.add(BrokenPhone(randint(350,450), -50, fireboy_group))
            elif choice == 2:
                flask_group.add(Flask(randint(350,450), -50, watergirl_group))
            elif choice == 3:
                motherboard_group.add(Motherboard(randint(350,450), -50, sili_woman_group))
            elif choice == 4:
                chemical_group.add(Chemical(randint(350,450), -50, fireman_group))

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

    if(count < 5): count+=1
    if count == 4 :
        line_group.add(Line(401,-5))
        count = 0
    line_group.draw(screen)
    line_group.update()

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

