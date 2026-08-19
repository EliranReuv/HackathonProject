import pygame
import button

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")

#game variables

game_quit = False

#define fonts
font = pygame.font.SysFont("Arial", 20)

#define colours
TEXT_COL = (255, 255, 255)

CELL_SIZE = 20

#load button images
english_dungeon = pygame.image.load("dungeons/english_dungeon.png").convert_alpha()
history_dungeon = pygame.image.load("dungeons/history_dungeon.png").convert_alpha()
math_dungeon = pygame.image.load("dungeons/science_dungeon.png").convert_alpha()
science_dungeon = pygame.image.load("dungeons/math_dungeon.png").convert_alpha()


#create button instances
english_dungeon_button = button.Button(0, 0, english_dungeon, 1)
history_dungeon_button = button.Button(360, 75, english_dungeon, 1)
math_dungeon_button = button.Button(250, 300, english_dungeon, 1)
science_dungeon_button = button.Button(800, 600, english_dungeon, 1)


run = True
while run:
    screen.fill((0, 0, 0))
    english_dungeon_button.draw(screen)
    math_dungeon_button.draw(screen)
    history_dungeon_button.draw(screen)
    science_dungeon_button.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()