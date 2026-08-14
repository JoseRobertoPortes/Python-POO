from hashlib import sha256


class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            self.__hash = sha256(chave.encode("utf-8")).hexdigest()
        else:
            raise ValueError("Senha Invalida.")

    def validar(self, chave):
        if sha256(chave.encode("utf-8")).hexdigest() == self.__hash:
            print("senha valida")
            return True
        else:
            print("senha invalida")
            return False
