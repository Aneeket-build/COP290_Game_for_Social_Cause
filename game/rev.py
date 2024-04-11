import pygame
import sys
import random

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Title")

play_hover_sound = pygame.mixer.Sound("play_hover_sound.mp3")
caught_sound = pygame.mixer.Sound("caught.wav")
dead_sound = pygame.mixer.Sound("dead_sound.wav")
bounce_sound = pygame.mixer.Sound("bounce_sound.mp3")
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

sprite_img_fall = pygame.image.load("fall.png")
trampoline_img = pygame.image.load("trampoline.png")
sprite_img_bounce = pygame.image.load("bounce.png")
sprite_img_stand = pygame.image.load("stand.png")
sprite1 = pygame.image.load("fall-turn1.png")
sprite_dead = pygame.image.load("dead.png")
sprite_fall1 = pygame.image.load("fall1.png")
sprite_fall2 = pygame.image.load("fall2.png")
sprite_fall3 = pygame.image.load("fall3.png")
sprite_fall4 = pygame.image.load("fall4.png")

# Set up the game objects
sprites = []
trampoline_rect = trampoline_img.get_rect(midbottom=(WIDTH // 2, HEIGHT))

# Set up game variables
trampoline_speed = 10
score = 0

clock = pygame.time.Clock()

def create_sprite():
    return sprite_img_fall.get_rect(topleft=(random.randint(75, WIDTH - sprite_img_fall.get_width()-75), 140-sprite_img_fall.get_height()))

def draw_score():
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Game loop
while True:
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
                background = pygame.image.load("factory bg.jpg")
                background = pygame.transform.scale(background, (800, 600))
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
        screen.blit(background, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and trampoline_rect.x >0:
            trampoline_rect.x -= trampoline_speed
        if keys[pygame.K_RIGHT] and trampoline_rect.x< (WIDTH-trampoline_rect.width):
            trampoline_rect.x += trampoline_speed

        # Update sprite positions
        for sprite_rect in sprites:
            if sprite_rect[1]==2:
                sprite_rect[0].y += ((2*sprite_rect[2]+1)/50)
                sprite_rect[2]+=1
                if sprite_rect[0].colliderect(trampoline_rect):
                    sprite_rect[1]=6
                    caught_sound.play()
                    score += 1
                elif sprite_rect[0].y > HEIGHT - sprite_img_fall.get_height():
                    sprite_rect[1]=5
                    dead_sound.play()
            elif sprite_rect[1]==0:
                sprite_rect[0].y += (2+((2*sprite_rect[2]-1)/50))
                sprite_rect[2]+=1
                if sprite_rect[0].colliderect(trampoline_rect):
                    bounce_sound.play()
                    sprite_rect[1] = 1
                elif sprite_rect[0].y > HEIGHT- sprite_img_fall.get_height():
                    sprite_rect[1]=5
                    dead_sound.play()
            elif sprite_rect[1] == 1:
                if sprite_rect[2]>1:
                    sprite_rect[0].y -= (((2*sprite_rect[2]-1)/50))
                    sprite_rect[2]-=1
                else:
                    sprite_rect[1]=2  
            elif sprite_rect[1] == -1:
                if sprite_rect[3]<30:
                    sprite_rect[3]+=1
                else:
                    sprite_rect[3] = 0
                    sprite_rect[1]=0   
            elif sprite_rect[1]==5:
                if sprite_rect[3]<60:
                    sprite_rect[3]+=1
                else:
                    sprites.remove(sprite_rect)   
                    sprite_rect[3] = 0            
            elif sprite_rect[1]==6:
                if sprite_rect[3] < 50:
                    sprite_rect[3]+=1
                else:
                    sprites.remove(sprite_rect)
                    sprite_rect[3] = 0    
        # Generate a new sprite if needed
        if len(sprites) < 2:
            sprites.append([create_sprite(),-1,3,0])

        # Draw game objects
        for sprite_rect in sprites:
            if sprite_rect[1]==1:
                if sprite_rect[2]<=10 or sprite_rect[2]>=95:
                    screen.blit(sprite1, sprite_rect[0])
                else:    
                    screen.blit(sprite_img_bounce, sprite_rect[0])
            elif sprite_rect[1]==-1:
                screen.blit(sprite_img_stand, sprite_rect[0])
            elif sprite_rect[1]==5:
                screen.blit(sprite_dead,sprite_rect[0])    
            elif sprite_rect[1]==6:
                if sprite_rect[3]<10:
                    screen.blit(sprite_fall1,sprite_rect[0])  
                elif sprite_rect[3]<20:
                    screen.blit(sprite_fall2,sprite_rect[0])  
                elif sprite_rect[3]<30:
                    screen.blit(sprite_fall3,sprite_rect[0])  
                else:
                    screen.blit(sprite_fall4,sprite_rect[0])  
            else:
                screen.blit(sprite_img_fall, sprite_rect[0])
        screen.blit(trampoline_img, trampoline_rect)

        draw_score()

    # Update the display
    pygame.display.flip()
    clock.tick(60)
