from circleshape import CircleShape
from constants import * 
import pygame

class Shot(CircleShape):
    def __init__(self,x,y,radius,velocity): 
        super().__init__(x,y,radius)
        self.x = x
        self.y = y
        self.velocity = ""
        self.rotation = 0
        self.velocity = velocity

    def draw(self,screen):
        pygame.draw.circle(surface=screen,
                           color=(255,255,255),
                           width=2,
                           center=(self.position),
                           radius=self.radius)
        return super().draw(screen)


    def update(self,dt):
        #print("se updatea el bicho")
        self.move(dt)

    def move(self,dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward + (self.velocity *  dt) * PLAYER_SHOOT_SPEED  
        #print(f"velocidad {self.velocity}")
        #print(f"posicion {self.position}")

        