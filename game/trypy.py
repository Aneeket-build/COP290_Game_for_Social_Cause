import pygame
pygame.init()

width = 850
length = 480
win = pygame.display.set_mode((width,length))
pygame.display.set_caption("Trying")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self,objwidth,objlength,width,length):
        self.objwidth = objwidth
        self.objlength = objlength
        self.x = 0
        self.y = length - objlength
        self.vel = 10
        self.isJump = False
        self.Jumpcnt = 1
        self.left = False 
        self.right = True
        self.standing = True
        self.walkCount = 0

    def draw(self,win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1 
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))         

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 15*facing

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x,end]
        self.vel = 6
        self.walkCount = 0

    def draw(self,win):
        self.move()

        if self.vel>0:
            win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))      
            self.walkCount +=1
    def move(self):
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel>0:
            if self.x + self.vel <= self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel*(-1)
                self.walkCount = 0
        else:
            if self.x + self.vel >= self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel*(-1)
                self.walkCount = 0             


def drawGame():
    win.blit(bg,(0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    goblin.draw(win)    
    pygame.display.update()

man = player(64,64,width,length)
goblin = enemy(200,length-59,64,64,600)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < width and bullet.x >0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))    

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and len(bullets) < 5:
        if man.left :
            facing = -1
        else:
            facing = 1    
        bullets.append(projectile((man.x +(man.objwidth//2)),(man.y + (man.objlength//2)),3,(200,0,255),facing))

    if keys[pygame.K_LEFT] and man.x >= man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x <= (width-man.vel)-man.objwidth:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0    
    if not (man.isJump):
        # if keys[pygame.K_UP] and y >= vel:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y <= (length-vel)-objlength:
        #     y += vel
        if keys[pygame.K_UP]:
            man.isJump = True
            
    else:  
        if man.Jumpcnt<=10:
            man.y -= (((50) - (5*((2*man.Jumpcnt)-1))))
            man.Jumpcnt +=1
        else:
            man.isJump = False
            man.Jumpcnt = 1       

    drawGame()

pygame.quit()



