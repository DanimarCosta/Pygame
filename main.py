import pygame, sys
from button import Button
import tkinter as tk
import time 

# Pega as dimenções da tela
janela_tk = tk.Tk()
largura_janela, altura_janela = (janela_tk.winfo_screenwidth()), (janela_tk.winfo_screenheight())

# Inicia a instancia do pygame
pygame.init()
pygame.mixer.init()

# Configurações iniciais da tela
SCREEN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
pygame.display.set_caption("Menu")
BG = pygame.image.load("assets/Main Menu/background.jpg")
pygame.display.set_caption('Jogo do EL Giorgio')

# Cria uma função para passar a fonte
def get_font(size): 
    return pygame.font.Font("assets/8-BIT WONDER.TTF", size)

# Função que carrega as informações do jogo
def play():
    while True:
        # JOGO
        largura_janela = 1280
        altura_janela = 740
        clock = pygame.time.Clock()

        # Carrega os arquivos de imagens
        fgExit = True
        personagemImg = pygame.image.load('assets\eu.png')
        cenario = pygame.image.load('assets\cenario.jpg')
        tela = pygame.display.set_mode((largura_janela, altura_janela))

        # Configurações da janela e declarações de variavel
        x = (largura_janela * 0.1)
        y = (altura_janela * 0.1)
        x1 = 0
        x2 = 0
        y1 = 0
        y2 = 0

        # Velocidade do movimento
        speed_x = 10
        speed_y = 10

        # Realiza o mivimento dos personagens
        while fgExit:
            # Detecta qual tecla foi pressionada
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
                        x1 = - speed_x
                        
                        # Som de passos
                        effect = pygame.mixer.Sound('assets\passos.ogg')
                        effect.set_volume(9.0)
                        effect.play()
                    if event.key == pygame.K_RIGHT:
                        x2 = speed_x

                        # Som de passos
                        effect = pygame.mixer.Sound('assets\passos.ogg')
                        effect.set_volume(9.0)
                        effect.play()
                    if event.key == pygame.K_UP:
                        y1 = - speed_y

                        effect2 = pygame.mixer.Sound('assets\pulo_personagem.ogg')
                        effect2.set_volume(0.5)
                        effect2.play()
                    
                    if event.key == pygame.K_DOWN:
                        y2 = speed_y

                        effect2 = pygame.mixer.Sound('assets\pulo_personagem.ogg')
                        effect2.set_volume(0.5)
                        effect2.play()

                if pygame.key.get_pressed()[ord('f')] == 1:
                    main_menu()

            # aplica o movimento ao objeto
            x += x1 + x2
            y += y1 + y2
            #print('PosX é de:', x, 'e a PosY é de:', y)
            
            tela.blit(cenario,(0,0))
            tela.blit(personagemImg, (x, y))
            pygame.display.update()
            clock.tick(60)
        
        # FIM

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("janela do Jogo.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        # Fecha a tela quando o x do windows é precionado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fgExit = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        
        # atuliza o display
        pygame.display.update()

# Carrega a pagina de configurações do jogo
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        # Configurações dos botões
        OPTIONS_TEXT = get_font(45).render("Janela de configs do Jogo.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        # Retorna ao menu principal
        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        # Muda a cor quando o mause passa por cima
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        # Sai do sistema caso o botão equivalente ao esc é precionados
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def main_menu():
    # Configurações da musica de fundo
    pygame.mixer.music.load ("assets/Soundtrack/lofi.mp3")
    pygame.mixer.music.play(0)
    pygame.mixer.music.set_volume(0.7)

    # Executa infinitamente até a tecla esc ou f(durande o jogo) seje precionada
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        # Configurações dos botões
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Main Menu/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Main Menu/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Main Menu/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Aplica a mudança de cor quando o mause passa por cima dos botões
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        # Fecha o jogo quando o x do windows é clicado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Chega quando o botão é pressionad
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        # Atualiza a tela
        pygame.display.update()

# inicia o programa incials
main_menu()