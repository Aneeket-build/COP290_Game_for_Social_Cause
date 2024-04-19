import pygame
from sys import exit
from random import randint, choice
import time

def execute_failure():
    with open('failure.py', 'r') as file:
        code = file.read()
    exec(code)


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

        self.dig_sound = pygame.mixer.Sound('../Assets/audio/scene1/dig2.wav')
        self.dig_sound.set_volume(0.9)
        
        for i in range(0, 13):
            path = f"../Assets/sprites/scene1/s{i}.png"
            img = pygame.image.load(path).convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            if self.is_inverted == False:
                sprite = scaled_img
            else:
                sprite = pygame.transform.flip(scaled_img, True, False)
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
                if abs(worker.rect.centery -45 - self.rect.centery) <= 20:
                    print("touch")
                    worker.curr_state = 0
                else:
                    print("no touch")
                    # print(f"Soldier rect: {self.rect.centerx}, {self.rect.centery}")
                    # print(f"Worker rect: {worker.rect.centerx}, {worker.rect.centery}")


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
            self.dig_sound.play()
            # print("curr_state: "+ str(self.curr_state))
            # print("frame: "+str(self.frame))
                    
    def move_towards(self):
        if self.rect.centery < self.target_y:
            self.rect.centery += self.speed
        else:
            self.curr_state = 3
            self.frame = 0
            self.dig_sound.play()
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
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            if self.is_inverted == False:
                sprite = scaled_img
            else:
                sprite = pygame.transform.flip(scaled_img, True, False)
            self.working.append(sprite)
        for i in range(2,-1,-1):
            self.working.append(self.working[i])        
        
        for i in range(0,3):
            path = f"../Assets/sprites/scene1/t{i}.png"
            img = pygame.image.load(path).convert_alpha()
            scaled_img = pygame.transform.scale(img, (img.get_width()/2, img.get_height()/2))
            if self.is_inverted == True:
                sprite = scaled_img
            else:
                sprite = pygame.transform.flip(scaled_img, True, False)
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
background = pygame.image.load("../Assets/sprites/scene1/bg.png")
pygame.display.set_caption('Congo')
clock = pygame.time.Clock()
story_msg = pygame.mixer.Sound('../Assets/audio/scene1/story13.wav')
# story_msg.play()
bg_music = pygame.mixer.Sound('../Assets/audio/scene1/happy1.wav')
bg_music.set_volume(0.2)
# bg_music.play()
# bg_music = pygame.mixer.Sound('')
# bg_music.play(loops = -1)

font = pygame.font.Font(None, 30)
message = "Click on those tired bastards to keep them digging "
text_surface = font.render(message, True, (255, 255, 255))
text_rect = text_surface.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.top = 20 
# Groups

worker_group_left = pygame.sprite.Group()
worker_group_right = pygame.sprite.Group()

workers_left = [Worker(375,550),Worker(375,450),Worker(375,350),Worker(375,250),Worker(375,150)]
workers_right = [Worker(425,550,is_inverted=True),Worker(425,450,is_inverted=True),Worker(425,350,is_inverted=True),Worker(425,250,is_inverted=True),Worker(425,150,is_inverted=True)]

workers_combined = workers_left + workers_right

for worker in workers_left:
    worker_group_left.add(worker)
for worker in workers_right:
    worker_group_right.add(worker)

soldier_group = pygame.sprite.Group()
soldier_left = Soldier(200,500,worker_group_left,is_inverted=True)
soldier_right = Soldier(600,500,worker_group_right)
soldier_group.add(soldier_left)
soldier_group.add(soldier_right)

start_time = time.time()
message_over = False

pause = False

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
                for worker in workers_combined:
                    worker.curr_state = 0
                    worker.frame = randint(0,3)
                message_over=False
                start_time = time.time()
                pause = False
            elif pause_button3_rect.collidepoint(event.pos):
                exec(open("unlocked_home_page.py").read())   
        screen.blit(pause_box,(250,200))
        screen.blit(pause_button1,pause_button1_rect)
        screen.blit(pause_button2,pause_button2_rect)
        screen.blit(pause_button3,pause_button3_rect)     
    else:
        
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > 38:
            message_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pause_img_rect.collidepoint(event.pos):
                    pygame.mixer.pause()
                    pause = True        
                else:
                    target_x, target_y = pygame.mouse.get_pos()
                    if target_x < 400:
                        for worker in worker_group_left:
                            larger_rect = worker.rect.inflate(100, 0)
                            if larger_rect.collidepoint(target_x, target_y):
                                soldier_left.set_target(worker.rect.centerx , worker.rect.centery-45)
                                print("Target x: " + str(soldier_left.target_x))
                                print("Target y: " + str(soldier_left.target_y))
                    else:
                        for worker in worker_group_right:
                            larger_rect = worker.rect.inflate(100, 0)
                            if larger_rect.collidepoint(target_x, target_y):
                                soldier_right.set_target(worker.rect.centerx, worker.rect.centery-45)
            
        tired_count = 0
        for worker in workers_combined:
            tired_count += worker.curr_state
        if message_over == True:
            if tired_count > 4 :
                pygame.mixer.stop()
                execute_failure()
                for worker in workers_combined:
                    worker.curr_state = 0
                    worker.frame = randint(0,3)
                message_over=False
                start_time = time.time()
            else:
                pygame.mixer.stop()
                running = False        
            
        # screen.fill((255, 255, 255))
        screen.blit(background,(0,0))
        soldier_group.draw(screen)    
        soldier_group.update()

        screen.blit(text_surface, text_rect)
        screen.blit(pause_img,pause_img_rect)

        worker_group_left.draw(screen)
        worker_group_left.update()
        
        worker_group_right.draw(screen)
        worker_group_right.update()
    
    pygame.display.update()
    clock.tick(25)


