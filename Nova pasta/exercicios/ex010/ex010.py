class Avaliaçao:
    def __init__(self, nome, diciplina, nota=0):
        self.nome = nome
        self.diciplina = diciplina
        self._nota = nota

    @property
    def nota(self):
        return self.nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota invalida!")
