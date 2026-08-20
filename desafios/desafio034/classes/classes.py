from abc import ABC, abstractmethod
from uteis.dinheiro import formatar_moeda


class Funcionario(ABC):
    def __init__(self, nome, salario:float):
        self.nome = nome
        self._salario = salario

    @abstractmethod
    def  calcularbonus(self):
        return

class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    @property
    def salario(self):
        fsalario = formatar_moeda(self._salario)
        return fsalario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario > self._salario:
            self._salario = novo_salario
            print('Salario atualizado com sucesso!')
            return True
        else: raise ValueError('Você não pode abaixar o salario de um funcionario.')

    def calcularbonus(self):
        percentual = 15/100
        bonus = formatar_moeda(self._salario * percentual)
        return bonus

class Dev(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcularbonus(self):
        percentual = 10/100
        bonus = formatar_moeda(self._salario * percentual)
        return bonus


class Designer(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcularbonus(self):
        percentual = 8/100
        bonus = formatar_moeda(self._salario * percentual)
        return bonus


a = Gerente('Jose', 1000)

print(a)