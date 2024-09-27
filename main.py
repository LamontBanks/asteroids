# Docs: https://www.pygame.org/docs/ref/pygame.html
import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Limit the game to 60 FPS
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    game_clock = pygame.time.Clock()
    delta_time = 0  # time passed since last frame was drawn

    # Use Groups to handle sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets, updatable, drawable)

    # Create the player sprite at the center of the screen
    # See player.py
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    # Game loop
    while (True):
        # Listen for the "close window" event to close the game
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return

        # Update sprites
        for obj in updatable:
            obj.update(delta_time)
        # Can't use updatable.update() ?

        
        for asteroid in asteroids:
            # Exit if the player has collided with any asteroids
            if (asteroid.collision(player)):
                print("Game Over!")
                return
            # Destory asteroids and bullets that collide
            for bullet in bullets:
                if (bullet.collision(asteroid)):
                    asteroid.kill()
                    bullet.kill()
        

        # Black screen
        screen.fill(pygame.Color(0, 0, 0))

        # Draw sprites
        for obj in drawable:
            obj.draw(screen)
        # Can't use: drawable.draw(screen) ?

        # Update displays
        pygame.display.flip()

        # Limit to 60 FPS
        delta_time = game_clock.tick(60) / 1000

# Keep at bottom of file
# This line ensures the main() function is only called when this file is run directly; 
# it won't run if it's imported as a module.
# It's considered the "pythonic" way to structure an executable program in Python.
if __name__ == "__main__":
    main()