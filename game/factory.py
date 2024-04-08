import pygame
import random
import sys

# Initialize Pygame
pygame.init()

bg = pygame.image.load("factory bg.jpg")

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Sprite")

# Load images
sprite_img = pygame.image.load("fall.png")
trampoline_img = pygame.image.load("trampoline.png")

# Set up the game objects
sprites = []
trampoline_rect = trampoline_img.get_rect(midbottom=(WIDTH // 2, HEIGHT))

# Set up game variables
trampoline_speed = 5
score = 0

clock = pygame.time.Clock()

def create_sprite():
    return sprite_img.get_rect(topleft=(random.randint(75, WIDTH - sprite_img.get_width()-75), 180-sprite_img.get_height()))

def draw_score():
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Game loop
while True:
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and trampoline_rect.x >0:
        trampoline_rect.x -= trampoline_speed
    if keys[pygame.K_RIGHT] and trampoline_rect.x< (WIDTH-trampoline_rect.width):
        trampoline_rect.x += trampoline_speed

    # Update sprite positions
    for sprite_rect in sprites:
        sprite_rect.y += 3
        if sprite_rect.colliderect(trampoline_rect):
            sprites.remove(sprite_rect)
            score += 1
        elif sprite_rect.y > HEIGHT:
            sprites.remove(sprite_rect)

    # Generate a new sprite if needed
    if len(sprites) < 3:
        sprites.append(create_sprite())

    # Draw game objects
    for sprite_rect in sprites:
        screen.blit(sprite_img, sprite_rect)
    screen.blit(trampoline_img, trampoline_rect)

    draw_score()

    pygame.display.flip()
    clock.tick(60)
