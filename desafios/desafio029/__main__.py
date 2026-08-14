from classe.diario import Diario
from rich import print


def main():
    diario = Diario()
    diario.Escrever("Oi")
    diario.Escrever("Fiz o exercício!")

    try:
        diario.Ler("CeV!@")
    except PermissionError as erro:
        print(f"[red]{erro}[/]")


if __name__ == "__main__":
    main()
