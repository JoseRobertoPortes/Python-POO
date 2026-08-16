class Numero:

    def __init__(self, valor: int | float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor = self.valor * 2

    def __str__(self) -> str:
        return f'Tenho o valor {self.valor}'


class Texto:

    def __init__(self, texto: str = ''):
        self.texto = texto

    def dobrar(self):
        self.texto = self.texto + " " + self.texto

    def __str__(self) -> str:
        return f'Tenho o texto {self.texto}'


class Lista:

    def __init__(self, lista: list = []):
        self.valores = lista

    def dobrar(self):
        self.valores = self.valores + self.valores

    def __str__(self) -> str:
        return f'Tenho os itens {self.valores}'


class Papel:

    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__(self) -> str:
        return f'O papel está {self.dobrado}'


class Casa:

    def __init__(self):
        pass

    def __str__(self) -> str:
        return f'que engraçado'


def tente_dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f'Tive dificuldades para dobrar {objeto.__class__.__name__}')
