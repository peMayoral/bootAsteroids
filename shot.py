from circleshape import CircleShape
from constants import SHOT_RADIUS as radius
import pygame


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius)    

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255,255,255), self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

#VARIABLES
    containers = None
