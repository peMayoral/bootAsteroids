from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS



class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255,255,255), self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if (self.radius == ASTEROID_MIN_RADIUS):
            return
        angle = random.uniform(20, 50)

        newVel1 = self.velocity.rotate(angle)
        newVel2 = self.velocity.rotate(-angle)

        newSize = self.radius - ASTEROID_MIN_RADIUS
        
        firstAsteroid = Asteroid(self.position.x, self.position.y, newSize)
        firstAsteroid.velocity = newVel1 *1.2
        secondAsteroid = Asteroid(self.position.x, self.position.y, newSize)
        secondAsteroid.velocity = newVel2 *1.2
        

#VARIABLES
    containers = None