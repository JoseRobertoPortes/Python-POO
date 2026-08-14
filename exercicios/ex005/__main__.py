from rich import print, inspect
from class_ex005 import Aluno, Professor, Funcionario


def main():
    a1 = Aluno("José", 23, "informatica", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    

    p1 = Professor("Samuel", 25, "biologia", "mestre")
    p1.dar_aula()
    

    f1 = Funcionario(f"Claudia", 27, "secretaria", "secretaria")
    f1.bater_ponto()
    


if __name__ == "__main__":
    main()
