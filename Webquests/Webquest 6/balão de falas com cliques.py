import pygame
import math


pygame.init()
game_display = pygame.display.set_mode((800 , 600))
pygame.display.set_caption('A Matemática está em tudo')
clock = pygame.time.Clock()   # relogio pra temporizar a animaçao
personagem = pygame.image.load('mario.png')

t=0
x= 100
y = 470
x1 = 0
x2 = 0

def balao(screen,text, x0,y0):
    font = pygame.font.SysFont('comicsansms', 12, bold=False, italic=False)  #pygame.font.Font(font, 12)
    textSurf = font.render(text, True, (30,30,30)).convert_alpha()
    textSize = textSurf.get_size()   
    bubbleSurf = pygame.Surface((textSize[0] + 31, textSize[1] + 15 + 30))
    bubbleSurf.fill((0,0,0))
    bubbleSurf.set_colorkey((0,0,0))  
    l = 6
    x,y = textSize[0] + 30, textSize[1] + 15
    points = [ [l,0], [x-l,0],[x,l],[x,y-l],[x-l,y], [x/2+6,y] ,[x/2,y+30], [x/2-6,y] ,[l,y],[0,y-l],[0,l]]
    pygame.draw.polygon(bubbleSurf, (255,255,255), points)
    pygame.draw.lines(bubbleSurf, (30,30,30), True, points)
    bubbleRect = bubbleSurf.get_rect()
    bubbleSurf.blit(textSurf, textSurf.get_rect(center = (x/2,y/2)))
    bubbleRect.center = (x0,y0-bubbleRect[3]/2)
    screen.blit(bubbleSurf, bubbleRect)
    


pygame.font.init()
fs = pygame.font.get_fonts()
print(fs)
itera = 0
falas = ["Olá","Eu sou o Mário.","Como você está?","Só queria falar que","A Matemática está em TUDO!","E em breve em TODOS!","Até mais","Vamos recomeçar?"]



while True :
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            itera = itera + 1
          if event.type == pygame.QUIT:
            pygame.quit()
          if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x1 = 0
            if event.key == pygame.K_RIGHT:
                x2 = 0
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 = -2
            if event.key == pygame.K_RIGHT:
                x2 = +2
        x += x1 + x2
        game_display.fill((135,206,235))
        game_display.blit(personagem, (x, y))
        tx,ty = x+30,y-2
        balao(game_display,falas[itera%len(falas)],tx,ty)
        pygame.display.update()
        clock.tick(30)
        t = t + 0.01

pygame.quit()
quit()
