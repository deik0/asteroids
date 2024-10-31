import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys



def main():
    print("Starting asteroids!")
    pygame.init()
    
    window = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    jugador = Player(SCREEN_WIDTH / 2,
               SCREEN_HEIGHT / 2,
               PLAYER_RADIUS)
    asteroides = AsteroidField()
    
    pygame.mixer.init()
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()
    
    

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(window,(0,0,0)) #Dibuja el fondo de negro
        for obj in drawable:
            obj.draw(screen=window)
        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            for shot in shots:
                if obj.collision(shot) == True:
                    if obj.radius < ASTEROID_MIN_RADIUS:
                        obj.kill()
                    else:
                        obj.split()
                    shot.kill()
                    effect = pygame.mixer.Sound("destroyed.mp3")
                    pygame.mixer.Sound.play(effect)
            if obj.collision(jugador) == True:
                print("Game over!")
                sys.exit()
            else:
                pass



        pygame.display.update() # Ni idea
        pygame.display.flip() # Necesario

        time_passed = game_clock.tick(60) 
        dt  = time_passed /1000
        


if __name__ == "__main__":
    main()
