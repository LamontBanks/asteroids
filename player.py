import pygame

from circleshape import *
from constants import *

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # Override from CircleShare
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)
    
    # Copy-pasted code
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    
    def update(self, delta_time):
        keys = pygame.key.get_pressed()

        # Key: A - turn left
        if keys[pygame.K_a]:
            self.rotate(delta_time * -1)
        # Key: D - turn right
        if keys[pygame.K_d]:
            self.rotate(delta_time)
    
    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time