import pygame
import random
from quadrado import *
from caminhante import *
from morcego import *
from caramujo import *


WIDTH = 800
HEIGHT = 380
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255,128,0)
GRAY = (128,128,128)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Experimentando com Sprites")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Quadro(10,RED)
player2 = Quadro(6,GREEN)
player3 = Quadro(4,BLUE)
cami = Caminhante()
bat  = Morcego()
cara = Caramujo()
all_sprites.add(bat)
all_sprites.add(player)
all_sprites.add(player2)
all_sprites.add(player3)
all_sprites.add(cami)
all_sprites.add(cara)

# Game loop
x1 = x2 = y1 = y2 = 0
a1 = a2 = b1 = b2 = 0
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            aaa=0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x1 = 0
            if event.key == pygame.K_RIGHT:
                x2 = 0
            if event.key == pygame.K_UP:
                y1 = 0
            if event.key == pygame.K_DOWN:
                y2 = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 = -5
            if event.key == pygame.K_RIGHT:
                x2 = 5
            if event.key == pygame.K_UP:
                y1 = -5
            if event.key == pygame.K_DOWN:
                y2 = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                a1 = 0
            if event.key == pygame.K_d:
                a2 = 0
            if event.key == pygame.K_w:
                b1 = 0
            if event.key == pygame.K_s:
                b2 = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                a1 = -5
            if event.key == pygame.K_d:
                a2 = 5
            if event.key == pygame.K_w:
                b1 = -5
            if event.key == pygame.K_s:
                b2 = 5
    bat.xpos = bat.xpos + x1+x2
    bat.ypos = bat.ypos + y1+y2
    cara.xpos = cara.xpos + a1+a2
    cara.ypos = cara.ypos + b1+b2
    # Update
    all_sprites.update()
    
    # Draw / render
    screen.fill(GRAY)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
