from rich.traceback import install

install()


class Funcionario:
    def __init__(
        self,
        nome="<Não informado/>.",
        cargo="<Não informado./>",
        setor="<Não informado./>",
    ):

        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = "Curso em video"

    def apresentar(self):
        return f"O funcionario {self.nome} trabalha como {self.cargo} no setor de {self.setor} na empresa {self.empresa}"


Funcionario1 = Funcionario("José", "T.i")
print(Funcionario1.apresentar())
