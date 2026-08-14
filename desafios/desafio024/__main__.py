from classes.cafe import Cafe
from classes.cha import Cha
from classes.leite import Leite
from rich import print
from rich.traceback import install

install()


def main():
    bebida = Cha()
    bebida.preparar()


if __name__ == "__main__":
    main()
