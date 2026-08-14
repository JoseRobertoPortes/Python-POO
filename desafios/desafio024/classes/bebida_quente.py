from abc import ABC, abstractmethod
from rich import print


class BebidaQuente(ABC):
    """Classe base para bebidas quentes."""

    def __init__(self):
        print("--- Iniciando o processo ---")

    def preparar(self):
        print("1. Fervendo água a 100 graus Celsius.")
        self.misturar()
        self.servir()

    def ferver_agua(self):
        return "Água fervida"

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass
