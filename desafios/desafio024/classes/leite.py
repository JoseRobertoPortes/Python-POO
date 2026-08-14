from rich import print
from .bebida_quente import BebidaQuente


class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico do leite")

    def servir(self):
        print("3. Servindo na caneca grande, já com café.")
        print("--- Bebida pronta ---")
