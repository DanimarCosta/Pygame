import pygame, random
from pygame.locals import *

#definição de cores e imagens

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)

cogumeload = pygame.image.load('cogumelo.png')
cogumelofigura = pygame.transform.scale(cogumeload, (60, 60))
miraload = pygame.image.load('mira.png')
mira = pygame.transform.scale(miraload, (30, 30))
cenario = pygame.image.load('cenario-mario.jpg')

#definição de texto, alvo cogumelo e da função click

def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, 50)
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1, [x, y])
    
def cogumeloalvo(cogumelox, cogumeloy, cogumelolargura, cogumeloaltura):
    cogumelo = (cogumelox, cogumeloy)
    tela.blit(cogumelofigura, cogumelo)

def click(cogumelox, cogumeloy, cogumelolargura, cogumeloaltura):
    mouse = pygame.mouse.get_pos()
    if cogumelox < mouse[0] < cogumelox + cogumelolargura and cogumeloy < mouse[1] < cogumeloy + cogumeloaltura:
        print("Clique no cogumelo")
        status = DENTRO
    else:
        print("Clique fora do cogumelo")
        status = FORA
    return cogumelox, status

#inicialização e demais configurações

pygame.init()
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Teste sua mira')

clock = pygame.time.Clock()

DIREITA = 1
ESQUERDA = 0
FORA = 1
DENTRO = 0
contador = 10

sentido = DIREITA
status = FORA
cogumelox = 0
cogumeloy = random.randint(50, 500)
cogumelolargura, cogumeloaltura = 50, 50
cogumeloalvo(cogumelox, cogumeloy, cogumelolargura, cogumeloaltura)

#loop do game - mouseclick, reiniciar e movimentação do alvo cogumelo

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()        
        if event.type == MOUSEBUTTONDOWN and contador >0:
            cogumelox, status = click(cogumelox, cogumeloy, cogumelolargura, cogumeloaltura)
            if status == DENTRO:
                contador = contador -1
                status = FORA
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                contador = 10
                status = FORA             

    if sentido == DIREITA and status == FORA:
        cogumelox = cogumelox + 10
    if sentido == ESQUERDA and status == FORA:
        cogumelox = cogumelox - 10

    if cogumelox < -80 or cogumelox > 620:
        sentido = random.randint(0, 2)
        if sentido == 0:
            sentido = ESQUERDA
            cogumelox = 610
        if sentido == 1:
            sentido = DIREITA
            cogumelox = -60
        cogumeloy = random.randint(50, 500)

#definições de exibição na tela

    pygame.mouse.set_visible(False)
    tela.blit(cenario,(0,0))

    cogumeloalvo(cogumelox, cogumeloy, cogumelolargura, cogumeloaltura)
    tela.blit(mira,(pygame.mouse.get_pos(),pygame.mouse.get_pos()))

    pygame.draw.rect(tela, preto, [145, 0, 310, 45])
    pygame.draw.rect(tela, branco, [150, 0, 300, 40])
    pygame.draw.rect(tela, vermelho, [150, 0,((300)/10)*contador, 40])

    if contador <= 0:
        texto("Você venceu!", preto, 200, 200, 300)
        texto("Aperte r para reiniciar.", preto, 200, 140, 330)
        status = DENTRO
        pygame.display.update()

    pygame.display.update()
