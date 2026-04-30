from rich import print
from rich.traceback import install
from rich.panel import Panel
install()

class Churrasco:
    consumo_padrao:float = 0.400
    custo_kg:float = 82.40
    def __init__(self, evento, pessoas):
        self.evento = evento
        self.pessoas = pessoas
    def __str__(self):
        return f"Esse é o churrasco {self.evento} com {self.pessoas} pessoas participando"
    def calcular_qtd_carne(self) -> float:
        return Churrasco.consumo_padrao * self.pessoas
    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.custo_kg
    def custo_individual(self) -> float:
        return self.calcular_custo_total() / self.pessoas
    def analisar(self):
        conteudo = f"Analisando [green]{self.evento}[/green] com [blue]{self.pessoas} convidados[/blue]\n"
        conteudo += f"Cada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.custo_kg:,.2f}\n"
        conteudo += f"Recomendo [blue]comprar {self.calcular_qtd_carne():.3f}Kg[/blue] de carne\n"
        conteudo += f"O custo total será de [green]R${self.calcular_custo_total():,.2f}[/green]\n"
        conteudo += f"Cada pessoa pagará [yellow]R${self.custo_individual():,.2f}[/yellow] para participar"
        return Panel(conteudo, title=self.evento)
c1 = Churrasco("Churras da tropa", 10)
print(c1.analisar())
c2 = Churrasco("Finalzinho do ano", 67)
print(c2.analisar())

#a1 = Panel(f"Analisando [green]{self.evento}[/green] com [blue]{self.pessoas} convidados[/blue]\nCada participante comerá {self.qtcarne}Kg e cada Kg custa R${self.custo1kg:,.2f}\nRecomendo [blue]comprar {self.carnetotal}Kg[/blue] de carne\nO custo total será de [green]R${self.custototal:,.2f}[/green]\nCada pessoa pagará [yellow]R${self.custopessoa:,.2f}[/yellow] para participar", title=self.evento, width=110)