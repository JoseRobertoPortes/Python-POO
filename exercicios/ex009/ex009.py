class Avaliaçao:
    def __init__(self, nome, diciplina, nota=0):
        self.nome = nome
        self.diciplina = diciplina
        self._nota = nota

    def get_nota(self):
        return self._nota

    def set_nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota invalida!")
