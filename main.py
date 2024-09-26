# Docs: https://www.pygame.org/docs/ref/pygame.html
import pygame

from constants import *



def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while (True):

        # Listen for the "close window" event to close the game
        for event in pygame.event.get():
            print(event)
            if (event.type == pygame.QUIT):
                return

        screen.fill(pygame.Color(0, 0, 0))
        pygame.display.flip()

# Keep at bottom of file
# This line ensures the main() function is only called when this file is run directly; 
# it won't run if it's imported as a module. 

# It's considered the "pythonic" way to structure an executable program in Python.
if __name__ == "__main__":
    main()