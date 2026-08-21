from abc import ABC, abstractmethod


class Arquivio(ABC):
    _extensao: str
    app: str


    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho / 1024

    @property
    def nome_completo(self,):
        return (
            f'{self.nome}.{self._extensao} ({self.tamanho:.1f}MB)'

        )

    def abrir(self):
        return (
            f'Abrindo {self.nome_completo} em {self.app}'
        )


class PDF(Arquivio):

    _extensao = 'pdf'
    app = 'Adobe Reader'


class DOC(Arquivio):
    _extensao = 'docx'
    app = 'Microsoft Word'
