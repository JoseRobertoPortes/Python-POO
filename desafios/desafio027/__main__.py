from classes.personagens_rpg import *
from rich import print
from rich.traceback import install

install()


def main():
    p1 = Guerreiro("Jose", 200)
    p2 = Mago("Julia", 300)

    print(p2.Atacar(p1))
    print(p2.Atacar(p1))
    print(p2.Atacar(p1))


if __name__ == "__main__":
    main()
