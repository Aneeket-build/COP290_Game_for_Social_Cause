import pygame
import sys

def execute_level(file_name):
    with open(file_name, 'r') as file:
        code = file.read()
    exec(code,globals(),locals())  


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Title")

play_hover_sound = pygame.mixer.Sound("../Assets/audio/main_page/play_hover_sound.mp3")

background = pygame.image.load("../Assets/sprites/main_page/main.jpg")
background = pygame.transform.scale(background, (800, 600))
screen_img = pygame.image.load("../Assets/sprites/main_page/phone_screen_plain.png")

text_size1 = 25
text_size2 = 25
text_size3 = 25
text_size4 = 25
text_size5 = 25
text1 = "Scene1"
text2 = "Scene2"
text3 = "Scene3"
text4 = "Scene4"
text5 = "Main Menu"

pause = 0

clock = pygame.time.Clock()

running = True

font1 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size1)
play_button1 = font1.render(text1, True, (0, 0, 0))
play_button_rect1 = play_button1.get_rect(center=(400, 240))
font2 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size2)
play_button2 = font2.render(text2, True, (0, 0, 0))
play_button_rect2 = play_button2.get_rect(center=(400, 300))
font3 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size3)
play_button3 = font3.render(text3, True, (0, 0, 0))
play_button_rect3 = play_button3.get_rect(center=(400, 360))
font4 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size4)
play_button4 = font4.render(text4, True, (0, 0, 0))
play_button_rect4 = play_button4.get_rect(center=(400, 420))
font5 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size5)
play_button5 = font5.render(text5, True, (0, 0, 0))
play_button_rect5 = play_button5.get_rect(center=(400, 480))

head_font = pygame.font.Font("../Assets/sprites/main_page/choose_font.ttf", 50)
head_text = head_font.render("Choose",True,(255,180,60))
head_text_rect = head_text.get_rect(center=(400,135))
head_text2 = head_font.render("Game",True,(255,180,60))
head_text_rect2 = head_text2.get_rect(center=(400,175))

start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == pygame.MOUSEMOTION:
        if play_button_rect1.collidepoint(event.pos):
            text_size1 = 30
            if(pause==0):
                play_hover_sound.play()
                pause+=1
        elif play_button_rect2.collidepoint(event.pos):
            text_size2 = 30
            if(pause==0):
                play_hover_sound.play()
                pause+=1
        elif play_button_rect3.collidepoint(event.pos):
            text_size3 = 30
            if(pause==0):
                play_hover_sound.play()
                pause+=1
        elif play_button_rect4.collidepoint(event.pos):
            text_size4 = 30
            if(pause==0):
                play_hover_sound.play()
                pause+=1
        elif play_button_rect5.collidepoint(event.pos):
            text_size5 = 30
            if(pause==0):
                play_hover_sound.play()
                pause+=1        
        else:
            text_size1 = 25
            text_size2 = 25
            text_size3 = 25
            text_size4 = 25
            text_size5 = 25
            pause=0
            
    current_time = pygame.time.get_ticks()        
    if event.type == pygame.MOUSEBUTTONDOWN and (current_time-start_time)>2000:
        if play_button_rect1.collidepoint(event.pos):
            running = False
            execute_level("scene1.py")
            exec(open("unlocked_home_page.py").read())
        elif play_button_rect2.collidepoint(event.pos):
            running = False 
            execute_level("factory.py")
            exec(open("unlocked_home_page.py").read())
        elif play_button_rect3.collidepoint(event.pos):
            running = False 
            execute_level("throw.py")
            exec(open("unlocked_home_page.py").read())
        elif play_button_rect4.collidepoint(event.pos):
            running = False 
            execute_level("scene4.py")
            exec(open("unlocked_home_page.py").read())
        elif play_button_rect5.collidepoint(event.pos):
            running = False
            exec(open("unlocked_home_page.py").read())    

    screen.blit(background, (0, 0))
    screen.blit(screen_img,(271,108))
    font1 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size1)
    play_button1 = font1.render(text1, True, (0, 0, 0))
    play_button_rect1 = play_button1.get_rect(center=(400, 240))
    screen.blit(play_button1,play_button_rect1)
    font2 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size2)
    play_button2 = font2.render(text2, True, (0, 0, 0))
    play_button_rect2 = play_button2.get_rect(center=(400, 300))
    screen.blit(play_button2,play_button_rect2)
    font3 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size3)
    play_button3 = font3.render(text3, True, (0, 0, 0))
    play_button_rect3 = play_button3.get_rect(center=(400, 360))
    screen.blit(play_button3,play_button_rect3)
    font4 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size4)
    play_button4 = font4.render(text4, True, (0, 0, 0))
    play_button_rect4 = play_button4.get_rect(center=(400, 420))
    screen.blit(play_button4,play_button_rect4)
    font5 = pygame.font.Font("../Assets/sprites/main_page/play_font.ttf", text_size5)
    play_button5 = font5.render(text5, True, (0, 0, 0))
    play_button_rect5 = play_button5.get_rect(center=(400, 480))
    screen.blit(play_button5,play_button_rect5)
   
    screen.blit(head_text,head_text_rect)
    screen.blit(head_text2,head_text_rect2)

    pygame.display.flip()
    clock.tick(30)

