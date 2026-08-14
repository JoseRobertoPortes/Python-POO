from rich import inspect

from classes.contabancaria import *


def main():
    cc = ContaBancaria(111, "José Roberto", 10_000, "guanabara")

    cc.nome = "Adailton"
    inspect(cc)


if __name__ == "__main__":
    main()
