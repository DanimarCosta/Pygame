# -*- coding: latin-1 -*-
energia0 = 'energia0.png'
energia1 = 'energia1.png'
energia2 = 'energia2.png'
energia3 = 'energia3.png'
energia4 = 'energia4.png'
energia5 = 'energia5.png'
estado = 0

import pygame, sys
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((250,185),0,0)

tela0=pygame.image.load(energia0).convert()
tela1=pygame.image.load(energia1).convert()
tela2=pygame.image.load(energia2).convert()
tela3=pygame.image.load(energia3).convert()
tela4=pygame.image.load(energia4).convert()
tela5=pygame.image.load(energia5).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if (event.type == MOUSEBUTTONUP) and (estado == 0):
            screen.blit(tela0, (0,0))
            estado = 1

        elif (event.type == MOUSEBUTTONUP) and (estado == 1):
            screen.blit(tela1, (0,0))
            estado = 2

        elif (event.type == MOUSEBUTTONUP) and (estado == 2):
            screen.blit(tela2, (0,0))
            estado = 3

        elif (event.type == MOUSEBUTTONUP) and (estado == 3):
            screen.blit(tela3, (0,0))
            estado = 4

        elif (event.type == MOUSEBUTTONUP) and (estado == 4):
            screen.blit(tela4, (0,0))
            estado = 5

        elif (event.type == MOUSEBUTTONUP) and (estado == 5):
            screen.blit(tela5, (0,0))
            estado = 6
   
    
    pygame.display.update()
