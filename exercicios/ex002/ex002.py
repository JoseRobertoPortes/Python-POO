class Gafanhoto:
    """
    função que recebe 2 paramentros, Gafanhoto(nome, idade)
    e retorna uma mensagem
    """

    def __init__(self, nome="", idade=0):

        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é um gafanhoto e tem {self.idade} anos!"


g1 = Gafanhoto(nome="José", idade=23)
print(g1)

print(g1.__dict__)  
print(g1.__getstate__)  
print(g1.__class__)
print(g1.__doc__)  
