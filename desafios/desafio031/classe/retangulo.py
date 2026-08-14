class Retangulo:
    def __init__(self, base: int | float = 1, altura: int | float = 1):
        self.base = base
        self.altura = altura

    @property
    def base(self) -> int | float:
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError('O valor deve ser um numero.')
        if valor < 0:
            raise ValueError('Valor invalido para a base')
        self._base = valor

    @property
    def altura(self) -> int | float:
        return self._altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError('O valor deve ser um numero.')
        if valor < 0:
            raise ValueError('Valor invalido para a altura')
        self._altura = valor

    @property
    def area(self):
        return f'Base = {self.base}, altura = {self.altura}, area = {self.base * self.altura}m²'

    @area.setter
    def area(self):
        raise PermissionError('O parametro de area é calculado automaticamente.')

    @property
    def medidas(self) -> str:
        return f'Base = {self.base} \nAltura = {self.altura}'

    @medidas.setter
    def medidas(self, valores: tuple):
        if not isinstance(valores, tuple):
            raise TypeError('Os valores devem ser informados dentro de um tupla "ex:(base, altura)"')
        if len(valores) != 2:
            raise ValueError('Informe uma tupla com apenas 2 valores numericos')
        self.base = valores[0]
        self.altura = valores[1]