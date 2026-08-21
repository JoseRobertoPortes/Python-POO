from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print
from rich.traceback import install
install()


class Mensagem(ABC):
    def __init__(self, mensagem):
        self._mensagem = mensagem

    @abstractmethod
    def mostrar(self):
        pass


class Aviso(Mensagem):
    def mostrar(self):
        print(
            Panel(
                f'{self._mensagem}',
                title=':speech_balloon: AVISO :speech_balloon:',
                title_align='center',
                border_style='white',
                style='white on black',
                width=40,
            )
        )


class Alerta(Mensagem):
    def mostrar(self):
        print(
            Panel(
                f'{self._mensagem}',
                title=':warning: ALERTA :warning:',
                title_align='center',
                border_style='black',
                style='black on yellow',
                width=40,
            )
        )


class Erro(Mensagem):
    def mostrar(self):
        print(
            Panel(
                f'{self._mensagem}',
                title=':no_entry_sign: ERRO :no_entry_sign:',
                border_style='yellow',
                title_align='center',
                style='yellow on red',
                width=40,
            )
        )
