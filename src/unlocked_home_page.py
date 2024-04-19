import pygame
import sys
import math
from random import randint
import msg

def execute_level(file_name):
    with open(file_name, 'r') as file:
        code = file.read()
    exec(code,globals(),locals())  

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Title")

play_hover_sound = pygame.mixer.Sound("../Assets/audio/main_page/play_hover_sound.mp3")

background = pygame.image.load("../Assets/sprites/main_page/main.jpg")
background = pygame.transform.scale(background, (800, 600))
screen_img = pygame.image.load("../Assets/sprites/main_page/phone_screen.png")

text_size = 29
text_size2 = 29
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
free_play_button_rect = free_play_button.get_rect(center=(400,415))

start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEMOTION:
        if play_button_rect.collidepoint(event.pos):
            text_size = 25
            if(pause==0):
                play_hover_sound.play()
                pause+=1
        elif free_play_button_rect.collidepoint(event.pos):
            text_size2 = 25
            if(pause==0):
                play_hover_sound.play()
                pause+=1        
        else:
            text_size = 29
            text_size2 = 29
            pause=0
            
    current_time = pygame.time.get_ticks()  
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        if play_button_rect.collidepoint(event.pos) and (current_time-start_time)>1000:
            execute_level("welcome.py")
            msg.set_message(1)
            execute_level("scene1.py")
            pygame.mixer.stop()
            msg.set_message(2)
            execute_level("scene2.py")
            pygame.mixer.stop()
            msg.set_message(3)
            execute_level("scene3.py")
            pygame.mixer.stop()
            msg.set_message(4)
            execute_level("scene4.py")
            pygame.mixer.stop()
            execute_level("cycle.py")
            execute_level("doom.py")
        elif free_play_button_rect.collidepoint(event.pos) and (current_time-start_time)>1000:
            running = False    
            exec(open("choose_game.py").read())

    screen.blit(background, (0, 0))
    screen.blit(screen_img,(271,108))
    font = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size)
    play_button = font.render(play_text, True, (0, 0, 0))
    play_button_rect = play_button.get_rect(center=(400, 350))
    screen.blit(play_button,play_button_rect)
    font2 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size2)
    free_play_button = font2.render(free_play_text,True,(0,0,0))
    free_play_button_rect = free_play_button.get_rect(center=(400,415))
    screen.blit(free_play_button,free_play_button_rect)

    pygame.display.flip()
    clock.tick(30)

