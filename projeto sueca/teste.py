import random

# Ordem de força na Sueca
ORDEM = ["2", "3", "4", "5", "6", "D", "V", "R", "7", "A"]
VALORES = {
    "A": 11,
    "7": 10,
    "R": 4,
    "V": 3,
    "D": 2
}

NAIPES = ["♠", "♥", "♦", "♣"]


class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return f"{self.valor}{self.naipe}"


class JogoSueca:
    def __init__(self):
        self.baralho = self.criar_baralho()
        self.maos = [[] for _ in range(4)]
        self.mesa = []
        self.turno = 0
        self.trunfo = None
        self.pontos = [0, 0]  # dupla 0 (0 e 2), dupla 1 (1 e 3)

    def criar_baralho(self):
        return [Carta(v, n) for v in ORDEM for n in NAIPES]

    def embaralhar(self):
        random.shuffle(self.baralho)

    def distribuir(self):
        for i in range(10):
            for j in range(4):
                self.maos[j].append(self.baralho.pop())

        # Define trunfo pela última carta distribuída
        self.trunfo = self.maos[-1][-1].naipe

    def carta_valida(self, jogador, carta):
        mao = self.maos[jogador]

        if carta not in mao:
            return False

        if not self.mesa:
            return True

        naipe_mesa = self.mesa[0][1].naipe
        tem_naipe = any(c.naipe == naipe_mesa for c in mao)

        if tem_naipe and carta.naipe != naipe_mesa:
            return False

        return True

    def jogar_carta(self, jogador, carta):
        if not self.carta_valida(jogador, carta):
            raise ValueError("Jogada inválida")

        self.maos[jogador].remove(carta)
        self.mesa.append((jogador, carta))

    def comparar_cartas(self, c1, c2, naipe_mesa):
        # Trunfo ganha sempre
        if c1.naipe == self.trunfo and c2.naipe != self.trunfo:
            return c1
        if c2.naipe == self.trunfo and c1.naipe != self.trunfo:
            return c2

        # Mesmo naipe → comparar força
        if c1.naipe == c2.naipe:
            return c1 if ORDEM.index(c1.valor) > ORDEM.index(c2.valor) else c2

        # Seguir naipe da mesa
        if c1.naipe == naipe_mesa:
            return c1
        return c2

    def determinar_vencedor(self):
        naipe_mesa = self.mesa[0][1].naipe
        vencedor, melhor = self.mesa[0]

        for jogador, carta in self.mesa[1:]:
            melhor_carta = self.comparar_cartas(melhor, carta, naipe_mesa)
            if melhor_carta == carta:
                vencedor = jogador
                melhor = carta

        return vencedor

    def calcular_pontos_rodada(self):
        pontos = 0
        for _, carta in self.mesa:
            pontos += VALORES.get(carta.valor, 0)
        return pontos

    def jogar_rodada(self):
        for i in range(4):
            jogador = (self.turno + i) % 4
            mao = self.maos[jogador]

            # jogada automática simples (primeira carta válida)
            for carta in mao:
                if self.carta_valida(jogador, carta):
                    self.jogar_carta(jogador, carta)
                    break

        vencedor = self.determinar_vencedor()
        pontos = self.calcular_pontos_rodada()

        dupla = 0 if vencedor % 2 == 0 else 1
        self.pontos[dupla] += pontos

        self.mesa = []
        self.turno = vencedor

    def jogar_partida(self):
        self.embaralhar()
        self.distribuir()

        while any(self.maos):
            self.jogar_rodada()

        return self.pontos


if __name__ == "__main__":
    jogo = JogoSueca()
    resultado = jogo.jogar_partida()

    print("Resultado final:")
    print(f"Dupla 0 (Jogadores 0 e 2): {resultado[0]} pontos")
    print(f"Dupla 1 (Jogadores 1 e 3): {resultado[1]} pontos")