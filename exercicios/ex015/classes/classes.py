from uteis.dinheiro import formatar_moeda


class Carteira:
    def __init__(self, saldo: int | float = 0):
        self.__saldo = saldo

    def __str__(self) -> str:
        return f'Você tem {self.fmoeda} na carteira'

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError('Você não tem autorização para isso')

    @property
    def fmoeda(self):
        return formatar_moeda(self.saldo)

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError('O valor do depósito deve ser positivo')
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError('O valor do saque deve ser positivo')
        if valor > self.__saldo:
            raise ValueError('Saldo insuficiente')
        self.__saldo -= valor

    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False

    def __iadd__(self, valor: int | float):
        self.depositar(valor)
        return self

    def __isub__(self, valor: int | float):
        self.sacar(valor)
        return self

    def __le__(self, other):
        if self.saldo <= other.saldo:
            return True

        else:
            return False