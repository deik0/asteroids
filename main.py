import pygame
from constants import * 

def main():
    print("Starting asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    window = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.Surface.fill(window,(0,0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        pygame.display.update()
        pygame.display.flip()


if __name__ == "__main__":
    main()
