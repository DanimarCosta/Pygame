import pygame, math, sys, os

WIDTH = 800
HEIGHT = 380
FPS = 30

class Caminhante(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.addImage("Walk1.png")
        self.addImage("Walk2.png")
        self.addImage("Walk3.png")
        self.addImage("Walk4.png")
        self.addImage("Walk5.png")
        self.addImage("Walk6.png")
        self.addImage("Walk7.png")
        self.addImage("Walk8.png")
        self.image = pygame.Surface.copy(self.images[0])
        self.currentImage = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.scale = 1
        self.xpos = 0
        self.ypos = 100
        self.originalWidth = self.rect.width
        self.originalHeight = self.rect.height
        self.indexns = 0
        self.itera = 0


    def update(self):
        self.itera = self.itera + 1
        self.indexns = int(self.itera/int((6*FPS)/60))%8
        self.changeImage(self.indexns)
        self.xpos = self.xpos + 5
        if self.xpos > WIDTH :
            self.xpos = 0
        self.move( self.xpos, self.ypos)

        
    def addImage(self, filename):
        self.images.append(loadImage(filename))
        print(self.images)

    def move(self, xpos, ypos, centre=False):
        if centre:
            self.rect.center = [xpos, ypos]
        else:
            self.rect.topleft = [xpos, ypos]

    def changeImage(self, index):
        self.currentImage = index
        if self.angle == 0:
            self.image = self.images[index]
        else:
            self.image = pygame.transform.rotate(self.images[self.currentImage], -self.angle)
        oldcenter = self.rect.center
        self.rect = self.image.get_rect()
        self.originalWidth = self.rect.width
        self.originalHeight = self.rect.height
        self.rect.center = oldcenter
        self.mask = pygame.mask.from_surface(self.image)

def loadImage(fileName, useColorKey=False):
    if os.path.isfile(fileName):
        image = pygame.image.load(fileName)
        image = image.convert_alpha()
        # Return the image
        return image
    else:
        raise Exception("Error loading image: " + fileName + " - Check filename and path?")

