import pygame
import sys

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Black Horizontal Line")

# Define the color
BLACK = (0, 0, 0)

# Draw the black horizontal line
start_pos = (100, 100)  # Starting position of the line
end_pos = (start_pos[0] + 50, start_pos[1])  # Ending position of the line
line_thickness = 2  # Thickness of the line
pygame.draw.line(screen, BLACK, start_pos, end_pos, line_thickness)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
