from uteis.num import Real
from abc import ABC, abstractmethod
from rich.panel import Panel


class Funcionario(ABC):
    def __init__(self, nome: str, sal_bruto: float):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.sal_min: float = 1_612
        self.inss = 7.5 / 100

    @abstractmethod
    def calc_sal(self):
        raise NotImplementedError()

    def analisar_sal(self):
        salario_liquido = self.calc_sal()
        qtd_salarios_min = salario_liquido / self.sal_min

        conteudo = (
            f"O salário de [cyan]{self.nome}[/] [purple]({self.__class__.__name__})[/] é [green]{Real(salario_liquido)}[/]\n"
            f"corresponde a [yellow]{qtd_salarios_min:.1f} salários mínimos.[/]"
        )
        return Panel(conteudo, title="Análise de Salário", width=65)


class FuncionarioHorista(Funcionario):
    def __init__(self, nome: str, valor_hora: float, horas_trab: float):
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = valor_hora * horas_trab
        super().__init__(nome, self.sal_bruto)

    def calc_sal(self):
        return self.sal_bruto - ((self.sal_bruto / 100) * 7.5)


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome: str, sal_bruto: float):
        super().__init__(nome, sal_bruto)

    def calc_sal(self):
        return self.sal_bruto - ((self.sal_bruto / 100) * 7.5)
