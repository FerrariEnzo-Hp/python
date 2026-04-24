from rich import print
from rich.traceback import install
install()

class Caneta:
    def __init__(self, cor):
        self.estado = True
        self.dicionario = {'vermelho':'red', 'azul':'blue', 'branco':'white', 'verde':'green', 'rosa':'pink'}
        self.cor = self.dicionario[f'{cor}']
    def destampar(self):
        self.estado = False
        return f"caneta {self.cor} está destampada!"
    def escrever(self, texto):
        self.texto = texto
        if self.estado == False:
            return f'[{self.cor}]{texto}[/]'
        else:
            return "a caneta está tampada"
c1 = Caneta("vermelho")
c1.destampar()
print(c1.escrever("Oi tudo bem?"))