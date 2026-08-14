from .classes.circulo import Circulo
from .classes.quadrado import Quadrado
from rich import print
from rich.traceback import install

install()


def main():
    q1 = Circulo(20)

    print(f"Perimetro: {q1.perimetro():.1f} cm\n" f"Area: {q1.area():.1f} cm")


if __name__ == "__main__":
    main()
