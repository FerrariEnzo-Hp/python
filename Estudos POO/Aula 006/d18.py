from rich import print
from rich.traceback import install
from rich.panel import Panel
install()

class Churrasco:
    def __init__(self, evento, pessoas):
        self.evento = evento
        self.pessoas = pessoas
        self.qtcarne = 0.4
        self.carnetotal = float(pessoas)*self.qtcarne
        self.custo1kg = 82.40
        self.custototal = self.carnetotal*self.custo1kg
        self.custopessoa = self.custototal/self.pessoas
    def analisar(self):
        a1 = Panel(f"Analisando [green]{self.evento}[/green] com [blue]{self.pessoas} convidados[/blue]\nCada participante comerá {self.qtcarne}Kg e cada Kg custa R${self.custo1kg:,.2f}\nRecomendo [blue]comprar {self.carnetotal}Kg[/blue] de carne\nO custo total será de [green]R${self.custototal:,.2f}[/green]\nCada pessoa pagará [yellow]R${self.custopessoa:,.2f}[/yellow] para participar", title=self.evento, width=110)
        return a1
c1 = Churrasco("Churras da tropa", 100)
print(c1.analisar())