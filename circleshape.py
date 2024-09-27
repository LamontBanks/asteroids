# Copy-pasted code
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    # Two CircleShapes are colliding if the distance between their centers <= radius_1 + radius_2
    def collision(self, anotherCircleShape):
        # position is a Vector2:
        # https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2.distance_to
        distance = self.position.distance_to(anotherCircleShape.position)
        
        return (distance <= (self.radius + anotherCircleShape.radius))

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass