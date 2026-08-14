from abc import ABC, abstractmethod
from .real import Real
from rich.traceback import install

install()


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def cal_frete(self):
        pass


class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50

    def cal_frete(self):
        frete = self.fator * self.distancia
        return Real(frete)


class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.10

    def cal_frete(self):
        if self.distancia > 10:
            return "Frete não disponível."
        frete = self.fator * self.distancia
        return Real(frete)


class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.00

    def cal_frete(self):
        if self.distancia < 50:
            return "Frete não disponivel."
        frete = self.fator * self.distancia
        return Real(frete)
