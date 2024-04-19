import pygame
import math
from sys import exit
from random import randint
import time

def execute_failure():
    with open('failure.py', 'r') as file:
        code = file.read()
    exec(code)

fallen_objects = 0
total_objects = 0

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

        self.flame_sound = pygame.mixer.Sound('../Assets/audio/scene4/flames2.wav')
        self.flame_sound.set_volume(0.5)

        for i in range(1, 12):
            path = f"../Assets/sprites/scene4/fireman/idle{i}.png"
            img = pygame.image.load(path).convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            self.idle.append(scaled_img)

        for i in range(1,12):
            path = f"../Assets/sprites/scene4/fireman/w{i}.png"
            img = pygame.image.load(path).convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            self.working.append(scaled_img)

        self.frame = 0
        self.image = self.idle[self.frame]
        self.rect = self.image.get_rect()
        self.rect.inflate(50,50)
        self.rect.bottomright = (self.x, self.y)
    
    def update(self):
        # Update prev_state
        self.prev_state = self.curr_state
        
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.idle[int(self.frame)]
        if self.curr_state == 1:
            self.flame_sound.play()
            self.image = self.working[int(self.frame)]
        
        # Move to the next frame
        if self.curr_state == 0:
            if self.frame < 10:
                self.frame += 0.2
            else: self.frame = 0

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

        self.spark_sound = pygame.mixer.Sound('../Assets/audio/scene4/sparks2.wav')
        self.spark_sound.set_volume(0.5)

        for i in range(1, 12):
            path = f"../Assets/sprites/scene4/sili_wom/sw{i}.png"
            img = pygame.image.load(path).convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            if i==1:
                self.idle = scaled_img
            else:
                self.working.append(scaled_img)

        self.frame = 0
        self.image = self.idle
        self.rect = self.image.get_rect()
        self.rect.inflate(50,50)
        self.rect.bottomleft = (self.x, self.y)
    
    def update(self):
        # Update prev_state
        self.prev_state = self.curr_state
        
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.idle
        if self.curr_state == 1:
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

        self.wash_sound = pygame.mixer.Sound('../Assets/audio/scene4/wash3.wav')
        self.wash_sound.set_volume(0.2)

        for i in range(1, 7):
            path = f"../Assets/sprites/scene4/watergirl/wg{i}.png"
            img = pygame.image.load(path).convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            if i==1:
                self.idle = scaled_img
            else:
                self.working.append(scaled_img)

        self.frame = 0
        self.image = self.idle
        self.rect = self.image.get_rect()
        self.rect.inflate(50,50)
        self.rect.bottomright = (self.x, self.y)
    
    def update(self):
        # Update prev_state
        self.prev_state = self.curr_state
        
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.idle
        if self.curr_state == 1:
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

        self.cough_sound = pygame.mixer.Sound('../Assets/audio/scene4/fire_whoosh.mp3')
        self.cough_sound.set_volume(0.2)

        for i in range(1, 15):
            path = f"../Assets/sprites/scene4/fireboy/b{i}.png"
            img = pygame.image.load(path).convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            if i < 6:
                self.idle.append(scaled_img)
            else:
                self.working.append(scaled_img)

        self.frame = 0
        self.image = self.idle[self.frame]
        self.rect = self.image.get_rect()
        self.rect.inflate(50,50)
        self.rect.bottomleft = (self.x, self.y)
    
    def update(self):
        # Update prev_state
        self.prev_state = self.curr_state
        
        # Update the sprite based on the image index
        if self.curr_state == 0:
            self.image = self.idle[int(self.frame)]
        if self.curr_state == 1:
            self.image = self.working[int(self.frame)]
            self.cough_sound.play()
        
        # Move to the next frame
        if self.curr_state == 0:
            if self.frame < 4:
                self.frame += 0.2
            else: self.frame = 0

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

class BrokenPhone(pygame.sprite.Sprite):
    def __init__(self,x,y,worker_goup):
        super().__init__()
        self.x = x
        self.y = y

        self.motion_x = x
        self.motion_y = y

        self.speed = 4
        self.worker_group = worker_goup

        img = pygame.image.load("../Assets/sprites/scene4/junk/broken_phone.png").convert_alpha()
        scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
        self.image = scaled_img
        self.rect = self.image.get_rect()
        self.rect.inflate(50,50)
        self.rect.center = (self.x, self.y)

        self.fall_sound = pygame.mixer.Sound('../Assets/audio/scene4/fall.mp3')
        self.fall_sound.set_volume(0.5)

        self.dragging = False

    def update(self):
        global fallen_objects
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
            fallen_objects += 1
            self.kill()

class Flask(pygame.sprite.Sprite):
    def __init__(self,x,y,worker_goup):
        super().__init__()
        self.x = x
        self.y = y

        self.motion_x = x
        self.motion_y = y

        self.speed = 4
        self.worker_group = worker_goup

        img = pygame.image.load("../Assets/sprites/scene4/junk/flask.png").convert_alpha()
        scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
        self.image = scaled_img
        self.rect = self.image.get_rect()
        self.rect.inflate(50,50)
        self.rect.center = (self.x, self.y)

        self.fall_sound = pygame.mixer.Sound('../Assets/audio/scene4/fall.mp3')
        self.fall_sound.set_volume(0.5)

        self.dragging = False

    def update(self):
        global fallen_objects
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
            fallen_objects += 1
            self.kill()

