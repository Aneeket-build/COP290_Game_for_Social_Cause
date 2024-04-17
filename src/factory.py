import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg_audio_2 = pygame.mixer.Sound("../Assets/audio/scene2/scene2_audio.wav")

caught_sound = pygame.mixer.Sound("../Assets/audio/scene2/caught.wav")
caught_sound.set_volume(0.2)
dead_sound = pygame.mixer.Sound("../Assets/audio/scene2/dead_sound.wav")
bounce_sound = pygame.mixer.Sound("../Assets/audio/scene2/bounce_sound.mp3")

bg_game2 = pygame.image.load("../Assets/sprites/scene2/factory bg.jpg")

sprite_img_fall = pygame.image.load("../Assets/sprites/scene2/fall.png")
trampoline_img = pygame.image.load("../Assets/sprites/scene2/trampoline.png")
sprite_img_bounce = pygame.image.load("../Assets/sprites/scene2/bounce.png")
sprite_img_stand = pygame.image.load("../Assets/sprites/scene2/stand.png")
sprite1 = pygame.image.load("../Assets/sprites/scene2/fall-turn1.png")
sprite_dead = pygame.image.load("../Assets/sprites/scene2/dead.png")
sprite_fall1 = pygame.image.load("../Assets/sprites/scene2/fall1.png")
sprite_fall2 = pygame.image.load("../Assets/sprites/scene2/fall2.png")
sprite_fall3 = pygame.image.load("../Assets/sprites/scene2/fall3.png")
sprite_fall4 = pygame.image.load("../Assets/sprites/scene2/fall4.png")

sprites = []
trampoline_rect = trampoline_img.get_rect(midbottom=(WIDTH // 2, HEIGHT))

trampoline_speed = 10
score = 0
neg_score =0

clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)
message = "Use left and right arrow keys to save the workers."
text_surface = font.render(message, True, (255, 255, 255))
text_rect = text_surface.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.top = 15

def create_sprite():
    return sprite_img_fall.get_rect(topleft=(random.randint(75, WIDTH - sprite_img_fall.get_width()-75), 140-sprite_img_fall.get_height()))

bg_audio_2.play()

running = True

while running:
    screen.blit(bg_game2, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and trampoline_rect.x >0:
        trampoline_rect.x -= trampoline_speed
    if keys[pygame.K_RIGHT] and trampoline_rect.x< (WIDTH-trampoline_rect.width):
        trampoline_rect.x += trampoline_speed

    for sprite_rect in sprites:
        if sprite_rect[1]==2:
            sprite_rect[0].y += ((2*sprite_rect[2]+1)/10)
            sprite_rect[2]+=1
            if sprite_rect[0].colliderect(trampoline_rect):
                sprite_rect[1]=6
                caught_sound.play()
                score += 1
            elif sprite_rect[0].y > HEIGHT - sprite_img_fall.get_height():
                sprite_rect[1]=5
                dead_sound.play()
                neg_score+=1
        elif sprite_rect[1]==0:
            sprite_rect[0].y += (2+((2*sprite_rect[2]-1)/10))
            sprite_rect[2]+=1
            if sprite_rect[0].colliderect(trampoline_rect):
                bounce_sound.play()
                sprite_rect[1] = 1
            elif sprite_rect[0].y > HEIGHT- sprite_img_fall.get_height():
                sprite_rect[1]=5
                dead_sound.play()
                neg_score+=1
        elif sprite_rect[1] == 1:
            if sprite_rect[2]>1:
                sprite_rect[0].y -= (((2*sprite_rect[2]-1)/10))
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

    if len(sprites) < 2:
        sprites.append([create_sprite(),-1,3,0])

    for sprite_rect in sprites:
        if sprite_rect[1]==1:
            if sprite_rect[2]<=10 or sprite_rect[2]>=500:
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

    screen.blit(text_surface, text_rect)

    if score+neg_score==8:
        if score>5:
            running = False
            exec(open("throw.py").read())
        else:
            running = False
            exec(open("rev.py").read())    
    

    pygame.display.flip()
    clock.tick(30)
