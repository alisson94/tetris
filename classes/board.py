import pygame
from classes.tricks import *

class Board:
    def __init__(self, tela, x, y):
        self.tela = tela
        self.quant_colunas = x
        self.quant_linhas = y
        self.matriz = [[0]*10 for _ in range(20) ]
        self.offSetX = 20
        self.offSetY = 20
        self.tricks = []
        self.trickAtual = None

        temp_trick = Trick(self)
        self.trickAtual = temp_trick
        self.tricks.append(temp_trick)

    def atualizar(self):
        pass

    def desenharGrid(self, tela, tamanho):
        x_fim = self.offSetX + self.quant_colunas * tamanho  + 1
        y_fim = self.offSetY + self.quant_linhas * tamanho  + 1

        for i in range(self.offSetX, x_fim, tamanho):
            pygame.draw.line(tela, "white", (i, self.offSetY), (i, y_fim))
        for i in range(self.offSetY, y_fim+1, tamanho):
            pygame.draw.line(tela, "white", (self.offSetX, i), (x_fim, i))
    
    def criarTrick(self):
        trick = Trick(self)

        self.trickAtual = trick


    def desenharTrickAtual(self):
        self.trickAtual.desenhar(self.tela)

