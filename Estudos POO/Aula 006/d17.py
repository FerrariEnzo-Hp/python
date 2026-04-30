from rich import print
from rich.traceback import install
from rich.panel import Panel
install()
class Produto:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco
    def etiqueta(self):
        conteudo = f"{self.produto.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        caixa = Panel(f'{conteudo}', title="Etiqueta", width=34)
        return caixa
c1 = Produto("Iphone", 15000)
print(c1.etiqueta())
c2 = Produto("Tectoy", 800)
print(c2.etiqueta())