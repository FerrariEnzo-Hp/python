from rich import print
from rich.traceback import install
install()
class Caneta:
    def __init__(self, cor = "azul"):
        self.tampada = True
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
    def destampar(self) -> bool:
        self.tampada = False
    def escrever(self, msg):
        if  self.tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada")
        else:
            print(f"{self.cor}{msg}[/]", end="")
    def quebrar_linha(self, qtd = 1):
        print("\n"*qtd, end="")

c1 = Caneta("AzUl")
c2 = Caneta("Vermelha")
c3 = Caneta("Verde")

c1.destampar()

c3.destampar()

c1.escrever("aaaaaa ")
c2.escrever("aaaaaa ")
c3.escrever("aaaaaa")