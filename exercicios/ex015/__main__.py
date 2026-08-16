
from classes.classes import *
# nao terminado


def main():

    c1 = Carteira(100)
    c2 = Carteira(150)

    if (c1 == c2):
        print("Vocês tem o mesmo valor na carteira")
    else:
        print("As carteiras tem valores diferentes")

    if (c1 <= c2):
        print("A segunda carteira tem mais dinheiro")
    else:
        print("A primeira carteira tem mais dinheiro")

    print(c1)
    print(c2)


if __name__ == '__main__':
    main()
