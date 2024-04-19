import pygame
import math
from sys import exit

class Face(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.speaking = []
        self.silent = []
        self.frame = 0
        self.state = 0
        self.speaking_frames = 0
        self.blinking_frames = 0

        for i in range(1,6):
            path = path = f"../Assets/sprites/face/f{i}.png"
            img = pygame.image.load(path).convert_alpha()
            if i < 4:
                self.speaking.append(img)
            else:
                self.silent.append(img)
        self.speaking.append(self.speaking[1])
        self.image = self.speaking[0]
        self.rect = self.image.get_rect()
        self.rect.topright = (x, y)
    
    def update(self):
        if self.state == 0:
            self.image = self.speaking[int(self.frame)]
        if self.state == 1:
            self.image = self.silent[int(self.frame)]

        # Move to the next frame
        if self.state == 0:
            # print("wow")
            if self.frame < 3:
                if self.speaking_frames < 144:
                    self.frame += 0.2
                    self.speaking_frames += 1
                else: 
                    self.state = 1
                    self.frame = 0
            else:
                self.frame = 0
        if self.state == 1:
            if self.frame < 1:
                self.frame += 0.015
            else:
                self.frame = 0
    
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("../Assets/sprites/face/main.png")
pygame.display.set_caption('Congo')
clock = pygame.time.Clock()

faces = pygame.sprite.GroupSingle()
faces.add(Face(521,108))
bg_music = pygame.mixer.Sound('../Assets/audio/face/hello_consumer1.wav')
bg_music.set_volume(0.5)
bg_music.play()

start_time = pygame.time.get_ticks()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(background,(0,0))

    current_time = pygame.time.get_ticks()

    if (current_time-start_time)>7000:
        running = False

    faces.draw(screen)
    faces.update()

    pygame.display.update()
    clock.tick(25)



