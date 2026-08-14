from rich import print, inspect
from classes.credencial import Credencial


def main():
    c = Credencial()
    c.senha = "13Elula"
    c.validar(str(input("Digite a sua senha: ")))


if __name__ == "__main__":
    main()
