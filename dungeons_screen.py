import pygame
import dungeons
import consts

pygame.init()

dungeon_screen = dungeons.create_dungeon()
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
def show_dungeon_screen():
    screen.fill(consts.DUNGEON_COLOR)
    for i in range(len(dungeon_screen)):
        for j in range(len(dungeon_screen[i])):
            if dungeon_screen[i][j] == "enemy":
                screen.blit(pygame.transform.smoothscale(consts.ENEMY, (40, 40)), (i*40, j*40))
            if dungeon_screen[i][j] == "disc":
                screen.blit(pygame.transform.smoothscale(consts.DISC, (40, 40)), (i*40, j*40))

    return screen

print(ofriiiii)

run = True
while run:

    show_dungeon_screen()
    pygame.display.update()