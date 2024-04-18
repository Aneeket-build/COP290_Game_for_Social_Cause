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
                if self.speaking_frames < 106:
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

play_hover_sound = pygame.mixer.Sound("../Assets/audio/main_page/play_hover_sound.mp3")

font = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", 45)
text = "ULTRAREASLISTIC MODE"
text_size = 20
play_button = font.render(text, True, (0, 0, 0))
play_button_rect = play_button.get_rect(center=(400, 400))

faces = pygame.sprite.GroupSingle()
faces.add(Face(521,108))
bg_music = pygame.mixer.Sound('../Assets/audio/face/cycle1.wav')
bg_music.set_volume(0.2)
bg_music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        screen.blit(background,(0,0))

        if event.type == pygame.MOUSEMOTION:
            if play_button_rect.collidepoint(event.pos):
                text_size = 20
                if pause == 0:
                    play_hover_sound.play()
                    pause += 1
            else:
                text_size = 25
                pause = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                pass
    faces.draw(screen)
    faces.update()

    font = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size)
    play_button = font.render(text, True, (255, 255, 255))
    play_button_rect = play_button.get_rect(center=(400, 470))
    screen.blit(play_button, play_button_rect)

    pygame.display.update()
    clock.tick(25)



