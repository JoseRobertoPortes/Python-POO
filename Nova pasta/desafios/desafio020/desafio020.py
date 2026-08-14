from rich import print
from rich.panel import Panel
from rich.traceback import install

install()


class Jogador:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def favoritos(self, *jogos):
        novos = set(self.jogos_favoritos).union(jogos)
        self.jogos_favoritos = sorted(novos)
        return self.jogos_favoritos

    def ficha(self):
        conteudo = f"Nome real: [black on blue]{self.nome}[/]\n" f"Jogos favoritos:"

        for game in self.jogos_favoritos:
            conteudo += f"\n:video_game: [blue]{game}[/]"

        return Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)


j1 = Jogador("José Roberto", "Portes")
j1.favoritos("Detroit Become Human", "CS2", "COD:Zombies", "Satisfactory")
print(j1.ficha())

j2 = Jogador("Olivia Rodrigo", "vampire")
j2.favoritos("Fortnite")
j2.favoritos("lixo")
print(j2.ficha())
