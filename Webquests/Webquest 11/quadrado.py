import pygame

WIDTH = 800
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Quadro(pygame.sprite.Sprite):
    def __init__(self, vel, cor):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.veloc = vel

    def update(self):
        self.rect.x += self.veloc
        if self.rect.left > WIDTH:
            self.rect.right = 0
 
 
