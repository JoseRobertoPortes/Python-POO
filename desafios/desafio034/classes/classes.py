from abc import ABC, abstractmethod
from uteis.dinheiro import formatar_moeda


class Funcionario(ABC):
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, novo_salario: float):
        if novo_salario > self._salario:
            self._salario = novo_salario
            print('Salário atualizado com sucesso!')
        elif novo_salario == self._salario:
            print('O salário informado é igual ao atual.')
        else:
            raise ValueError(
                'Você não pode abaixar o salário de um funcionário.')

    @property
    def salario_formatado(self):
        return formatar_moeda(self._salario)

    @abstractmethod
    def calcularbonus(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} | Nome: {self.nome} | Salário: {self.salario_formatado}"


class Gerente(Funcionario):
    def calcularbonus(self):
        percentual = 15 / 100
        return self._salario * percentual


class Dev(Funcionario):
    def calcularbonus(self):
        percentual = 10 / 100
        return self._salario * percentual


class Designer(Funcionario):
    def calcularbonus(self):
        percentual = 8 / 100
        return self._salario * percentual
