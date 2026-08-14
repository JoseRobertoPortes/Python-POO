from rich import print


class Termostato:
    def __init__(
        self,
    ):
        self.__temperatura: float = 24

    @property
    def temperatura(self):
        return f"{self.__temperatura}°C"

    @temperatura.setter
    def temperatura(self, valor: float):
        if 16 <= valor <= 30 and (valor * 10) % 10 in (0, 5):
            self.__temperatura = valor
        elif valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30
        else:
            raise ValueError(f"[red]Temperatura de {valor} é invalida.[/]")
