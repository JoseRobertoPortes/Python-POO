from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self._nome = nome

    @abstractmethod
    def emitir_som(self):
        pass


class Cachorro(Animal):
    def emitir_som(self):
        print(f"{self._nome} acabou de dizer 'AU! AU! AU!'")


class Gato(Animal):
    def emitir_som(self):
        print(f"{self._nome} acabou de dizer 'MIAU! MIAU!'")


class Pato(Animal):
    def emitir_som(self):
        print(f"{self._nome} acabou de dizer 'QUACK! QUACK!'")


class Galinha(Animal):
    def emitir_som(self):
        print(f"{self._nome} acabou de dizer 'PÓ! PÓ! PÓ!'")