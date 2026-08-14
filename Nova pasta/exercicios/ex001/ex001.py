class Gafanhoto:
    def __init__(self):

        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é um gafanhoto e tem {self.idade} anos!"


g1 = Gafanhoto()
g1.nome = "José"
g1.idade = 23
g1.aniversario()
print(g1.mensagem())
