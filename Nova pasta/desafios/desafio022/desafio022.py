from tkinter.font import BOLD
from typing import Self

from rich import print
from rich.traceback import install
from rich.panel import Panel

install()


class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 5
    volume_min: int = 1
    volume_max: int = 4

    def __init__(self, canal=1, volume=2):
        self.canal_atual = canal
        self.volume_atual = volume
        self.ligado = False

    def Liga_Desliga(self):
        self.ligado: bool = not self.ligado

    def canal_mais(self):
        if self.canal_atual == self.canal_max:
            self.canal_atual = self.canal_min
        else:
            self.canal_atual += 1

    def canal_menos(self):
        if self.canal_atual == self.canal_min:
            self.canal_atual = self.canal_max
        else:
            self.canal_atual -= 1

    def volume_mais(self):
        if self.volume_atual == self.volume_max:
            self.volume_atual = self.volume_min
        else:
            self.volume_atual += 1

    def volume_menos(self):
        if self.volume_atual == self.volume_min:
            self.volume_atual = self.volume_max
        else:
            self.volume_atual -= 1

    def televisao(self):
        conteudo = ""
        if not self.ligado:
            conteudo = f"[red]A Tv está desligada.[/]\n"
        else:
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[yellow on yellow] {self.canal_atual} [/]"
                else:
                    conteudo += f"[black on gray] {canal} [/]"

            conteudo += "\n"
            for volume in range(
                ControleRemoto.volume_min, ControleRemoto.volume_max + 1
            ):
                if volume <= self.volume_atual:
                    conteudo += f"[white on cyan] . [/]"
                else:
                    conteudo += f"[white on gray] . [/]"
            conteudo += "\n"

        tv = Panel(f"{conteudo}", title="TV", width=40, height=5)
        print(tv)


c = ControleRemoto()

while True:
    c.televisao()
    comando = str(input(f"<|CH{c.canal_atual}|>      -|VOL{c.volume_atual}|+ "))
    match comando:
        case "0":
            break
        case "@":
            c.Liga_Desliga()
        case ">":
            c.canal_mais()
        case "<":
            c.canal_menos()
        case "+":
            c.volume_mais()
        case "-":
            c.volume_menos()
