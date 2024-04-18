import pygame
from pygame.locals import *

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load background images
bg1 = pygame.image.load("../Assets/sprites/scene4/bg.png").convert()
bg2 = pygame.image.load("../Assets/sprites/scene1/bg.png").convert()

# Position off-screen to the left
bg2_x = -800

# Transition duration in frames
transition_duration = 60
transition_progress = 0
transition_started = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            # Start transition on left mouse click
            transition_started = True
            transition_progress = 0  # Reset transition progress

    # Clear the screen
    screen.fill((0, 0, 0))

    if not transition_started:
        # Display bg1
        screen.blit(bg1, (0, 0))
        pygame.display.flip()
        clock.tick(60)
        continue

    # Update transition progress
    transition_progress += 1
    if transition_progress > transition_duration:
        break

    # Calculate position of bg2
    bg2_x = -800 + int(800 * (transition_progress / transition_duration))

    # Draw bg1 and sliding bg2
    screen.blit(bg1, (0, 0))
    screen.blit(bg2, (bg2_x, 0))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
