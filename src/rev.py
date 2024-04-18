import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Title")


screen_name = "home page"


clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if screen_name=="home page":
        exec(open("home_page_locked.py").read())

    elif screen_name=="page 1":
        exec(open("factory.py").read())
        
    elif screen_name=="game3":
        exec(open("throw.py").read())
    
    elif screen_name=="descent":
        exec(open("doom.py").read())

    pygame.display.flip()
    clock.tick(30)
