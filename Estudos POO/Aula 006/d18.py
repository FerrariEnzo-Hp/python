from rich import print
from rich.traceback import install
from rich.panel import Panel
install()

class Churrasco:
    qtcarne = 0.4
    custo1kg = 82.40
    def __init__(self, evento, pessoas):
        self.evento = evento
        self.pessoas = pessoas
        self.custototal = self.qtcarne*self.pessoas*self.custo1kg
        self.custopessoa = self.custototal/self.pessoas
    def analisar(self):
        conteudo = f"Analisando [green]{self.evento}[/green] com [blue]{self.pessoas} convidados[/blue]\n"
        conteudo += f"Cada participante comerá {Churrasco.qtcarne}Kg e cada Kg custa R${self.custo1kg:,.2f}\n"
        conteudo += f"Recomendo [blue]comprar {Churrasco.qtcarne*self.pessoas}Kg[/blue] de carne\n"
        conteudo += f"O custo total será de [green]R${self.custototal:,.2f}[/green]\n"
        conteudo += f"Cada pessoa pagará [yellow]R${self.custopessoa:,.2f}[/yellow] para participar"
        return Panel(conteudo, title=self.evento)
c1 = Churrasco("Churras da tropa", 10)
print(c1.analisar())

#a1 = Panel(f"Analisando [green]{self.evento}[/green] com [blue]{self.pessoas} convidados[/blue]\nCada participante comerá {self.qtcarne}Kg e cada Kg custa R${self.custo1kg:,.2f}\nRecomendo [blue]comprar {self.carnetotal}Kg[/blue] de carne\nO custo total será de [green]R${self.custototal:,.2f}[/green]\nCada pessoa pagará [yellow]R${self.custopessoa:,.2f}[/yellow] para participar", title=self.evento, width=110)