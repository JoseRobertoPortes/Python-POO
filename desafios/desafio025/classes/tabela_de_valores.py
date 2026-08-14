from rich import print
from rich.table import Table
from rich.traceback import install
from .transportes import Moto, Caminhao, Transporte, Drone

install()


def tabela_simples(distancia=0):
    t = Table(title="Tabela de Valores")
    t.add_column("Distancia")
    t.add_column("Tipo")
    t.add_column("Frete")
    t.add_row(
        f"{distancia}",
        f"{type(Moto(distancia)).__name__}",
        f"{Moto(distancia).cal_frete()}",
    )
    t.add_row(
        f"{distancia}",
        f"{type(Drone(distancia)).__name__}",
        f"{Drone(distancia).cal_frete()}",
    )
    t.add_row(
        f"{distancia}",
        f"{type(Caminhao(distancia)).__name__}",
        f"{Caminhao(distancia).cal_frete()}",
    )
    return t
