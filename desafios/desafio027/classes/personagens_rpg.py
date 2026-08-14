from abc import ABC, abstractmethod
from random import choice, randint, random


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

        golpes = []

    def Atacar(self, alvo):
        self.forca = randint(0, 100)

        if self.__class__.__name__ == "Guerreiro":
            golpes = [
                "Desferiu um Golpe Demolidor",
                "Executou um Corte Redemoinho",
                "Avançou com a Investida do Touro",
                "Usou um Golpe Provocador",
                "Aplicou uma Estocada Perfurante",
            ]
        elif self.__class__.__name__ == "Mago":
            golpes = [
                "Lançou uma Bola de Fogo",
                "Disparou Setas Mágicas",
                "Invocou um Relâmpago",
                "Conjurou uma Explosão Arcana",
                "Lançou um Raio de Gelo",
            ]

        forma_de_ataque = choice(golpes)
        alvo_nome = alvo.nome
        if self.vida <= 0 or alvo.vida <= 0:
            print("O ataque nao pode ser efetuado.")
        else:

            resultado_ataque = f"[blue]{self.nome}[/]({self.vida}) {forma_de_ataque} em {alvo_nome}({alvo.vida}) causando [red]{self.forca} de dano.[/]"

            retorno_dano = alvo.Receber_Dano(self.forca, atacante=self.nome)

            return resultado_ataque + "\n" + retorno_dano

    def Receber_Dano(self, dano: int, atacante: str | None = None):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        atacante_txt = f" por {atacante}" if atacante else ""
        return f"{self.nome} recebeu {dano} de dano{atacante_txt}! [green]Vida restante: {self.vida}[/]"

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
        curas = [
            "Usou uma Poção de Cura",
            "Descansou na Fogueira",
            "Consumiu Rações de Viagem",
            "Recebeu uma Bênção Curativa",
            "Aplicou Bandagens nos Ferimentos",
            "Recuperou o Fôlego",
            "Ativou o Elixir de Regeneração",
        ]
        forma_de_cura = choice(curas)
        recuperar = randint(0, 100)
        self.vida += recuperar
        return f"[green]{self.nome} {forma_de_cura} e recuperou {recuperar} de vida![/]"


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self):
        curas = [
            "Lançou uma Simpatia Arcana",
            "Ativou uma Aurea de Regeneração",
            "Usou uma Poção de Mana e Cura",
            "Invocou a Graça do Planalto Elemental",
            "Conjurou um Ritual de Reconstituição",
            "Usou uma Poção Transmutativa de Alquimia",
        ]
        forma_de_cura = choice(curas)
        recuperar = randint(0, 100)
        self.vida += recuperar
        return f"{self.nome} {forma_de_cura} e recuperou {recuperar} de vida!"
