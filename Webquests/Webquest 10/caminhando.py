import pygame, math, sys, os

WIDTH = 800
HEIGHT = 380
FPS = 30
GRAY = (128,128,128)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Experimentando com Sprites")
clock = pygame.time.Clock()
images = []
images.append(pygame.image.load("Walk1.png"))
images.append(pygame.image.load("Walk2.png"))
images.append(pygame.image.load("Walk3.png"))
images.append(pygame.image.load("Walk4.png"))
images.append(pygame.image.load("Walk5.png"))
images.append(pygame.image.load("Walk6.png"))
images.append(pygame.image.load("Walk7.png"))
images.append(pygame.image.load("Walk8.png"))
itera = 0
xpos = 0
ypos = 100
running = True
while running:
    itera = itera + 1
    indexImg = int(itera/int((6*FPS)/60))%8
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False         
           
    screen.fill(GRAY)
    screen.blit(images[indexImg], (xpos,ypos))
    pygame.display.flip()
    xpos = xpos + 5
    if xpos > WIDTH: xpos = 0

pygame.quit()
