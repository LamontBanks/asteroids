import pygame

from circleshape import *
from constants import *
from shot import *

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
    
    # Update the position, rotation using the WASD keys
    def update(self, delta_time):
        keys = pygame.key.get_pressed()

        # Key: A - turn left
        if keys[pygame.K_a]:
            self.rotate(delta_time * -1)
        # Key: D - turn right
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        # Key: W - move forward in current direction
        if keys[pygame.K_w]:
            self.move(delta_time)
        # Key: S - move backwards to current direction
        if keys[pygame.K_s]:
            self.move(delta_time * -1)
        # Key: Spacebar - shoot
        if keys[pygame.K_SPACE]:
            self.shoot()

    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def move(self, delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
