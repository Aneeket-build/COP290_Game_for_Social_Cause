import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Title")

doom_sound = pygame.mixer.Sound("../Assets/audio/doom/doom.mp3")

doom_phone = pygame.image.load("../Assets/sprites/doom/doom_phone.png")
bg_descent = pygame.image.load("../Assets/sprites/doom/doom1.png")

clock = pygame.time.Clock()

class Doom_phone:
    def __init__(self):
        self.x = 400
        self.y = 0
        self.image = pygame.image.load("../Assets/sprites/doom/doom_phone.png")
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.count=0

    def move(self):
        self.y += 1.2
        self.rect.center = (self.x,self.y)  


descent_spawned = False
doom_phone_obj = 0

running = True

while running:
    screen.blit(bg_descent,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if descent_spawned:
        if doom_phone_obj.y<255:
            doom_phone_obj.move()
            doom_phone_obj.count+=1
            screen.blit(doom_phone_obj.image,doom_phone_obj.rect)
        elif doom_phone_obj.count > 375:
            running = False
        else:
            screen.blit(doom_phone_obj.image,doom_phone_obj.rect)   
            doom_phone_obj.count+=1 
    else:
        doom_phone_obj = Doom_phone()
        screen.blit(doom_phone_obj.image,doom_phone_obj.rect)
        descent_spawned = True
        doom_sound.play()

    pygame.display.flip()
    clock.tick(30)