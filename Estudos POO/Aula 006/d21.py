from rich import print
from rich.traceback import install
install()

class Caneta:
    def __init__(self, cor):
        self.estado = True
        self.dicionario = {'vermelho':'red',
                            'azul':'blue',
                            'amarelo':'yellow',
                            'branco':'white',
                            'verde':'green',
                            'rosa':'pink',
                            'preto':'black'}
        self.cor = self.dicionario[f'{cor}']
    def destampar(self):
        self.estado = False
        return f"caneta {self.cor} está destampada!"
    def escrever(self, texto):
        self.texto = texto
        if self.estado == False:
            return f'[{self.cor}]{texto}[/]'
        else:
            return ":prohibited: a caneta está tampada"
c1 = Caneta("verde")
c1.destampar()
print(c1.escrever("Oi tudo bem?"))