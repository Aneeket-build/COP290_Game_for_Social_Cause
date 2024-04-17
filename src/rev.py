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
bg_audio_2 = pygame.mixer.Sound("../Assets/audio/scene2/scene2_audio.wav")
bg_audio_3 = pygame.mixer.Sound("../Assets/audio/scene3/scene3_audio.wav")
caught_sound = pygame.mixer.Sound("../Assets/audio/scene2/caught.wav")
dead_sound = pygame.mixer.Sound("../Assets/audio/scene2/dead_sound.wav")
bounce_sound = pygame.mixer.Sound("../Assets/audio/scene2/bounce_sound.mp3")
hit_sound = pygame.mixer.Sound("../Assets/audio/scene3/hit.mp3")
catch_sound = pygame.mixer.Sound("../Assets/audio/scene3/phone_catch.mp3")
# Load the background image
background = pygame.image.load("main.jpg")
background = pygame.transform.scale(background, (800, 600))
bg_game2 = pygame.image.load("factory bg.jpg")
bg_game3 = pygame.image.load("bg_game3.png")

# Load the font
font = pygame.font.Font("play_font.ttf", 45)

screen_name = "home page"

# Initial text size and button rectangle
text_size = 55
play_text = "PLAY"
play_button = font.render(play_text, True, (0, 0, 0))
play_button_rect = play_button.get_rect(center=(400, 400))

pause = 0

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

stand_img = pygame.image.load('../Assets/sprites/scene3/thrower/img5.png')
throwup = pygame.image.load('../Assets/sprites/scene3/thrower/img2.png')
throwdown = pygame.image.load('../Assets/sprites/scene3/thrower/img3.png')
thrown = pygame.image.load('../Assets/sprites/scene3/thrower/img4.png')
pickup = pygame.image.load('../Assets/sprites/scene3/thrower/img1.png')
phone_img = pygame.image.load('../Assets/sprites/scene3/phone.png')
runner1 = pygame.image.load('../Assets/sprites/scene3/catcher/run1.png')
runner2 = pygame.image.load('../Assets/sprites/scene3/catcher/run2.png')
runner3 = pygame.image.load('../Assets/sprites/scene3/catcher/run3.png')
runner4 = pygame.image.load('../Assets/sprites/scene3/catcher/run4.png')
runner5 = pygame.image.load('../Assets/sprites/scene3/catcher/run5.png')
runner6 = pygame.image.load('../Assets/sprites/scene3/catcher/run6.png')
runner_hit = pygame.image.load('../Assets/sprites/scene3/catcher/hit.png')
runner_catch = pygame.image.load('../Assets/sprites/scene3/catcher/catch.png')

