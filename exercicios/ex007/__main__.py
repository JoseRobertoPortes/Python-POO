from traceback import print_tb

from rich import print, inspect
from classes import Aluno, Professor, Funcionario


def main():
    a1 = Aluno("José", 23, "informatica", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    

    p1 = Professor("Samuel", 25, "biologia", "mestrado")
    p1.dar_aula()
    

    f1 = Funcionario(f"Claudia", 27, "secretaria", "secretaria")
    f1.bater_ponto()
    
    print("-" * 20)

    a1.estudar()
    p1.estudar()
    f1.estudar()


if __name__ == "__main__":
    main()
