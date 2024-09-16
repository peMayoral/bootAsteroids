import sys
import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot


def main():

# ----- PRE-INIT ANNOUNCEMENTS
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# ----- INIT
    pygame.init()

# VARIABLES
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH/(2),SCREEN_HEIGHT/2)




# ----- GAMELOOP

    while(True):
        #Allows quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Background Color
        screen.fill(0)

        #Updates
        for sprite in updatable:
            sprite.update(dt)

        #Collision Check
        for asteroid in asteroids:
            for shot in shots:
                if (shot.collisionCheck(asteroid)):
                    shot.kill()
                    asteroid.split()
                    continue

            if(player.collisionCheck(asteroid)):
                print("Game over!")
                sys.exit()


        #Draw cicle
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()