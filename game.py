from pickle import TRUE
from tkinter import font
import pygame

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        self.DISPLAY_W,self.DISPLAY_H = 1280, 720
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))

        self.font_name = '8-BIT WONDER.TTF'
        #self.font_name = pygame.font.get_default_font()

        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)

    def gameloop(self):
        while self.playing:
            self.check_events()

            if self.START_KEY:
                self.playing = False

            self.display.fill(self.BLACK)
            self.draw_text('Obrigado Por Jogar!', 20, self.DISPLAY_W / 2, self.DISPLAY_H / 2)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = TRUE

            if event.type == pygame.K_BACKSPACE:
                self.BACK_KEY = TRUE
            
            if event.type == pygame.K_DOWN:
                self.DOWN_KEY = TRUE

            if event.type == pygame.K_UP:
                self.UP_KEY = TRUE
    
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)