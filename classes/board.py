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
        self.trickAtual = None

        self.criarTrick()

    def atualizar(self):
        if self.trickAtual.y + formatos[self.trickAtual.formato]['y'] * constantes.TAMANHO_GRID == self.offSetY + self.quant_linhas * constantes.TAMANHO_GRID:
            self.trickToBoard()
            self.criarTrick()

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

    def trickToBoard(self):
        formatoTrick = self.trickAtual.matriz
        for j, linha in enumerate(formatoTrick):
            y = self.quant_linhas - len(formatoTrick) + j
            for i, coluna in enumerate(linha):
                x = int((self.trickAtual.x - self.offSetX) / constantes.TAMANHO_GRID) + i
                
                if formatoTrick[j][i] == 1:
                    self.matriz[y][x] = 1

    def desenharBoard(self):
        for i in range(self.quant_linhas):
            for j in range(self.quant_colunas):

                if self.matriz[i][j] == 1:
                    x = self.offSetX + j * constantes.TAMANHO_GRID
                    y = self.offSetY + i * constantes.TAMANHO_GRID

                    pygame.draw.rect(self.tela, "red", (x , y, constantes.TAMANHO_GRID, constantes.TAMANHO_GRID))

    def desenharTrickAtual(self):
        self.trickAtual.desenhar(self.tela)

