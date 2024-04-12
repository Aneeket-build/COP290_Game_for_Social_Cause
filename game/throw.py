import pygame
import math
import random

# Initialize Pygame
pygame.init()

hit_sound = pygame.mixer.Sound("hit.mp3")
catch_sound = pygame.mixer.Sound("phone_catch.mp3")

bg_game3 = pygame.image.load("bg_game3.png")
# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Catapult Game")

# Load images
stand_img = pygame.image.load('thrower/img5.png')
throwup = pygame.image.load('thrower/img2.png')
throwdown = pygame.image.load('thrower/img3.png')
thrown = pygame.image.load('thrower/img4.png')
pickup = pygame.image.load('thrower/img1.png')
phone_img = pygame.image.load('phone.png')
runner1 = pygame.image.load('catcher/run1.png')
runner2 = pygame.image.load('catcher/run2.png')
runner3 = pygame.image.load('catcher/run3.png')
runner4 = pygame.image.load('catcher/run4.png')
runner5 = pygame.image.load('catcher/run5.png')
runner6 = pygame.image.load('catcher/run6.png')
runner_hit = pygame.image.load('catcher/hit.png')
runner_catch = pygame.image.load('catcher/catch.png')

# Catapult position and state
thrower_pos = (400, 75)
arm_stretched = False
throw_angle = 0

# Rock class
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

# Game loop
phones = []
runners = []
runners_hit = []
runners_catch = []
clock = pygame.time.Clock()
running = True
thrower = 0
while running:
    screen.blit(bg_game3,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not arm_stretched:
            arm_stretched = True
            catapult_start_pos = pygame.mouse.get_pos()
            thrower =1 

        elif event.type == pygame.MOUSEBUTTONUP and arm_stretched:
            arm_stretched = False
            catapult_end_pos = pygame.mouse.get_pos()
            dx = catapult_start_pos[0] - catapult_end_pos[0]
            dy = catapult_start_pos[1] - catapult_end_pos[1]
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

    for rock in phones:
        screen.blit(rock.image, rock.rect)

    for enemy in runners:
        if enemy[1]==1:
            screen.blit(runner1, enemy[0].rect)
            enemy[1]+=1
        elif enemy[1]==2:
            screen.blit(runner2, enemy[0].rect)
            enemy[1]+=1
        elif enemy[1]==3:
            screen.blit(runner3, enemy[0].rect)
            enemy[1]+=1
        elif enemy[1]==4:
            screen.blit(runner4, enemy[0].rect)
            enemy[1]+=1
        elif enemy[1]==5:
            screen.blit(runner5, enemy[0].rect)
            enemy[1]+=1
        elif enemy[1]==6:
            screen.blit(runner6, enemy[0].rect)
            enemy[1]=1

    for rock in phones:
        for enemy in runners:
            if rock.rect.colliderect(enemy[0].rect):
                catch_sound.play()
                runners_catch.append([enemy[0],0])
                phones.remove(rock)
                runners.remove(enemy)

    for rock in phones:
        rock.move()
        if rock.pos[1] < 0 or rock.pos[0] < 0 or rock.pos[0] > 800:
            phones.remove(rock)

    for enemy in runners:
        enemy[0].move()
        if enemy[0].pos[1] < 75:
            hit_sound.play()
            runners_hit.append([enemy[0],0])
            runners.remove(enemy)
    
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
        enemy_pos = (random.randint(50,750), 600)
        runners.append([Customer(enemy_pos),1])

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
