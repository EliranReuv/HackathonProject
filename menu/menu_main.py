import pygame
import button
from screen_elements import *
from consts import *
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")



#game variables

game_quit = False

#define fonts
font = pygame.font.SysFont("Arial", 20)

#Load dynamic screen sizes.
screen_size = screen.get_size() # (width: int, height: int)
block_size = [x // 10 for x in screen_size]

#load background image
background_image = pygame.image.load("images/dungeons/background.jpg").convert_alpha()
background_image = pygame.transform.scale(background_image, (screen_size[0], screen_size[1]))

#load button images
english_dungeon = pygame.image.load("images/dungeons/english_dungeon.png").convert_alpha()
history_dungeon = pygame.image.load("images/dungeons/history_dungeon.png").convert_alpha()
math_dungeon = pygame.image.load("images/dungeons/science_dungeon.png").convert_alpha()
science_dungeon = pygame.image.load("images/dungeons/math_dungeon.png").convert_alpha()


#create button instances
english_dungeon_button = button.Button(block_size[0] * 1.5,  block_size[1] * 2, english_dungeon, 2)
history_dungeon_button = button.Button(block_size[0] * 1.5, block_size[1] * 6, history_dungeon, 2)
math_dungeon_button = button.Button(block_size[0] * 5.5, block_size[1] * 2, math_dungeon, 2)
science_dungeon_button = button.Button(block_size[0] * 5.5, block_size[1] * 6, science_dungeon, 2)



def  choose_dugneon_screen() -> None:
    english_dungeon_button.draw(screen)
    history_dungeon_button.draw(screen)
    math_dungeon_button.draw(screen)
    science_dungeon_button.draw(screen)


#TESTING#################################################################################################


def main() -> None:

    status = 0


    run = True
    while run:
        screen.blit(background_image, (0,0))

        if status == 0:
            choose_dugneon_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if english_dungeon_button.check_click():
                status = 1
                screen.blit(background_image, (0,0))
                
            if history_dungeon_button.check_click():
                status = 1
                screen.blit(background_image, (0,0))

            if  math_dungeon_button.check_click():
                status = 1
                screen.blit(background_image, (0,0))

            if science_dungeon_button.check_click():
                status = 1
                screen.blit(background_image, (0,0))
            
        
        pygame.display.update()
    #SHITTTTT
    pygame.quit()


if __name__ == '__main__':
    main()

################################################################################################