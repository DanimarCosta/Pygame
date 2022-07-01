#Setup de Entrada - Import Bibliotecas-----------------------------------------#
import pygame, sys

#Setup de Entrada - Definições ----------------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Tela de Entrada')
screen = pygame.display.set_mode((800, 600),0,32)

font = pygame.font.SysFont(None, 30)

#Definição de Escrita de Texto-------------------------------------------------#
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

#Definição de ações do Menu Inicial--------------------------------------------#
def main_menu():
    while True:

        screen.fill((0,0,0))
        draw_text('Menu Principal', font, (255, 255, 255), screen, 330, 40)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 200, 200, 50)
        button_2 = pygame.Rect(300, 300, 200, 50)
        button_3 = pygame.Rect(300, 400, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                exite()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text('Jogar', font, (255, 255, 255), screen, 372, 215)
        draw_text('Opções', font, (255, 255, 255), screen, 363, 315)
        draw_text('Sair', font, (255, 255, 255), screen, 378, 415)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
        
#Definições dos Submenus dos Botões - Game - Opções - Sair --------------------#
def game():
    running = True
    while running:
        screen.fill((0,0,0))
        
        draw_text('Meu Jogo', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Opções', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def exite():
    pygame.quit()
    sys.exit()

           
main_menu()
