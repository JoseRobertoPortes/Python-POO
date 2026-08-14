from rich import print, inspect


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)

        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} acabou de fazer matricula")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)

        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"O professor {self.nome} começou a aula")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)

        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto")


a1 = Aluno("José", 23, "informatica", "T01")
a1.fazer_aniversario()
a1.fazer_matricula()


p1 = Professor("Samuel", 25, "biologia", "mestre")
p1.dar_aula()


f1 = Funcionario(f"Claudia", 27, "secretaria", "secretaria")
inspect(f1, methods=True)
