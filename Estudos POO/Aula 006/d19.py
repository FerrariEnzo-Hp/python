from rich import print
from rich.traceback import install
install()

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = abs(paginas)
        self.pagina_atual = 0
    def abrir_livro(self):
        if self.pagina_atual == 0:
            self.pagina_atual += 1
            return f"Você pegou o livro {self.titulo}\nAbrindo Livro... Você está na página 1"
        else:
            return "Livro já está aberto\nVocê está na página 1"
    def avancar_paginas(self, avancar):
        self.avancar = avancar
        if self.pagina_atual == 0:
            return f'Livro Fechado, não é possivel avançar páginas'
        while self.avancar != self.pagina_atual:
            if self.pagina_atual < self.paginas:
                self.pagina_atual += 1
                print(f"avançando páginas, pagina atual {self.pagina_atual}")
            else:
                return f"Chegamos ao final do livro"
        else:
            return f'Chegamos a página {self.pagina_atual}'
c1 = Livro("teste", 20)
print(c1.abrir_livro())
print(c1.abrir_livro())
print(c1.avancar_paginas(30))