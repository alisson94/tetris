import pygame
import constantes
import random

formatos = {
    'T': {
        'x': 3,
        'y': 2,
        'matriz': [
            [0, 1, 0],
            [1, 1, 1]
        ]
    },
    'SQUARE': {
        'x': 2,
        'y': 2,
        'matriz': [
            [1, 1],
            [1, 1]
        ]
    },
    'LINHA': {
        'x': 4,
        'y': 1,
        'matriz': [
            [1, 1, 1, 1]
        ]
    },
    'L': {
        'x': 2,
        'y': 3,
        'matriz': [
            [1, 0],
            [1, 0],
            [1, 1]
        ]
    },
    'Z': {
        'x': 3,
        'y': 2,
        'matriz': [
            [1, 1, 0],
            [0, 1, 1]
        ]
    }
}

class Trick:
    def __init__(self, board): 
        self.board = board
        self.formato = random.choice(list(formatos.keys()))
        self.x = random.randint(0, board.quant_colunas - formatos[self.formato]['x'] - 1) * constantes.TAMANHO_GRID + board.offSetX
        self.y = board.offSetY - 2 * constantes.TAMANHO_GRID
        self.board = board
        self.matriz = formatos[self.formato]['matriz']
        self.iat = 0

    def desenhar(self, tela):

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):

                if self.matriz[i][j]:
                    x = self.x + j * constantes.TAMANHO_GRID
                    y = self.y + i * constantes.TAMANHO_GRID

                    if y >= self.board.offSetY:
                        pygame.draw.rect(tela, "white", (x , y, constantes.TAMANHO_GRID, constantes.TAMANHO_GRID))

    
    def descer(self): 
        
        if not self.seTrickChegouNoFinal() and not self.seColidiu():
            self.y += constantes.TAMANHO_GRID
            
    def girar(self):
        self.matriz = [list(reversed(col)) for col in zip(*self.matriz)]

    def moverLateralmente(self, direcao):
        if self.seEstaDentro(direcao):
            self.x += direcao * constantes.TAMANHO_GRID

    def seEstaDentro(self, direcao):
        return (self.x - self.board.offSetX + direcao  > 0 and 
                self.x - self.board.offSetX + direcao < (self.board.quant_colunas - formatos[self.formato]['x']) * constantes.TAMANHO_GRID )

    def seTrickChegouNoFinal(self):
        return (self.y >= self.board.quant_linhas * constantes.TAMANHO_GRID + self.board.offSetY - (len(self.matriz))*constantes.TAMANHO_GRID)
    
    def seColidiu(self):
        return(
            
        )