from .bebida_quente import BebidaQuente
from rich import print


class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Passando água pressurizada pelo pó de cafe moído.")

    def servir(self):
        print("3. Servindo em xícara pequena")
        print("--- Bebida pronta ---")
