import pygame, sys
import math

pygame.init()

largura_janela = 800   
altura_janela = 600
pygame.display.set_caption('Game do Mario')
clock = pygame.time.Clock()
fgExit = False
personagemImg = pygame.image.load('mario.png')
personagem2Img = pygame.image.load('cogumelo.png')
cenario = pygame.image.load('cenario-mario.jpg')
tela = pygame.display.set_mode((largura_janela, altura_janela))
x = (largura_janela * 0.1)
y = (altura_janela * 0.1)
x1 = 0
x2 = 0
y1 = 0
y2 = 0
personagem_speed = 0
xmario = x+45
ymario = y+65
xcogumelo = 500+128
ycogumelo = 300+128
x_1 = x
y_1 = y
print ('vamos la')

def colidiu():
    distancia =  math.sqrt(math.pow(xmario-xcogumelo,2)+math.pow(ymario-ycogumelo,2))
    print (distancia)
    if distancia<128+50:
        return True
    else:
        return False

while not fgExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fgExit = True
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
    x += x1 + x2
    y += y1 + y2
    xmario = x+45
    ymario = y+65
    if colidiu():
        print ('bateu')
        x = x_1
        y = y_1                       
    else:
        x_1 = x
        y_1 = y
    tela.blit(cenario,(0,0))
    tela.blit(personagem2Img, (500, 300))
    tela.blit(personagemImg, (x, y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()

