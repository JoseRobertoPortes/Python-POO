from classes.classes import Aluno
from rich import print, inspect


def main():
    a = Aluno("sasaa", 2000, 'adm')
    print(a.cursos_disponiveis)

if __name__ == "__main__":
    main()