# Set up the game objects
sprites = []
trampoline_rect = trampoline_img.get_rect(midbottom=(WIDTH // 2, HEIGHT))

# Set up game variables
trampoline_speed = 10
score = 0
neg_score =0

clock = pygame.time.Clock()

def create_sprite():
    return sprite_img_fall.get_rect(topleft=(random.randint(75, WIDTH - sprite_img_fall.get_width()-75), 140-sprite_img_fall.get_height()))

def draw_score():
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

thrower_pos = (400, 75)
arm_stretched = False
throw_angle = 0

class Phone:
    def __init__(self, pos, angle):
        self.pos = pos
        self.angle = angle
        self.speed = 20
        self.image = pygame.transform.rotate(phone_img, angle)
        self.rect = self.image.get_rect(center=pos)

    def move(self):
        dx = math.cos(math.radians(self.angle)) * self.speed
        dy = math.sin(math.radians(self.angle)) * self.speed
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)
        self.rect.center = self.pos

# Enemy class
class Customer:
    def __init__(self, pos):
        self.pos = pos
        self.speed = 4
        self.image1 = runner1
        self.rect = self.image1.get_rect(center=pos)

    def move(self):
        self.pos = (self.pos[0], self.pos[1] - self.speed)
        self.rect.center = self.pos

phones = []
runners = []
runners_hit = []
runners_catch = []
thrower = 0

last_spawned = 0
last_to_last_spawned = 0

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
                screen_name = "page 1"
                bg_audio_2.play()
            # Draw the background
        screen.blit(background, (0, 0))

        # Re-render the button with the updated text size
        font = pygame.font.Font("play_font.ttf", text_size)
        play_button = font.render(play_text, True, (0, 0, 0))
        play_button_rect = play_button.get_rect(center=(400, 400))
        # Draw the "PLAY" button
        screen.blit(play_button,play_button_rect)
    elif screen_name=="page 1":
        screen.blit(bg_game2, (0, 0))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and trampoline_rect.x >0:
            trampoline_rect.x -= trampoline_speed
        if keys[pygame.K_RIGHT] and trampoline_rect.x< (WIDTH-trampoline_rect.width):
            trampoline_rect.x += trampoline_speed

        # Update sprite positions
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
        # Generate a new sprite if needed
        if len(sprites) < 2:
            sprites.append([create_sprite(),-1,3,0])

        # Draw game objects
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
        if score+neg_score==8:
            if score>5:
                screen_name="game3"
                score=0
                neg_score=0
                bg_audio_3.play()
            else:
                score=0
                neg_score=0    
        

    elif screen_name=="game3":
        screen.blit(bg_game3,(0,0))

        if event.type == pygame.MOUSEBUTTONDOWN and not arm_stretched:
            arm_stretched = True
            mouse_start_pos = pygame.mouse.get_pos()
            thrower =1 

        elif event.type == pygame.MOUSEBUTTONUP and arm_stretched:
            arm_stretched = False
            mouse_end_pos = pygame.mouse.get_pos()
            dx = mouse_start_pos[0] - mouse_end_pos[0]
            dy = mouse_start_pos[1] - mouse_end_pos[1]
            throw_angle = math.degrees(math.atan2(dy, dx))
            phones.append(Phone(thrower_pos, throw_angle))
            thrower =2

        if thrower == 0:
            screen.blit(stand_img, (thrower_pos[0] - stand_img.get_width() // 2, thrower_pos[1] - stand_img.get_height() // 2)) 
        if thrower ==1:
            screen.blit(throwup, (thrower_pos[0] - throwup.get_width() // 2, thrower_pos[1] - throwup.get_height() // 2)) 
        elif thrower >1 :
            thrower+=1
            if thrower<10:
                screen.blit(throwdown, (thrower_pos[0] - throwdown.get_width() // 2, thrower_pos[1] - throwdown.get_height() // 2))
            elif thrower<20:
                screen.blit(thrown, (thrower_pos[0] - thrown.get_width() // 2, thrower_pos[1] - thrown.get_height() // 2))    
            else:
                thrower =0    

        if arm_stretched:
            pygame.draw.line(screen, (255,255,255), thrower_pos, pygame.mouse.get_pos(), 5)  

        for phone in phones:
            screen.blit(phone.image, phone.rect)

        for runner in runners:
            if runner[1]==1:
                screen.blit(runner1, runner[0].rect)
                runner[1]+=1
            elif runner[1]==2:
                screen.blit(runner2, runner[0].rect)
                runner[1]+=1
            elif runner[1]==3:
                screen.blit(runner3, runner[0].rect)
                runner[1]+=1
            elif runner[1]==4:
                screen.blit(runner4, runner[0].rect)
                runner[1]+=1
            elif runner[1]==5:
                screen.blit(runner5, runner[0].rect)
                runner[1]+=1
            elif runner[1]==6:
                screen.blit(runner6, runner[0].rect)
                runner[1]=1

        for phone in phones:
            for runner in runners:
                if phone.rect.colliderect(runner[0].rect):
                    score+=1
                    catch_sound.play()
                    runners_catch.append([runner[0],0])
                    phones.remove(phone)
                    runners.remove(runner)

        for phone in phones:
            phone.move()
            if phone.pos[1] < 0 or phone.pos[0] < 0 or phone.pos[0] > 800 or phone.pos[1]>600:
                phones.remove(phone)

        for runner in runners:
            runner[0].move()
            if runner[0].pos[1] < 75:
                neg_score+=1
                hit_sound.play()
                runners_hit.append([runner[0],0])
                runners.remove(runner)
        
        for hit in runners_hit:
            if hit[1] < 15:
                screen.blit(runner_hit,hit[0].rect)
                hit[1]+=1
            else:
                runners_hit.remove(hit)    

        for caught in runners_catch:
            if caught[1]==0:
                caught[0].move()
                caught[0].move()
            if caught[1]<15: 
                screen.blit(runner_catch,caught[0].rect)
                caught[1]+=1
            else:
                runners_catch.remove(caught)    

        if random.randint(0, 100) < 10 and len(runners)<3:
            spawn_at = random.choice([random.randint(50,300),random.randint(500,750)])
            if abs(spawn_at-last_spawned)>50 and abs(spawn_at-last_to_last_spawned)>50:
                runner_pos = (spawn_at, 600)
                runners.append([Customer(runner_pos),1])
                last_to_last_spawned = last_spawned
                last_spawned = spawn_at

        if score+neg_score==25:
            if score>20:
                screen_name="home page"
                score=0
                neg_score=0
            else:
                screen_name="page 1"   
                score=0
                neg_score=0   


    # Update the display
    pygame.display.flip()
    clock.tick(30)
