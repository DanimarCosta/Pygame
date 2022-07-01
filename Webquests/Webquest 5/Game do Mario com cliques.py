import pygame, sys
pygame.init()

largura_janela = 800   
altura_janela = 600
pygame.display.set_caption('Game do Mario')
clock = pygame.time.Clock()

fgExit = False

personagemImg = pygame.image.load('mario.png')
cenario = pygame.image.load('cenario-mario-2.jpg')

pulo = pygame.mixer.Sound('pulo-mario.ogg')
passo = pygame.mixer.Sound('passo.ogg')

somdefundo = pygame.mixer.music.load('somdefundo-mario.mp3')
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1)

fonte = pygame.font.SysFont("dejavusans", 30)
texto1 = fonte.render("Olá gamer, seja bem vindo ao jogo do Mário!", True, (255,0,0))
texto2 = fonte.render("Vamos começar a jogar?", True, (255,0,0))
texto3 = fonte.render("Use as setas para se movimentar", True, (255,0,0))
texto4 = fonte.render("Quais som você escuta?", True, (255,0,0))
texto5 = fonte.render("Obrigado por prestigiar esse game!", True, (255,0,0))
contador = 0

tela = pygame.display.set_mode((largura_janela, altura_janela))
x = (largura_janela * 0.1)
y = (altura_janela * 0.1)
x1 = 0
x2 = 0
y1 = 0
y2 = 0
personagem_speed = 0

while not fgExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fgExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            contador = contador +1
            if contador == 1:
               tela.blit(texto1, (0,550))
            if contador == 2:
               tela.fill((0,0,0))
               tela.blit(texto2, (0,550))
            if contador == 3:
               tela.fill((0,0,0))
               tela.blit(texto3, (0,550))
            if contador == 4:
               tela.fill((0,0,0))
               tela.blit(texto4, (0,550))
            if contador == 5:
               tela.fill((0,0,0))
               tela.blit(texto5, (0,550))
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
                passo.play()
            if event.key == pygame.K_RIGHT:
                x2 = 5
                passo.play()
            if event.key == pygame.K_UP:
                y1 = -5
                pulo.play()
            if event.key == pygame.K_DOWN:
                y2 = 5
    x += x1 + x2
    y += y1 + y2
    tela.blit(cenario,(0,0))
    tela.blit(personagemImg, (x, y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()

