from rich import print
from rich.traceback import install
install()

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro [red]{self.titulo}[/] que tem [yellow]{self.total_paginas} páginas no total[/], você agora está na página {self.pagina_atual}[/]")
    def avancar_paginas(self, qtd = 1):
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward:", end="")
                cont += 1
        print(f"[blue]você avançou {cont} e agora está na página {self.pagina_atual}[/]")
    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False
l1 = Livro("10 coisas que eu aprendi", 85)
l1.avancar_paginas(90)