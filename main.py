import pygame
from constants import *
from player import Player


def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    pygame.init()

    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/(2),SCREEN_HEIGHT/2)

#GAMELOOP

    while(True):
        #Allows quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Background Color
        screen.fill(0)
        player.draw(screen)
        player.update(dt)

        #Render display
        pygame.display.flip()
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()