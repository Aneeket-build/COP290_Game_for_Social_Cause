import pygame
import sys
import math
from random import randint
import subprocess

def execute_level(file_name):
    with open(file_name, 'r') as file:
        code = file.read()
    exec(code,globals(),locals())  

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Title")

play_hover_sound = pygame.mixer.Sound("../Assets/audio/main_page/play_hover_sound.mp3")
locked_sound = pygame.mixer.Sound("../Assets/audio/main_page/locked_sound.wav")
story_msg = pygame.mixer.Sound('../Assets/audio/scene1/story13.wav')
bg_audio2 = pygame.mixer.Sound("../Assets/audio/scene2/scene2_audio.wav")
bg_audio3 = pygame.mixer.Sound("../Assets/audio/scene3/scene3_audio.wav")
bg_audio4 = pygame.mixer.Sound('../Assets/audio/scene4/scene4_audio.wav')



background = pygame.image.load("../Assets/sprites/main_page/main.jpg")
background = pygame.transform.scale(background, (800, 600))
lock_img = pygame.image.load("../Assets/sprites/main_page/lock.png")
lock_img = pygame.transform.scale(lock_img,(40,40))

font = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", 45)

screen_name = "home page"

text_size = 25
text_size2 = 25
play_text = "Story Mode"
free_play_text = "Free Play"

pause = 0

clock = pygame.time.Clock()

running = True


font = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size)
play_button = font.render(play_text, True, (0, 0, 0))
play_button_rect = play_button.get_rect(center=(400, 350))
font2 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size2)
free_play_button = font2.render(free_play_text,True,(0,0,0))
free_play_button_rect = free_play_button.get_rect(center=(420,415))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEMOTION:
        if play_button_rect.collidepoint(event.pos):
            text_size = 30
            if(pause==0):
                play_hover_sound.play()
                pause+=1
        elif free_play_button_rect.collidepoint(event.pos):
            text_size2 = 27
            if(pause==0):
                locked_sound.play()
                pause+=1        
        else:
            text_size = 25
            text_size2 = 25
            pause=0
    if event.type == pygame.MOUSEBUTTONDOWN:
        if play_button_rect.collidepoint(event.pos):
            story_msg.play()
            execute_level("scene1.py")
            bg_audio2.play()
            execute_level("factory.py")
            bg_audio3.play()
            execute_level("throw.py")
            bg_audio4.play()
            execute_level("scene4.py")
            execute_level("doom.py")
            exec(open("unlocked_home_page.py").read())
            
            

    screen.blit(background, (0, 0))
    screen.blit(lock_img,(285,390))

    font = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size)
    play_button = font.render(play_text, True, (0, 0, 0))
    play_button_rect = play_button.get_rect(center=(400, 350))
    screen.blit(play_button,play_button_rect)
    font2 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size2)
    free_play_button = font2.render(free_play_text,True,(0,0,0))
    free_play_button_rect = free_play_button.get_rect(center=(420,415))
    screen.blit(free_play_button,free_play_button_rect)

    pygame.display.flip()
    clock.tick(30)

