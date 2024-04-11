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
catapult_img = pygame.image.load('thrower/img5.png')
throwup = pygame.image.load('thrower/img2.png')
throwdown = pygame.image.load('thrower/img3.png')
rock_img = pygame.image.load('phone.png')
enemy_img1 = pygame.image.load('catcher/run1.png')
enemy_img2 = pygame.image.load('catcher/run2.png')
enemy_img3 = pygame.image.load('catcher/run3.png')
enemy_img4 = pygame.image.load('catcher/run4.png')
enemy_img5 = pygame.image.load('catcher/run5.png')
enemy_img6 = pygame.image.load('catcher/run6.png')
enemy_imgh = pygame.image.load('catcher/hit.png')
enemy_imgc = pygame.image.load('catcher/catch.png')

# Catapult position and state
catapult_pos = (400, 75)
catapult_stretched = False
catapult_angle = 0

# Rock class
class Rock:
    def __init__(self, pos, angle):
        self.pos = pos
        self.angle = angle
        self.speed = 20
        self.image = pygame.transform.rotate(rock_img, angle)
        self.rect = self.image.get_rect(center=pos)

    def move(self):
        dx = math.cos(math.radians(self.angle)) * self.speed
        dy = math.sin(math.radians(self.angle)) * self.speed
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)
        self.rect.center = self.pos

# Enemy class
class Enemy:
    def __init__(self, pos):
        self.pos = pos
        self.speed = 4
        self.image1 = enemy_img1
        self.image2 = enemy_img2
        self.image3 = enemy_img3
        self.image4 = enemy_img4
        self.image5 = enemy_img5
        self.image6 = enemy_img6
        self.rect = self.image1.get_rect(center=pos)

    def move(self):
        self.pos = (self.pos[0], self.pos[1] - self.speed)
        self.rect.center = self.pos

# Game loop
rocks = []
enemies = []
enemies_hit = []
enemies_catch = []
clock = pygame.time.Clock()
running = True
thrower = 0
while running:
    screen.blit(bg_game3,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not catapult_stretched:
            catapult_stretched = True
            catapult_start_pos = pygame.mouse.get_pos()
            thrower =1 

        elif event.type == pygame.MOUSEBUTTONUP and catapult_stretched:
            catapult_stretched = False
            catapult_end_pos = pygame.mouse.get_pos()
            dx = catapult_start_pos[0] - catapult_end_pos[0]
            dy = catapult_start_pos[1] - catapult_end_pos[1]
            catapult_angle = math.degrees(math.atan2(dy, dx))
            rocks.append(Rock(catapult_pos, catapult_angle))
            thrower =2

    if thrower == 0:
        screen.blit(catapult_img, (catapult_pos[0] - catapult_img.get_width() // 2, catapult_pos[1] - catapult_img.get_height() // 2)) 
    if thrower ==1:
        screen.blit(throwup, (catapult_pos[0] - throwup.get_width() // 2, catapult_pos[1] - throwup.get_height() // 2)) 
    elif thrower ==2:
        screen.blit(throwdown, (catapult_pos[0] - throwdown.get_width() // 2, catapult_pos[1] - throwdown.get_height() // 2))

    if catapult_stretched:
        pygame.draw.line(screen, (255,255,255), catapult_pos, pygame.mouse.get_pos(), 5)

    for rock in rocks:
        screen.blit(rock.image, rock.rect)

    for enemy in enemies:
        if enemy[1]==1:
            screen.blit(enemy[0].image1, enemy[0].rect)
            enemy[1]+=1
        elif enemy[1]==2:
            screen.blit(enemy[0].image2, enemy[0].rect)
            enemy[1]+=1
        elif enemy[1]==3:
            screen.blit(enemy[0].image3, enemy[0].rect)
            enemy[1]+=1
        elif enemy[1]==4:
            screen.blit(enemy[0].image4, enemy[0].rect)
            enemy[1]+=1
        elif enemy[1]==5:
            screen.blit(enemy[0].image5, enemy[0].rect)
            enemy[1]+=1
        elif enemy[1]==6:
            screen.blit(enemy[0].image6, enemy[0].rect)
            enemy[1]=1

    for rock in rocks:
        for enemy in enemies:
            if rock.rect.colliderect(enemy[0].rect):
                catch_sound.play()
                enemies_catch.append([enemy[0],0])
                rocks.remove(rock)
                enemies.remove(enemy)

    for rock in rocks:
        rock.move()
        if rock.pos[1] < 0 or rock.pos[0] < 0 or rock.pos[0] > 800:
            rocks.remove(rock)

    for enemy in enemies:
        enemy[0].move()
        if enemy[0].pos[1] < 75:
            hit_sound.play()
            enemies_hit.append([enemy[0],0])
            enemies.remove(enemy)
    
    for hit in enemies_hit:
        if hit[1] < 15:
            screen.blit(enemy_imgh,hit[0].rect)
            hit[1]+=1
        else:
            enemies_hit.remove(hit)    

    for caught in enemies_catch:
        if caught[1]==0:
            caught[0].move()
            caught[0].move()
        if caught[1]<15: 
            screen.blit(enemy_imgc,caught[0].rect)
            caught[1]+=1
        else:
            enemies_catch.remove(caught)    

    if random.randint(0, 100) < 10 and len(enemies)<3:
        enemy_pos = (random.randint(50,750), 600)
        enemies.append([Enemy(enemy_pos),1])

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
