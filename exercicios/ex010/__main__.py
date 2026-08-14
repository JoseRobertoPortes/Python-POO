from exercicios.ex010.ex010 import Avaliaçao
from rich import print, inspect


def main():
    av1 = Avaliaçao("pedro", "matematica")
    av1.set_nota(923)
    inspect(av1, private=True)


if __name__ == "__main__":
    main()
