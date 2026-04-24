from rich import print
from rich.traceback import install
from rich import inspect
install()

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa curso em vídeo'
    
c2 = Funcionario('Pedro', 'Ti', 'Gerente')
inspect(c2)
print(c2.apresentacao())