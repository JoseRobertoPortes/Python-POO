from rich import print
from rich.panel import Panel

caixa = Panel(
    "Esse aqui é um painel de exemplo",
    title="Mensagem",
    title_align="left",
    style="red",
)

print(caixa)
