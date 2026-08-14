import locale as l

l.setlocale(l.LC_ALL, "pt_BR.UTF-8")


class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos.
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(
            f"Conta {self.id} criada com sucesso! saldo de {l.currency(self.saldo, grouping=True)}"
        )

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem {self.saldo} de saldo."

    def depositar(self, valor):
        self.saldo += valor
        print(
            f"Deposito de {l.currency(valor, grouping=True)} autorizado na conta {self.id}"
        )

    def sacar(self, valor):
        if valor > self.saldo:
            print(
                f"(Conta {self.id}) - Saque de {l.currency(valor, grouping=True)} NEGADO. Saldo insuficiente."
            )
        else:
            self.saldo -= valor
            print(f"saque de {l.currency(valor)} autorizado na conta {self.id}")


c1 = ContaBancaria(112, "José", 3000)

c1.depositar(5000)
c1.sacar(40_000)
print(c1)
