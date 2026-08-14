from classes.termostato import Termostato
from rich import inspect, print

from rich import print, inspect
from rich.traceback import install

install()


def main():
    t = Termostato()
    t.temperatura = 25
    inspect(t, private=True, methods=True)
    print(f"A temperatura atual é {t.temperatura}")


if __name__ == "__main__":
    main()
