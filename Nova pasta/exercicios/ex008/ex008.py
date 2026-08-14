import locale as l

l.setlocale(l.LC_ALL, "pt_BR.UTF-8")


class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos.
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        print(
            f"Conta {self.id} criada com sucesso! __saldo de {l.currency(self.__saldo, grouping=True)}"
        )

    def __str__(self):
        
        return f"estado atual da conta: {self.__dict__}"

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(
            f"Deposito de {l.currency(valor, grouping=True)} autorizado na conta {self.id}"
        )

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(
                f"(Conta {self.id}) - Saque de {l.currency(valor, grouping=True)} NEGADO. Saldo insuficiente."
            )
        else:
            self.__saldo -= valor
            print(f"saque de {l.currency(valor)} autorizado na conta {self.id}")
