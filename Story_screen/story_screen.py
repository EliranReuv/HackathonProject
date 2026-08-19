import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width = screen.get_width()
height = screen.get_height()

background = pygame.image.load('background.jpg')
button_img = pygame.image.load('back_button.png')
button_img = pygame.transform.scale(button_img, (140, 70))
button_rect = button_img.get_rect()
button_pos = (width-150, height-80)
button_rect.topleft = button_pos
story = """             Global IQ has dropped because of A.I...
        People can no longer think for themselves...
                It seems like the end is near.
                            But...
                            
Our player, by sheer chance; stumbles upon Einstein's secret room,
                a place filled with labyrinths...
                    On his final day, 
    Einstein foresaw a future where AI would take over the world.
    
At the end of each labyrinth lies a boss guarding a piece of a legendary artifact;
    the key to saving the world from AI. Secure it, and you can save humanity.
                To obtain this legendary artifact,
    you must complete every labyrinth in the room.
    
Do you have what it takes to claim Einstein's legendary artifact?
"""


def create_welcome_screen():
    global background
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))
    print_text()
    create_button()

# main loop to copy to main.py
"""    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:  # יציאה בלחיצה על Esc
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] >= button_pos[0] and mouse[1] >= button_pos[1]:
                    pass # calls back for the lobby window
        pygame.display.update()"""

def print_text():
    font = pygame.font.Font("fontt.otf", 30)
    text = font.render(story, True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.midtop = (screen.get_width() / 2 + 150, 0)
    screen.blit(text, text_rect)


def create_button():
    screen.blit(button_img, button_rect)