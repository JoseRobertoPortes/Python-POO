from rich import print
from time import sleep


class Livro:
    def __init__(self, livro: str, paginas: int):
        self.livro = livro
        self.paginas = paginas
        self.pagina_atual = 1
        self.paginas_faltando = self.paginas

        print(
            f"Você acabou de abrir o livro [red]'{self.livro}'[/red] que tem [green]{self.paginas} páginas no total[/green].\nVocê agora está na página 1\n"
        )

    def avancar_paginas(self, avancar: int):
        if self.paginas_faltando == 0:
            print(f"Você já terminou de ler o livro '{self.livro}'.\n")
            return

        if avancar > self.paginas_faltando:
            print(
                f"Não é possível avançar {avancar} páginas, pois faltam apenas {self.paginas_faltando} páginas.\n"
            )
        else:
            print(f"[blue]Avançando {avancar} páginas...[/blue]")

            for i in range(avancar):
                sleep(0.3)
                print(f"pag{self.pagina_atual}", end=" → ")
                self.pagina_atual += 1
                self.paginas_faltando -= 1

            print()
            print(
                f"Você avançou {avancar} páginas e agora está na página {self.pagina_atual}.\n"
            )

            if self.paginas_faltando == 0:
                print(f'Você chegou ao final do livro [red]"{self.livro}"[/red]!\n')


li = Livro("oi", 15)
li.avancar_paginas(5)
li.avancar_paginas(6)
