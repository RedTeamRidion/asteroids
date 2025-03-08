import pygame
from constants import *

def main():
    pygame.init

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True

    while running:
        # Check for events (like closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill the screen with black color
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()  

    # Clean up Pygame when done
    pygame.quit() 



if __name__ == "__main__":
    main()