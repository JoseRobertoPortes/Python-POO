from rich import print
from rich.traceback import install

install()


class Caneta:
    def __init__(self, cor="azul"):
        self.cor = cor.lower().strip()
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def escrever(self, texto):
        if not self.tampada:
            if self.cor == "verde":
                print(f"[green]{texto}[/]")

            elif self.cor in ("vermelho", "vermelha"):
                print(f"[red]{texto}[/]")

            elif self.cor == "azul":
                print(f"[blue]{texto}[/]")
        else:
            print(f"Você esqueceu de destampar a caneta {self.cor}.")
