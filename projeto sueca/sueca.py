from random import shuffle
from rich import print, inspect
ordem = ["A", "7", "K", "J", "Q", "6", "5", "4", "3", "2"]
valores = {
    "A":11,
    "7":10,
    "K":4,
    "J":3,
    "Q":2,
    }
naipes = ["E", "C", "O", "P"]

class Carta:
    def __init__(self, valor, naipe):
        self.naipe = naipe
        self.valor = valor
    def __repr__(self):
        return f"{self.valor}{self.naipe}"

class Sueca:
    def __init__(self):
        self.baralho = self.gerar_baralho()
        self.maos = [[] for _ in range(4)]
        self.mesa = []
        self.turno = 0
        self.trunfo = None
        self.pontos = [0, 0]
    
    def gerar_baralho(self):
        return [Carta(v, n) for v in ordem for n in naipes]
    def distribuir_cartas(self):
        shuffle(self.baralho)
        for jogador in range(4):
            for rodada in  range(10):
                card = self.baralho.pop()
                self.maos[jogador].append(card)
    def definir_trunfo(self):
        self.trunfo = self.maos[3][-1].naipe
    def obter_naipe_mesa(self):
        return self.mesa[0][1].naipe
    def jogar_carta(self, jogador, carta):
        if jogador != self.turno:
            return False
        if carta not in self.maos[jogador]:
            return False
        if self.mesa:
            naipe_mesa = self.obter_naipe_mesa()
            tem_naipe = any(c.naipe == naipe_mesa for c in self.maos[jogador])
            if tem_naipe and carta.naipe != naipe_mesa:
                return False
        self.maos[jogador].remove(carta)
        self.mesa.append((jogador, carta))
        self.turno = (self.turno + 1) % 4
        return True
    def determinar_vencedor(self):
        naipe_mesa = self.obter_naipe_mesa()
        melhor_jogador, melhor_carta = self.mesa[0]

        for jogador, carta in self.mesa:
            if carta.naipe == self.trunfo:
                if melhor_carta.naipe != self.trunfo:
                    melhor_carta = carta
                    melhor_jogador = jogador
                else:
                    if valores.get(carta.valor, 0) > valores.get(melhor_carta.valor, 0):
                        melhor_carta = carta
                        melhor_jogador = jogador
            elif carta.naipe == naipe_mesa:
                if melhor_carta.naipe == naipe_mesa:
                    if valores.get(carta.valor, 0) > valores.get(melhor_carta.valor, 0):
                        melhor_carta = carta
                        melhor_jogador = jogador
                elif melhor_carta.naipe != self.trunfo:
                    melhor_carta = carta
                    melhor_jogador = jogador
        return melhor_jogador