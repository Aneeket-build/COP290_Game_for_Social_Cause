import pygame
import random
import sys

def execute_failure():
    with open('failure.py', 'r') as file:
        code = file.read()
    exec(code)

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# bg_audio_3 = pygame.mixer.Sound("../Assets/audio/scene3/scene3_audio.wav")
# bg_audio_3.set_volume(5)
bg_audio = pygame.mixer.Sound("../Assets/audio/scene2/scene2_bg_audio.mp3")
bg_audio.set_volume(0.4)

caught_sound = pygame.mixer.Sound("../Assets/audio/scene2/caught.wav")
caught_sound.set_volume(0.2)
dead_sound = pygame.mixer.Sound("../Assets/audio/scene2/dead_sound.wav")
bounce_sound = pygame.mixer.Sound("../Assets/audio/scene2/bounce_sound.mp3")
bounce_sound.set_volume(0.4)

bg_game2 = pygame.image.load("../Assets/sprites/scene2/factory bg.jpg")

pause_img = pygame.image.load("../Assets/sprites/main_page/pause_button.png")
pause_img = pygame.transform.scale(pause_img,(30,30))
pause_img_rect = pause_img.get_rect(center=(760,30))
pause_box = pygame.image.load("../Assets/sprites/main_page/pause_box.png")
pause_box.set_alpha(200)
pause_size1 = 22
pause_size2 = 22
pause_size3 = 22
pause_text1 = "RESUME GAME"
pause_text2 = "RESTART GAME"
pause_text3 = "MAIN MENU"
pause_font1 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", pause_size1)
pause_font2 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", pause_size2)
pause_font3 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", pause_size3)
pause_button1 = pause_font1.render(pause_text1,True,(0,0,0))
pause_button2 = pause_font2.render(pause_text2,True,(0,0,0))
pause_button3 = pause_font3.render(pause_text3,True,(0,0,0))
pause_button1_rect = pause_button1.get_rect(center=(400,240))
pause_button2_rect = pause_button2.get_rect(center=(400,300))
pause_button3_rect = pause_button3.get_rect(center=(400,360))


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

# pause_rect = pygame.Rect()

trampoline_speed = 15
score = 0
neg_score =0

clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)
message = "Working Hands Saved: " + str(2*score) + " / " + str(2*(score+neg_score)) 
text_surface = font.render(message, True, (255, 255, 255))
text_rect = text_surface.get_rect(topleft=(15,15))

pause = False

last_spawned =0

bg_audio.play()

running = True

while running:
    screen.blit(bg_game2, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if pause:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_button1_rect.collidepoint(event.pos):
                pygame.mixer.unpause()
                pause= False
            elif pause_button2_rect.collidepoint(event.pos):
                sprites = []
                score=0
                neg_score=0
                pygame.mixer.unpause()
                pause = False
            elif pause_button3_rect.collidepoint(event.pos):
                exec(open("unlocked_home_page.py").read())    
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
        screen.blit(pause_box,(250,200))
        screen.blit(pause_button1,pause_button1_rect)
        screen.blit(pause_button2,pause_button2_rect)
        screen.blit(pause_button3,pause_button3_rect)
    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_img_rect.collidepoint(event.pos):
                pygame.mixer.pause()
                pause = True        

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

        if len(sprites) < 3:
            temp = random.randint(1,100)
            if temp>97:
                launch_at = random.randint(75, WIDTH - sprite_img_fall.get_width()-75)
                if abs(launch_at-last_spawned)>100:
                    sprites.append([sprite_img_fall.get_rect(topleft=(launch_at, 140-sprite_img_fall.get_height()))
            ,-1,3,0])
                    last_spawned = launch_at

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
        message = "Working Hands Saved: " + str(2*score) + " / " + str(2*(score+neg_score))
        if score/(score+neg_score+1) >= 0.55 : 
            text_surface = font.render(message, True, (0,255,0))
        else:
            text_surface = font.render(message, True, (255,0,0))
        text_rect = text_surface.get_rect(center=(150,15))
        screen.blit(text_surface, text_rect)
        screen.blit(pause_img,pause_img_rect)

        if score+neg_score==12:
            if score>7:
                pygame.mixer.stop()
                running = False
                # bg_audio_3.play()
                # exec(open("throw.py").read())
            else:
                pygame.mixer.pause()
                execute_failure()
                bg_audio.play()
                sprites = []
                score=0
                neg_score=0  
    

    pygame.display.flip()
    clock.tick(30)
