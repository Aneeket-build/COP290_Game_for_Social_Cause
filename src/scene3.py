import pygame
import math
import random

def execute_failure():
    with open('failure.py', 'r') as file:
        code = file.read()
    exec(code)

pygame.init()
pygame.mixer.init()

bg_audio = pygame.mixer.Sound("../Assets/audio/scene3/scene3_bg_audio.mp3")
bg_audio.set_volume(0.5)
hit_sound = pygame.mixer.Sound("../Assets/audio/scene3/hit.mp3")
catch_sound = pygame.mixer.Sound("../Assets/audio/scene3/phone_catch.mp3")
catch_sound.set_volume(0.3)

bg_game3 = pygame.image.load("../Assets/sprites/scene3/bg_game3.png")
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TOXIC TECH")

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
pause_font1 = pygame.font.Font("../Assets/fonts/play_font.ttf", pause_size1)
pause_font2 = pygame.font.Font("../Assets/fonts/play_font.ttf", pause_size2)
pause_font3 = pygame.font.Font("../Assets/fonts/play_font.ttf", pause_size3)
pause_button1 = pause_font1.render(pause_text1,True,(0,0,0))
pause_button2 = pause_font2.render(pause_text2,True,(0,0,0))
pause_button3 = pause_font3.render(pause_text3,True,(0,0,0))
pause_button1_rect = pause_button1.get_rect(center=(400,240))
pause_button2_rect = pause_button2.get_rect(center=(400,300))
pause_button3_rect = pause_button3.get_rect(center=(400,360))

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

score=0
neg_score=0

font = pygame.font.Font(None, 30)
message2 = "Customers Fooled: "
message3 = str(score) + " / " + str(score+neg_score)
text_surface2 = font.render(message2,True,(255,255,255))
text_surface3 = font.render(message3,True,(255,255,255))
text_rect2 = text_surface2.get_rect(topleft=(10,15))
text_rect3 = text_surface3.get_rect(topleft=(85,50))

thrower_pos = (400, 75)
arm_stretched = False
throw_angle = 0

class Phone:
    def __init__(self, pos, angle):
        self.pos = pos
        self.angle = angle
        self.speed = 20
        self.image = pygame.transform.rotate( pygame.image.load('../Assets/sprites/scene3/phone.png'), angle)
        self.rect = self.image.get_rect(center=pos)

    def move(self):
        dx = math.cos(math.radians(self.angle)) * self.speed
        dy = math.sin(math.radians(self.angle)) * self.speed
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)
        self.rect.center = self.pos

class Customer:
    def __init__(self, pos):
        self.pos = pos
        self.speed = 4
        self.image1 = pygame.image.load('../Assets/sprites/scene3/catcher/run1.png')
        self.rect = self.image1.get_rect(center=pos)

    def move(self):
        self.pos = (self.pos[0], self.pos[1] - self.speed)
        self.rect.center = self.pos

phones = []
runners = []
runners_hit = []
runners_catch = []

last_spawned = 0
last_to_last_spawned = 0

clock = pygame.time.Clock()
running = True
thrower = 0

bg_audio.play()

pause = False

while running:
    screen.blit(bg_game3,(0,0))
    message3 = str(score) + " / " + str(score+neg_score)
    if score+neg_score==0 or score/(score+neg_score) > 0.5 :
        text_surface2 = font.render(message2,True,(0,255,0))
        text_surface3 = font.render(message3,True,(0,255,0))
    else:
        text_surface2 = font.render(message2,True,(255,0,0))
        text_surface3 = font.render(message3,True,(255,0,0))
    text_rect3 = text_surface2.get_rect(topleft=(85,50))
    screen.blit(text_surface2,text_rect2)
    screen.blit(text_surface3,text_rect3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pause:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pause_button1_rect.collidepoint(event.pos):
                pygame.mixer.unpause()
                pause= False
            elif pause_button2_rect.collidepoint(event.pos):
                score=0
                neg_score=0  
                phones = []
                runners = []
                runners_hit = []
                runners_catch = []
                last_spawned = 0
                last_to_last_spawned = 0
                pygame.mixer.unpause()
                pause = False
            elif pause_button3_rect.collidepoint(event.pos):
                exec(open("unlocked_home_page.py").read()) 

        screen.blit(stand_img, (thrower_pos[0] - stand_img.get_width() // 2, thrower_pos[1] - stand_img.get_height() // 2))            
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
        screen.blit(pause_box,(250,200))
        screen.blit(pause_button1,pause_button1_rect)
        screen.blit(pause_button2,pause_button2_rect)
        screen.blit(pause_button3,pause_button3_rect)        
    else:

        if event.type == pygame.MOUSEBUTTONDOWN and not arm_stretched:
            if pause_img_rect.collidepoint(event.pos):
                pygame.mixer.pause()
                pause = True 
            else:    
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
            phone.move()
            if phone.pos[1] < 0 or phone.pos[0] < 0 or phone.pos[0] > 800 or phone.pos[1]>600:
                phones.remove(phone)


        for phone in phones:
            for runner in runners:
                if phone.rect.colliderect(runner[0].rect):
                    score+=1
                    catch_sound.play()
                    runners_catch.append([runner[0],0])
                    phones.remove(phone)
                    runners.remove(runner)

        
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
            if abs(spawn_at-last_spawned)>100 and abs(spawn_at-last_to_last_spawned)>100:
                runner_pos = (spawn_at, 600)
                runners.append([Customer(runner_pos),1])
                last_to_last_spawned = last_spawned
                last_spawned = spawn_at

        screen.blit(pause_img,pause_img_rect)

        if score+neg_score==18:
            if score>9:
                pygame.mixer.stop()
                running = False
            else:
                pygame.mixer.stop()
                execute_failure()
                bg_audio.play()
                score=0
                neg_score=0  
                phones = []
                runners = []
                runners_hit = []
                runners_catch = []
                last_spawned = 0
                last_to_last_spawned = 0
                
    pygame.display.flip()
    clock.tick(30)
