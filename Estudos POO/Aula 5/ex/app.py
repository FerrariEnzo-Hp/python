import os
import time
class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa com nome e idade
    blablabla
    blalblalglablalb
    allba;bablalbalbalb

    fim 
    """
    def __init__(self, nome = "", idade = 0):
        self.nome = nome
        self.idade = idade
    
    def aniversario(self):
        self.idade = self.idade + 1
    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'
    def __str__(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

g1 = Gafanhoto("Lucas", 56)
g1.aniversario()
g2 = Gafanhoto('Joana', 22)

print(g1)
print(g2)
print(Gafanhoto.__doc__)
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
