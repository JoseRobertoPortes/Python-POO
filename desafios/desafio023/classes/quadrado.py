from .poligono import Poligono


class Quadrado(Poligono):
    def __init__(self, lado):

        self.lado: int = lado

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado * self.lado
