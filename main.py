import pygame
import constantes
from classes.board import *
from classes.tricks import *
from classes.timer import *

class Game:
    def __init__(self):
        pygame.init()
        
        self.tela = pygame.display.set_mode(constantes.TAMANHO_TELA)
        pygame.display.set_caption(constantes.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(constantes.FONTE)

    def novo_jogo(self):
        self.jogando = True
        
        self.board = Board(self.tela, constantes.COLUNAS_BOARD, constantes.LINHAS_BOARD)

        self.timers = {
            'descer tricks': Timer(200, True, self.board.trickAtual.descer),
            'criar trick': Timer(300, False, self.board.criarTrick)
        }
        
        self.timers['descer tricks'].ativar()

        while self.jogando:
            
            self.eventos()
            self.atualizar()
            self.desenhar()
            

    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                
                self.esta_rodando = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.board.trickAtual.moverLateralmente(-1)
                elif event.key == pygame.K_d:
                    self.board.trickAtual.moverLateralmente(1)

    def atualizar(self):
        self.board.atualizar()
        self.atualizar_timers()
    
    def atualizar_timers(self):
        for timer in self.timers.values():
            timer.atualizar()

    def desenhar(self):
        self.tela.fill("purple")

        self.board.desenharGrid(self.tela, constantes.TAMANHO_GRID)
        self.board.desenharBoard()
        self.board.desenharTrickAtual()
       

        pygame.display.flip()

    def mostrar_texto(self, texto, tamanho, cor, x, y):
        fonte = pygame.font.Font(self.fonte, tamanho)

        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto, texto_rect)

    
    def tela_start(self):
        self.mostrar_texto("TETRIS v2.0", 50, "white", constantes.TAMANHO_TELA[0]/2, 300)

        pygame.display.flip()
        self.esperar_jogador()

    def esperar_jogador(self):
        esperando = False
        while esperando:
            self.relogio.tick(constantes.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False

                if event.type == pygame.KEYUP:
                    esperando = False


    def tela_gameover(self):
        pass


def main():
    game = Game()
    game.tela_start()

    while game.esta_rodando:
        game.novo_jogo()
        game.tela_gameover()

    pygame.quit()


if __name__ == "__main__":
    main()
