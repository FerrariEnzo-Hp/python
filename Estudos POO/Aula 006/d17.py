from rich import print
from rich.traceback import install
from rich.panel import Panel
install()
class Produto:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco
    def etiqueta(self):
        caixa = Panel(f'{self.produto}\nR${self.preco:,.2f}', title="Etiqueta", width=30)
        return caixa
c1 = Produto("Iphone", 15000)
print(c1.etiqueta())