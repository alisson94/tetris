from pygame.time import get_ticks


class Timer():

    def __init__(self, duracao, repetir = False, func = None):
        self.duracao = duracao
        self.repetir = repetir
        self.funcao = func

        self.ativo = False
        self.tempo_inicial = 0

    def ativar(self):
        if self.ativo:
            return
        self.ativo = True
        self.tempo_inicial = get_ticks()

    def desativar(self):
        self.ativo = False
        self.tempo_inicial = 0

    def atualizar(self):
        self.tempo_atual = get_ticks()

        if self.tempo_atual - self.tempo_inicial >= self.duracao and self.ativo:

            if self.funcao and self.tempo_inicial != 0:
                
                self.funcao()

            self.desativar()

            if self.repetir:
                self.ativar()
        

