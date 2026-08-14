from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column("Nome", justify="left")
tabela.add_column("Preço", justify="left")

tabela.add_row("Lápis", "R$1,50")
tabela.add_row("Borracha", "R$5,00")

print(tabela)
