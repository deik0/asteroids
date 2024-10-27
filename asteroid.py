from circleshape import CircleShape
from constants import * 
import pygame

class Asteroid(CircleShape):
    def __init__(self,x,y,radius): 
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.velocity = ""
        self.rotation = 0

        #print(f"{self.velocity} de asteroides class")

    def draw(self,screen):
        pygame.draw.circle(surface=screen,
                           color=(255,255,255),
                           width=4,
                           center=(self.position),
                           radius=self.radius)

        #print("se dibuja el bicho")
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

        