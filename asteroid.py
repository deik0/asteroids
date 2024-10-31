from circleshape import CircleShape
from constants import * 
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius): 
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.velocity = ""
        self.rotation = 0

    def draw(self,screen):
        pygame.draw.circle(surface=screen,
                           color=(255,255,255),
                           width=4,
                           center=(self.position),
                           radius=self.radius)

        return super().draw(screen)


    def update(self,dt):
        #print("se updatea el bicho")
        self.move(dt)

    def move(self,dt):
        #print("se mueve el bicho")
        forward = pygame.Vector2(0, 1)
        self.position += forward + (self.velocity *  dt)
        #print(f"velocidad {self.velocity}")
        #print(f"posicion {self.position}")

    def split(self):
        self.kill()
        print("Split")
        random_angle = random.uniform(20,50)
        split1 = pygame.math.Vector2.rotate(self.velocity,random_angle)
        split2 = pygame.math.Vector2.rotate(self.velocity,-random_angle)
        radius1 = self.radius - ASTEROID_MIN_RADIUS  
        radius2 = self.radius - ASTEROID_MIN_RADIUS  
        Asteroid1 = Asteroid(self.position.x,self.position.y,radius1)
        Asteroid1.velocity = split1 * 1.2        
        Asteroid2 = Asteroid(self.position.x,self.position.y,radius2)
        Asteroid2.velocity = split2 * 1.2        