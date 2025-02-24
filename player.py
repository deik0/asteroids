from circleshape import CircleShape
from constants import * 
from shot import Shot
import pygame



class Player(CircleShape):
    
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.rotation = 0
        self.x = x
        self.y = y
        self.timer = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(surface=screen,
                            color=(255,255,255),
                            width=2,
                            points=self.triangle())
        #return super().draw(screen)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(dt)

        if keys[pygame.K_d]:
            self.rotate(-dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer > 0:
                pass
            else:    
                self.shoot()
                SHOT_SFX = pygame.mixer.Sound("shot.mp3")
                pygame.mixer.Sound.play(SHOT_SFX)
                self.timer = PLAYER_SHOOT_COOLDOWN

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt 

    def shoot(self):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        Shot(self.position[0],
             self.position[1],
             radius=SHOT_RADIUS,
             velocity=velocity)


