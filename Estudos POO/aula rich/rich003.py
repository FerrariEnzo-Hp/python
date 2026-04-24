from rich import print
from rich.table import Table as tb
tabela = tb(title='Tabela de Preços')

tabela.add_column('Nome')
tabela.add_column('Preço')

print(tabela)