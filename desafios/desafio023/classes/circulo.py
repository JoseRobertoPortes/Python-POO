from .poligono import Poligono


class Circulo(Poligono):
    def __init__(self, raio):

        self.raio = raio

    def perimetro(self):
        return (2 * 3.14) * self.raio

    def area(self):
        return 3.14 * self.raio**2
