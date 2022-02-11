import pygame
from game import Game

jogo = Game()

while jogo.running:
    jogo.playing = True
    jogo.gameloop()