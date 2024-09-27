import pygame
import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Create smaller asteroids on destruction (of large, medium asteroid)
    # Large asteroids break into 2 "medium" asteroids
    # Medium into 2 "small" asteroids
    # Small asteroids are simply destroyed
    # The smaller pieces travel in 2 random-ish directions, based on the original directory
    def split(self):
        self.kill()     # Sprite can still be handled after .kill()
        if (self.radius > ASTEROID_MIN_RADIUS):
            # Calculate trajectories
            random_uniform_angle = random.uniform(20, 50)
            smaller_asteroid_1_vector = self.velocity.rotate(random_uniform_angle)
            smaller_asteroid_2_vector = self.velocity.rotate(random_uniform_angle * -1)

            # Calculate size
            smaller_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

            # Create new asteroids, that move faster
            smaller_asteroid_1 = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)
            smaller_asteroid_2 = Asteroid(self.position.x, self.position.y, smaller_asteroid_radius)

            smaller_asteroid_1.velocity = smaller_asteroid_1_vector * ASTEROID_BROKEN_SPEED_SCALING
            smaller_asteroid_2.velocity = smaller_asteroid_2_vector * ASTEROID_BROKEN_SPEED_SCALING

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, width=2)

    def update(self, delta_time):
        self.position += self.velocity * delta_time
