import locale
from rich import print
from rich.panel import Panel


from rich.traceback import install

install()
locale.setlocale(locale.LC_ALL, "")


class Produto:
    def __init__(self, nome="", preco=0):
        self.nome = nome.upper()
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += "_" * 30
        conteudo += locale.currency(self.preco).center(30, "_")
        caixa = Panel(conteudo, title="PRODUTOS", width=34)
        print(caixa)


p1 = Produto("Iphone 17 pro max", 8_000)
p2 = Produto("Notebook Gamer", 5_500)
Produto.etiqueta(p1)
Produto.etiqueta(p2)
