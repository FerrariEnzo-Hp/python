from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []
    def add_favorito(self, jogo):
        self.favoritos.append(jogo)
    def ficha(self):
        cont = "\n".join(str(item) for item in self.favoritos)
        p1 = Panel(f"Nome real: [black on blue]{self.nome}[/black on blue]\nJogos favoritos:\n[blue]{cont}[/blue]", title=f"Jogador <{self.nick}>")
        return p1
j1 = Gamer("Enzo Ferrari", "FerrariZô")
j1.add_favorito("Elden ring")
j1.add_favorito("Dark Souls 1")
j1.add_favorito("Dark Souls 2")
j1.add_favorito("Dark Souls 3")
print(j1.ficha())
