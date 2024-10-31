import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self,jugador):
        r1 = (self.radius /2) 
        r2 = (jugador.radius /2)

        distancia = pygame.math.Vector2.distance_to(self.position,jugador.position)
        #print(f"RADIO = asteroide {r1} jugador {r2}")
        #print(f"POSICION = asteroide: {self.position} jugador : {jugador.position}")
        #print(f"DISTANCIA = distancia: {distancia}")
        if distancia < (r1 + r2):
            return True
        else:
            pass
        return False
    
   