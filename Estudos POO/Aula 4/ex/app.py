class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0
    
    def aniversario(self):
        self.idade = self.idade + 1
    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

g1 = Gafanhoto()
g1.nome = "Juca"
g1.idade = 34
g1.aniversario()

g2 = Gafanhoto()
g2.nome = 'Joana'
g2.idade = 22

print(g1.mensagem())
print(g2.mensagem())