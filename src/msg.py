import pygame
from sys import exit

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("../Assets/sprites/msgs/m1.png").convert_alpha()
bg2 = pygame.image.load("../Assets/sprites/msgs/m5.png").convert_alpha()
msg_box = pygame.image.load("../Assets/sprites/msgs/black_box.png").convert_alpha()
warning = pygame.image.load("../Assets/sprites/msgs/warning.png").convert_alpha()
pygame.display.set_caption('TOXIC TECH')
clock = pygame.time.Clock()

bg_music = pygame.mixer.Sound("../Assets/audio/msg/ryuk_theme.wav")
initial_volume = 1.0  # Assuming the initial volume is the maximum (1.0)
bg_music.set_volume(initial_volume)


# bg_music = pygame.mixer.Sound('')
font = pygame.font.Font("../Assets/fonts/arial.ttf", 28)

# Scene 1
msg1_1 = "Cobalt is a mineral that's essential for making the lithium-ion batteries that power our phones, laptops, and electric vehicles. "

msg1_2 = "The majority of cobalt's world supply is located in the Democratic Republic of the Congo - a country torn by a brutal civil war."

msg1_3 = "The ever increasing demand of cobalt created a wave of violence and massacre across Congo. Military groups enslaved prisoners of war - often children to mine the precious materials."

msg1_4 = "Directly or indirectly, we are all involved in this complex illegal traffic."

# Scene 2
msg2_1 = "Like most electronic gadgets, this phone was assembled in China, in a factory as big as a city."

msg2_2 = "Due to flexible labour laws, the workers are subjected to much abuse and discrimination. They are forced into illegal overtime and often work in inhumane conditions."

msg2_3 = "As a result, many workers commit suicide due to severe desperation."

# Scene 3
msg3_1 = "Then, you purchased this phone. It was new and classy. You've waited for it for months. No evidence of its troubling past was visible."
msg3_2 = "But did you really need it? Of course you did! We have invested a lot of money to instill this desire in you."
msg3_3 = "You were looking for something that could signal your status, your dynamic lifestyle, your unique personality. Just like everyone else..."

# Scene 4
msg4_1 = "Soon, we will introduce a new model which will make this one look antiquated, and you will discard it."
msg4_2 = "It will join tons of highly toxic electronic waste. They say they will recycle it, but it will probably be shipped to countries like Ghana, Pakistan or Bangladesh."
msg4_3 = "There its materials will be salvaged in methods which are harmful to both human health and the environment."

# Instruction message
inst_msg1 = "Click on the tired labourers to keep them digging."
inst_msg2 = "Use Left and Right arrow keys to save the workers commiting suicide so that the production doesn't stop."
inst_msg3 = "Drag back and release to launch the smartphones towards the maddened customers and satiate their craze."
inst_msg4 = "Drag and drop the e-waste to the right disposer to salvage it in environmentally harmful ways."

# Initialize variables
current_msg = ""
msg_timer = 0
msg_index = 0

msgs = []
msg_durations = []

msgs1 = [msg1_1, msg1_2, msg1_3,msg1_4,inst_msg1]
msg_durations1 = [6000,5000,6000,4000,4000]

msgs2 = [msg2_1, msg2_2, msg2_3,inst_msg2]
msg_durations2 = [4000,6000,4000,5000]

msgs3 = [msg3_1, msg3_2, msg3_3,inst_msg3]
msg_durations3 = [5000,5000,6000,5000]

msgs4 = [msg4_1, msg4_2, msg4_3, inst_msg4]
msg_durations4 = [5000,6000,5000,5000]

audio_length = 0

# Define box dimensions
box_width = 625
box_height = 113
box_x = (screen.get_width() - box_width) // 2
box_y = (screen.get_height() - box_height) // 2

def set_message(scene):
    global msg_timer
    global msg_index
    global msgs
    global msg_durations
    global audio_length
    global current_msg
    
    bg_music.play()
    if scene == 1:
        msgs = msgs1
        msg_durations = msg_durations1
        audio_length = sum(msg_durations) + 18000
    
    elif scene == 2:
        msgs = msgs2
        msg_durations = msg_durations2
        audio_length = sum(msg_durations) + 12000
    
    elif scene == 3:
        msgs = msgs3
        msg_durations = msg_durations3
        audio_length = sum(msg_durations) + 12000

    elif scene == 4:
        msgs = msgs4
        msg_durations = msg_durations4
        audio_length = sum(msg_durations) + 12000

    running = True
    start_time = pygame.time.get_ticks()  # Get the start time
    volume_decrement_rate = initial_volume / audio_length

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if msg_timer <= 0:
            if msg_index < len(msgs):
                current_msg = msgs[msg_index]
                msg_timer = msg_durations[msg_index]
                msg_index += 1
            else:
                current_msg = ""
                msg_timer = 0
                msg_index = 0
                break
        else:
            msg_timer -= 0.75

        elapsed_time = pygame.time.get_ticks() - start_time
        if elapsed_time < audio_length:
            current_volume = initial_volume - (elapsed_time * volume_decrement_rate)
            bg_music.set_volume(max(current_volume, 0.0))

        # Clear the screen
        if msg_index < len(msgs):
            screen.blit(background, (0, 0))
        else:
            screen.blit(bg2,(0,0))

        # Split the message into lines that fit within the box
        words = current_msg.split()
        lines = []
        while words:
            line = ''
            while words and font.size(line + words[0])[0] < box_width:
                line += words.pop(0) + ' '
            lines.append(line)

        # Render and display the message
        y = box_y
        for line in lines:
            rendered_msg = font.render(line, True, (0, 0, 0))
            screen.blit(rendered_msg, ((screen.get_width() - rendered_msg.get_width()) // 2, y + 110))
            y += rendered_msg.get_height()

        pygame.display.flip()
    pygame.mixer.stop()

