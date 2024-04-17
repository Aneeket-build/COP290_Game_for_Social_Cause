import pygame
import sys
import random
import math


# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Title")

play_hover_sound = pygame.mixer.Sound("play_hover_sound.mp3")



# Load the background image
background = pygame.image.load("main.jpg")
background = pygame.transform.scale(background, (800, 600))

# Load the font
font = pygame.font.Font("play_font.ttf", 45)

screen_name = "home page"

# Initial text size and button rectangle
text_size = 55
play_text = "PLAY"
play_button = font.render(play_text, True, (0, 0, 0))
play_button_rect = play_button.get_rect(center=(400, 400))

pause = 0




clock = pygame.time.Clock()





running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if screen_name=="home page":
        if event.type == pygame.MOUSEMOTION:
            # Check if the mouse is over the button and increase text size
            if play_button_rect.collidepoint(event.pos):
                text_size = 70  # Increase text size
                if(pause==0):
                    play_hover_sound.play()
                    pause+=1
            else:
                text_size = 55  # Reset text size
                pause=0
        if event.type == pygame.MOUSEBUTTONDOWN and screen_name=="home page":
            # Check if the mouse click is within the button rectangle
            if play_button_rect.collidepoint(event.pos):
                screen_name = "page 1"
            # Draw the background
        screen.blit(background, (0, 0))

        # Re-render the button with the updated text size
        font = pygame.font.Font("play_font.ttf", text_size)
        play_button = font.render(play_text, True, (0, 0, 0))
        play_button_rect = play_button.get_rect(center=(400, 400))
        # Draw the "PLAY" button
        screen.blit(play_button,play_button_rect)
    elif screen_name=="page 1":
        exec(open("factory.py").read())
        

    elif screen_name=="game3":
        exec(open("throw.py").read())
    
    elif screen_name=="descent":
        exec(open("doom.py").read())

    elif screen_name=="test":
        exec(open("throw.py").read())


    # Update the display
    pygame.display.flip()
    clock.tick(30)
