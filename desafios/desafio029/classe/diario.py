from rich import print
from rich.console import Console

console = Console()


class Diario:


    def __init__(self):
        self.__senha = "CeV!@"
        self.__conteudo = ""

    def Escrever(self, msg: str = ""):
        if not isinstance(msg, str):
            raise TypeError("A mensagem deve ser uma string.")
        self.__conteudo += msg + "\n"

    def Ler(self, senha: str = ""):
        if senha == self.__senha:
            return console.print(self.__conteudo, style="bold green")
        raise PermissionError("Senha inválida.")

    @property
    def senha(self):
        raise PermissionError(
            "Você não tem permissão para visualizar a senha.")

    @senha.setter
    def senha(self, nova_senha: str):
        if not isinstance(nova_senha, str) or not nova_senha.strip():
            raise ValueError("A nova senha não pode ser vazia.")
        self.__senha = nova_senha

    def alterar_senha(self, senha_atual: str, nova_senha: str):
        if senha_atual != self.__senha:
            raise PermissionError("A senha atual está incorreta.")

        self.senha = nova_senha
        print("Senha alterada com sucesso!")
