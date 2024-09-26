# Docs: https://www.pygame.org/docs/ref/pygame.html
import pygame

from constants import *
from player import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Limit the game to 60 FPS
    # https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick
    game_clock = pygame.time.Clock()
    delta_time = 0  # time passed since last frame was drawn
    desired_max_frame_rate = 60

    # Player sprite at the center of the screen
    # See player.py
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while (True):

        # Listen for the "close window" event to close the game
        for event in pygame.event.get():
            print(event)
            if (event.type == pygame.QUIT):
                return

        # Black screen
        screen.fill(pygame.Color(0, 0, 0))

        # Player
        player.draw(screen)

        # Update display
        pygame.display.flip()
        delta_time = game_clock.tick(desired_max_frame_rate)

# Keep at bottom of file
# This line ensures the main() function is only called when this file is run directly; 
# it won't run if it's imported as a module. 

# It's considered the "pythonic" way to structure an executable program in Python.
if __name__ == "__main__":
    main()