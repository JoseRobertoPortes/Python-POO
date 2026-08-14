from classe.funcionario import *
from rich import print
from rich.traceback import install

install()


def main():
    f1 = FuncionarioHorista("José", 12, 200)
    f2 = FuncionarioMensalista("Julia", 12_000)
    print(f1.analisar_sal())
    print(f2.analisar_sal())


if __name__ == "__main__":
    main()
