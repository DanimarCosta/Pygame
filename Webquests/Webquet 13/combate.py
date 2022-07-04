import pygame, sys
from random import randint
pygame.init()

#variáveis e definições

largura_janela = 800   
altura_janela = 600
tela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Batalha Pokemon')
clock = pygame.time.Clock()

branco = (255,255,255)
preto = (0,0,0)
verde = (0,128,0)
vermelho = (255,0,0)

def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, 38)
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1, [x, y])

fgExit = False

cenario = pygame.image.load('cenario.jpg')
pikachu = pygame.image.load('pikachu.png')
pikachu2 = pygame.transform.scale(pikachu, (400, 400))
charmander = pygame.image.load('charmander.png')
charmander2 = pygame.transform.scale(charmander, (400, 400))

vidapikachu = 20
vidacharmander = 20
especialpikachu = 10
especialcharmander = 10
turno = randint (0, 1)

#loop do reset do game e botões de combate

while not fgExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fgExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                vidapikachu = 20
                vidacharmander = 20
                especialpikachu = 10
                especialcharmander = 10
                turno = randint (0, 1)
                pygame.draw.rect(tela, branco, [0, altura_janela-40, largura_janela, 40])
                texto("Pontos de Vida: "+str(vidapikachu), preto, 20, 10, altura_janela-30)
                texto("Pontos de Vida: "+str(vidacharmander), preto, 20, 500, altura_janela-30)
                pygame.display.update()
        if event.type == pygame.KEYDOWN and vidapikachu >0 and vidacharmander >0:             
            if event.key == pygame.K_1 and turno == 0:
                vidacharmander = vidacharmander - 1
                especialpikachu = especialpikachu + 3
                turno = 1
                print (vidapikachu)
            if event.key == pygame.K_2 and turno == 0:
                vidacharmander = vidacharmander - 2
                especialpikachu = especialpikachu + 1
                turno = 1
                print (vidapikachu)
            if event.key == pygame.K_3 and especialpikachu >= 10 and turno == 0:
                vidacharmander = vidacharmander - randint(0, 5)
                especialpikachu = especialpikachu - 9
                turno = 1
                print (vidapikachu)
            if event.key == pygame.K_8 and turno == 1:
                vidapikachu = vidapikachu - 1
                especialcharmander = especialcharmander + 3
                turno = 0
                print (vidacharmander)
            if event.key == pygame.K_9 and turno == 1:
                vidapikachu = vidapikachu - 2
                especialcharmander = especialcharmander + 1
                turno = 0
                print (vidacharmander)
            if event.key == pygame.K_0 and especialcharmander >= 10 and turno == 1:
                vidapikachu = vidapikachu - randint(0, 5)
                especialcharmander = especialcharmander - 9
                turno = 0
                print (vidacharmander)

#loop dos pontos do placar de vida
                
        if vidapikachu >0 and vidacharmander >0:
            pygame.draw.rect(tela, branco, [0, altura_janela-40, largura_janela, 40])
            texto("Pontos de Vida: "+str(vidapikachu), preto, 20, 10, altura_janela-30)
            texto("Pontos de Vida: "+str(vidacharmander), preto, 20, 500, altura_janela-30)
            pygame.display.update()
        if vidapikachu <= 0:
            print ('pikachu dead')
            pygame.draw.rect(tela, branco, [0, altura_janela-40, largura_janela, 40])
            texto("Pontos de Vida: morto", preto, 20, 10, altura_janela-30)
            texto("Pontos de Vida: "+str(vidacharmander), preto, 20, 500, altura_janela-30)
            pygame.display.update()
        if vidacharmander <= 0:
            print ('charmander dead')
            pygame.draw.rect(tela, branco, [0, altura_janela-40, largura_janela, 40])
            texto("Pontos de Vida: morto", preto, 20, 500, altura_janela-30)
            texto("Pontos de Vida: "+str(vidapikachu), preto, 20, 10, altura_janela-30)
            pygame.display.update()

#exibição de personagens/cenário, Barra de especial e vez do jogador
    
    tela.blit(cenario,(0,0))
    tela.blit(pikachu2,(0,157))
    tela.blit(charmander2, (400, 157))
    pygame.draw.rect(tela, branco, [0, 0, largura_janela, 40])
    pygame.draw.rect(tela, vermelho, [0, 0,((largura_janela/2)/10)*especialpikachu, 40])
    texto("Especial Pikachu", preto, 0, 10, 10)
    pygame.draw.rect(tela, branco, [largura_janela/2, 0, largura_janela/2, 40])
    pygame.draw.rect(tela, verde, [largura_janela/2, 0, ((largura_janela/2)/10)*especialcharmander, 40])
    texto("Especial Charmander", preto, 0, (largura_janela/2)+10, 10)
    if turno == 0 and vidapikachu > 0 and vidacharmander > 0:
        texto("Jogador 1", preto, 0, 120, 100)
    if turno == 1 and vidapikachu > 0 and vidacharmander > 0:
        texto("Jogador 2", preto, 0, 550, 100)        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
