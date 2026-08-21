from abc import ABC, abstractmethod
from uteis.dinheiro import formatar_moeda

class Pagamento(ABC):
    def __init__(self, valor):
        self._valor = valor

    @property
    def fvalor(self):
        return f'{formatar_moeda(self._valor)}'

    @abstractmethod
    def pagar(self):
        pass


class Boleto(Pagamento):
    def pagar(self):
        print(f'Pagamento CONFIRMADO de {self.fvalor} via Boleto')


class Pix(Pagamento):
    def pagar(self):
        print(f'Pagamento CONFIRMADO de {self.fvalor} via Pix')


class Credito(Pagamento):
    def __init__(self, valor, parcelas=1):
        super().__init__(valor)
        self.parcelas = parcelas

    def pagar(self):
        print(
            f'Pagamento CONFIRMADO de {self.fvalor} via Crédito em {self.parcelas}x')


def finalizar_compra(forma_pagamento):
    forma_pagamento.pagar()
