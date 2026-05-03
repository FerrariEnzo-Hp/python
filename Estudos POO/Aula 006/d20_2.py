from rich import print
from rich.panel import Panel
from rich.traceback import install
install()
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()
    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)
    def ficha(self):
        conteudo = f"Nome real: [black on blue] {self.nome} [/]\n"
        conteudo += f"Jogos Favoritos: "
        for num, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: [blue]{game}[/]"
        painel = Panel(conteudo, title=self.nick, width=40)
        print(painel)
j1 = Gamer("Enzo Ferrari", "FerrariZô")
j1.add_favoritos("Sekiro")
j1.add_favoritos("Dark Souls")
j1.add_favoritos("Elden Ring")
j1.add_favoritos("Dark Souls II")
j1.add_favoritos("Armored Core V")
j1.ficha()
