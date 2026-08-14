from hashlib import sha256

import locale as l

from desafios.desafio024.classes import cha

l.setlocale(l.LC_ALL, "pt_BR.UTF-8")


class ContaBancaria:
    """
    Cria uma conta bancaria e permite fazer saques e depositos.
    """

    def __init__(
        self,
        _id: int,
        nome: str | None = None,
        saldo: float = 0,
        chave: str | None = None,
    ):
        self._id = _id
        while True:
            if nome is None or len(nome.strip()) < 5:
                print(
                    'O campo "Nome" não foi preenchido ou possui menos de 5 caracteres.'
                )
                nome = str(input("Digite o nome do titular: "))
            else:
                self._titular = nome.strip()
                break

        self.__saldo = saldo
        if chave is None or len(chave) < 6:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode("UTF-8")).hexdigest()
        print(
            f"Conta {self._id} criada com sucesso! saldo de {l.currency(self.__saldo, grouping=True)}"
        )

    def pede_senha(self) -> str:
        from pwinput import pwinput

        while True:
            senha = str(pwinput("Senha: "))
            if len(senha) >= 6:
                break
            else:
                print("A senha precisa ter, no minimo, 6 caracteres")
        return senha

    def __str__(self):
        
        return f"estado atual da conta: {self.__dict__}"

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(
            f"Deposito de {l.currency(valor, grouping=True)} autorizado na conta {self._id}"
        )

    def sacar(self, valor: float, chave: str | None = None):
        valor = abs(valor)

        if chave is None:
            chave = self.pede_senha()

        if self.validar(chave):
            print("Tentando sacar...")
            if valor > self.__saldo:
                print(
                    f"(Conta {self._id}) - Saque de {l.currency(valor, grouping=True)} NEGADO. Saldo insuficiente."
                )
            else:
                self.__saldo -= valor
                print(
                    f"saque de {l.currency(valor, grouping=True)} autorizado na conta {self._id}"
                )
        else:
            print("Senha nao confere. Saque nao autorizado.")

    def validar(self, chave):
        usuario = sha256(chave.encode()).hexdigest()

        if usuario == self.__hash:
            return True
        else:
            return False

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novonome: str | None):
        chave = self.pede_senha()
        if not self.validar(chave):
            print("Senha incorreta. Nome não alterado.")
            return

        if novonome is None or len(novonome.strip()) < 5:
            raise ValueError(f"O nome do titular deve ter no mínimo 5 caracteres.")

        self._titular = novonome.strip()
        print(f"Nome do titular alterado para: {self._titular}")
