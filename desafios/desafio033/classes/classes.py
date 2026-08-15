from abc import ABC
from datetime import datetime


class Pessoa(ABC):
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str | None):
        if novo_nome is not None and len(novo_nome.strip()) >= 5:
            self._nome = novo_nome.strip().capitalize()
        else:
            raise ValueError('O nome precisa ter no mínimo 5 caracteres')

    @property
    def ano_nascimento(self):
        return self._ano_nascimento

    @ano_nascimento.setter
    def ano_nascimento(self, ano):
        idade = datetime.now().year - ano
        if 18 <= idade <= 100 and ano < datetime.now().year:
            self._ano_nascimento = ano
        else:
            raise ValueError('Idade invalida (deve ter entre 18 e 100 anos)')

    @property
    def idade(self):
        return datetime.now().year - self._ano_nascimento


class Aluno(Pessoa):
    cursos_disponiveis = ['Adm', 'Python']

    def __init__(self, nome, ano_nascimento, curso):
        super().__init__(nome, ano_nascimento)
        self.curso = curso

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, novo_curso):
        if novo_curso is not None:
            curso_formatado = novo_curso.strip().capitalize()
            if curso_formatado in self.cursos_disponiveis:
                self._curso = curso_formatado
            else:
                raise ValueError('Curso nao disponivel.')
        else:
            raise ValueError('O curso não pode ser nulo.')