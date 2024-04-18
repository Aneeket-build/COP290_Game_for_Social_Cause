import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Title")

play_hover_sound = pygame.mixer.Sound("../Assets/audio/main_page/play_hover_sound.mp3")

background = pygame.image.load("../Assets/sprites/main_page/main.jpg")
background = pygame.transform.scale(background, (800, 600))

font = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", 45)

screen_name = "home page"

text_size = 55
play_text = "PLAY"
play_button = font.render(play_text, True, (0, 0, 0))
play_button_rect = play_button.get_rect(center=(400, 400))

pause = 0

clock = pygame.time.Clock()

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEMOTION:
        if play_button_rect.collidepoint(event.pos):
            text_size = 70 
            if(pause==0):
                play_hover_sound.play()
                pause+=1
        else:
            text_size = 55
            pause=0
    if event.type == pygame.MOUSEBUTTONDOWN:
        if play_button_rect.collidepoint(event.pos):
            running = False
            exec(open("mining.py").read())

    screen.blit(background, (0, 0))

    font = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size)
    play_button = font.render(play_text, True, (0, 0, 0))
    play_button_rect = play_button.get_rect(center=(400, 400))
    screen.blit(play_button,play_button_rect)

    pygame.display.flip()
    clock.tick(30)

