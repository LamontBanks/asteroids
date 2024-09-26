import pygame

from constants import *



def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# Keep at bottom of file
# This line ensures the main() function is only called when this file is run directly; 
# it won't run if it's imported as a module. 

# It's considered the "pythonic" way to structure an executable program in Python.
if __name__ == "__main__":
    main()