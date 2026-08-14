from .bebida_quente import BebidaQuente
from rich import print


class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água.")

    def servir(self):
        print("3. Servindo na canelca de porcelana com limão.")
        print("--- Bebida pronta ---")
