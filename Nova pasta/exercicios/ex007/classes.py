from abc import ABC, abstractmethod  


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def estudar(cls):
        pass

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)

        self.curso = curso
        self.turma = turma

    def estudar(self):
        print(
            f"O aluno {self.nome} está fazendo um curso de {self.curso} na turma {self.turma}"
        )

    def fazer_matricula(self):
        print(f"O aluno {self.nome} acabou de fazer matricula")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)

        self.especialidade = especialidade
        self.nivel = nivel

    def estudar(self):
        print(f"{self.nome} é especialista em {self.especialidade} no {self.nivel}")

    def dar_aula(self):
        print(f"O professor {self.nome} começou a aula")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)

        self.cargo = cargo
        self.setor = setor

    def estudar(self):
        print(f"{self.nome} se especializa para a area de {self.setor}")

    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto")
