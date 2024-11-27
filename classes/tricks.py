import pygame
import constantes
import random

formatos = {
    0: {'x': 3,
        'y': 2,
        'matriz': [[0,1,0],
                    [1,1,1]]},
    1: {'x': 2,
        'y': 2,
        'matriz': [[1,1],
                   [1,1]]}

}

class Trick:
    def __init__(self, board):
        self.formato = random.randint(0, 1)
        self.x = random.randint(0, board.quant_colunas - 1 - formatos[self.formato]['x']) * constantes.TAMANHO_GRID + board.offSetX
        self.y = board.offSetY
        self.board = board
        self.matriz = formatos[self.formato]['matriz']

    def desenhar(self, tela):
        
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):

                if self.matriz[i][j]:
                    x = self.x + j * constantes.TAMANHO_GRID
                    y = self.y + i * constantes.TAMANHO_GRID

                    pygame.draw.rect(tela, "white", (x , y, constantes.TAMANHO_GRID, constantes.TAMANHO_GRID))

    def descer(self):   

        if self.y < self.board.quant_linhas * constantes.TAMANHO_GRID + self.board.offSetY - (len(self.matriz))*constantes.TAMANHO_GRID:
            self.y += constantes.TAMANHO_GRID
            

    def mover(self, direcao):
        if self.estaDentro():
            self.x += direcao * constantes.TAMANHO_GRID

    def estaDentro(self):
        return True