class Motherboard(pygame.sprite.Sprite):
    def __init__(self,x,y,worker_goup):
        super().__init__()
        self.x = x
        self.y = y

        self.motion_x = x
        self.motion_y = y

        self.speed = 4
        self.worker_group = worker_goup

        img = pygame.image.load("../Assets/sprites/scene4/junk/motherboard.png").convert_alpha()
        scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
        self.image = scaled_img
        self.rect = self.image.get_rect()
        self.rect.inflate(50,50)
        self.rect.center = (self.x, self.y)

        self.fall_sound = pygame.mixer.Sound('../Assets/audio/scene4/fall.mp3')
        self.fall_sound.set_volume(0.5)

        self.dragging = False

    def update(self):
        global fallen_objects
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
            fallen_objects += 1
            self.kill()

class Chemical(pygame.sprite.Sprite):
    def __init__(self,x,y,worker_goup):
        super().__init__()
        self.x = x
        self.y = y

        self.motion_x = x
        self.motion_y = y

        self.speed = 4
        self.worker_group = worker_goup

        img = pygame.image.load("../Assets/sprites/scene4/junk/yellow_chem.png").convert_alpha()
        scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
        self.image = scaled_img
        self.rect = self.image.get_rect()
        self.rect.inflate(50,50)
        self.rect.center = (self.x, self.y)

        self.fall_sound = pygame.mixer.Sound('../Assets/audio/scene4/fall.mp3')
        self.fall_sound.set_volume(0.5)

        self.dragging = False

    def update(self):
        global fallen_objects
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
            fallen_objects += 1
            self.kill()

class Line(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = 4

        img = pygame.image.load("../Assets/sprites/scene4/line.png").convert_alpha()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.rect.centery < 540:
            self.rect.centery += self.speed
        else:
            self.kill()

pygame.init()

pause_img = pygame.image.load("../Assets/sprites/main_page/pause_button.png")
pause_img = pygame.transform.scale(pause_img,(30,30))
pause_img_rect = pause_img.get_rect(center=(760,30))
pause_box = pygame.image.load("../Assets/sprites/main_page/pause_box.png")
pause_box.set_alpha(200)
pause_size1 = 22
pause_size2 = 22
pause_size3 = 22
pause_text1 = "RESUME GAME"
pause_text2 = "RESTART GAME"
pause_text3 = "MAIN MENU"
pause_font1 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", pause_size1)
pause_font2 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", pause_size2)
pause_font3 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", pause_size3)
pause_button1 = pause_font1.render(pause_text1,True,(0,0,0))
pause_button2 = pause_font2.render(pause_text2,True,(0,0,0))
pause_button3 = pause_font3.render(pause_text3,True,(0,0,0))
pause_button1_rect = pause_button1.get_rect(center=(400,240))
pause_button2_rect = pause_button2.get_rect(center=(400,300))
pause_button3_rect = pause_button3.get_rect(center=(400,360))

# Set up the screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("../Assets/sprites/scene4/bg.png")
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
pygame.time.set_timer(timer,1500)

broken_phone_group = pygame.sprite.Group()

flask_group = pygame.sprite.Group()

motherboard_group = pygame.sprite.Group()

chemical_group = pygame.sprite.Group()

bg_audio = pygame.mixer.Sound("../Assets/audio/scene4/scene4_bg_audio.mp3")
bg_audio.set_volume(0.5)

# Define the color
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 30)
message = "Failed to Dispose: " + str(fallen_objects) + " / 10"
text_surface = font.render(message, True, (255, 255, 255))
text_rect = text_surface.get_rect(topleft=(15,15))


count = 0

message_over = False
start_time = time.time()

pause = False

bg_audio.play()

running = True

while running:
     
    
    if pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_button1_rect.collidepoint(event.pos):
                pygame.mixer.unpause()
                pause= False
            elif pause_button2_rect.collidepoint(event.pos):
                pygame.mixer.unpause()
                fallen_objects=0
                message_over=False
                start_time = time.time()
                for broken_phone in broken_phone_group:
                    broken_phone.kill()
                for motherboard in motherboard_group:
                    motherboard.kill()
                for flask in flask_group:
                    flask.kill()
                for chemical in chemical_group:
                    chemical.kill()
                pause = False
            elif pause_button3_rect.collidepoint(event.pos):
                exec(open("unlocked_home_page.py").read())   
        screen.blit(pause_box,(250,200))
        screen.blit(pause_button1,pause_button1_rect)
        screen.blit(pause_button2,pause_button2_rect)
        screen.blit(pause_button3,pause_button3_rect)     
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_img_rect.collidepoint(event.pos):
                    pygame.mixer.pause()
                    pause = True        

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
                total_objects += 1
                
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
                    
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > 32:
            message_over = True
                    
        if fallen_objects >= 10:
            pygame.mixer.stop()
            execute_failure()
            bg_audio.play()
            fallen_objects=0
            message_over=False
            start_time = time.time()
            for broken_phone in broken_phone_group:
                broken_phone.kill()
            for motherboard in motherboard_group:
                motherboard.kill()
            for flask in flask_group:
                flask.kill()
            for chemical in chemical_group:
                chemical.kill()
        if message_over == True:
            pygame.mixer.stop()
            running = False

        screen.blit(background,(0,0))
        message = "Failed to Dispose: " + str(fallen_objects) + " / 10" 
        text_surface = font.render(message, True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=(15,15))
        screen.blit(text_surface,text_rect)
        screen.blit(pause_img,pause_img_rect)

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

