import locale
from rich import print
from rich.panel import Panel
from rich.traceback import install

install()
locale.setlocale(locale.LC_ALL, "")


class Churrasco:
    def __init__(self, titulo: str, quant: int):
        self.titulo = titulo
        self.quant = quant

    def analisar(self):

        kg = 0.4 * self.quant
        custo = 82.40 * kg
        custopp = custo / self.quant
        conteudo = f"Analisando [green]{self.titulo}[/green] com [blue]{self.quant} convidados[/blue]\n"
        conteudo += f"Cada participante comerá 0.4KG e cada KG de carne custa {locale.currency(82.40, grouping=True)}\n"
        conteudo += f"Recomento comprar [blue]{kg:.1f}KG de carne[/blue]\n"
        conteudo += f"O custo total será {locale.currency(custo, grouping=True)}\n"
        conteudo += f"Cada pessoa pagará [yellow]{locale.currency(custopp, grouping=True)}[/yellow] pra participar\n"
        caixa = Panel(conteudo, title=self.titulo)
        print(caixa)


churrasco = Churrasco("Churras dos amigos", 15)
Churrasco.analisar(churrasco)
