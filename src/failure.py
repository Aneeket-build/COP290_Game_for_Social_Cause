import pygame
import math
from sys import exit

class Face(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.speaking = []
        self.silent = []
        self.frame = 0
        self.state = 0
        self.speaking_frames = 0
        self.blinking_frames = 0
        for i in range(1, 6):
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
        elif self.state == 1:
            self.image = self.silent[int(self.frame)]

        # Move to the next frame
        if self.state == 0:
            if self.frame < 3:
                if self.speaking_frames < 104:
                    self.frame += 0.2
                    self.speaking_frames += 1
                else:
                    self.state = 1
                    self.frame = 0
            else:
                self.frame = 0
        elif self.state == 1:
            if self.frame < 1:
                self.frame += 0.015
            else:
                self.frame = 0

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("../Assets/sprites/face/main.png")
pygame.display.set_caption('TOXIC TECH')
clock = pygame.time.Clock()
play_hover_sound = pygame.mixer.Sound("../Assets/audio/main_page/play_hover_sound.mp3")
font = pygame.font.Font("../Assets/fonts/play_font.ttf", 45)

faces = pygame.sprite.GroupSingle()
faces.add(Face(521, 108))

bg_music = pygame.mixer.Sound('../Assets/audio/face/failure1.wav')
bg_music.play()

text_size = 25
text_size2 =25
text = "TRY AGAIN"
text2 = "MAIN MENU"
play_button = font.render(text, True, (0, 0, 0))
play_button_rect = play_button.get_rect(center=(400, 400))
return_button = font.render(text2,True,(0,0,0))
return_button_rect = return_button.get_rect(center=(400,135))

pause = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if play_button_rect.collidepoint(event.pos):
                text_size = 20
                if pause == 0:
                    play_hover_sound.play()
                    pause += 1
            elif return_button_rect.collidepoint(event.pos):
                text_size2 = 20
                if pause==0:
                    play_hover_sound.play()
                    pause+=1        
            else:
                text_size = 25
                text_size2 = 25
                pause = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                pygame.mixer.stop()
                running=False
            elif return_button_rect.collidepoint(event.pos):
                pygame.mixer.stop()
                exec(open("unlocked_home_page.py").read())    
        
    screen.blit(background, (0, 0))
    font = pygame.font.Font("../Assets/fonts/play_font.ttf", text_size)
    font2 = pygame.font.Font("../Assets/fonts/play_font.ttf", text_size2)
    faces.draw(screen)
    faces.update()

    play_button = font.render(text, True, (255, 255, 255))
    play_button_rect = play_button.get_rect(center=(400, 470))
    screen.blit(play_button, play_button_rect)
    return_button = font2.render(text2,True,(255,255,255))
    return_button_rect = return_button.get_rect(center=(400,135))
    screen.blit(return_button,return_button_rect)
    
    pygame.display.update()
    clock.tick(25)