from rich import print
from rich.traceback import install
from rich import inspect
install()

class Funcionario:
    #atributos de classe
    empresa = "Curso em Vídeo"
    def __init__(self, nome, setor, cargo):
        #atributos de instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}'
c1 = Funcionario('Julinho', "limpeza", "Chefe da equipe")
c2 = Funcionario('Pedro', 'Ti', 'Gerente')
#inspect()
#Funcionario.empresa = "Megga Brindes"
print(c2.apresentacao())
print(c1.apresentacao())